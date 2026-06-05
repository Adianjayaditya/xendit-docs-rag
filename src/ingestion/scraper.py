import re
import time
import asyncio
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import async_playwright

SEED_URLS = [
    "https://docs.xendit.co/docs",
    "https://docs.xendit.co/apidocs",
]

OUTPUT_DIR = Path(r"C:\rag-midtrans-docs\data\raw")

DELAY = 1.2

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

VALID_PATTERN = re.compile(
    r"^https://docs\.xendit\.co/(docs|apidocs)/[\w\-]+"
)

def fetch_static(url: str) -> BeautifulSoup | None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except requests.RequestException as e:
        print(f"  [GAGAL] {e}")
        return None

async def fetch_apidocs(page, url: str) -> BeautifulSoup | None:
    """
    Fetch halaman apidocs dengan Playwright.
    Langkah:
      1. Goto URL
      2. Tunggu konten utama muncul di DOM
      3. Klik semua tombol "Expand All" agar schema ter-render
      4. Ambil HTML
    """
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_selector("h1", timeout=15000)
        await asyncio.sleep(1.5)

        expand_buttons = await page.query_selector_all(
            "button:has-text('Expand All'), "
            "[class*='expand']:has-text('Expand'), "
            "button[aria-label*='expand']"
        )
        for btn in expand_buttons:
            try:
                await btn.click()
                await asyncio.sleep(0.3)
            except Exception:
                pass

        if expand_buttons:
            await asyncio.sleep(1.0)

        html = await page.content()
        return BeautifulSoup(html, "html.parser")

    except Exception as e:
        print(f"  [GAGAL Playwright] {e}")
        return None

def extract_links(soup: BeautifulSoup) -> list[str]:
    found = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].split("#")[0].rstrip("/")
        if href.startswith("/"):
            href = "https://docs.xendit.co" + href
        if VALID_PATTERN.match(href):
            found.add(href)
    return list(found)

def extract_markdown(soup: BeautifulSoup, url: str) -> dict | None:
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(strip=True)

    content_el = (
        soup.find("article")
        or soup.find("main")
        or soup.find("div", class_="document360-editorjs")
        or soup.find("div", class_="article-content")
        or soup.find("body")
    )

    if not content_el:
        return None

    for tag in content_el.find_all(["nav", "footer", "script", "style", "noscript"]):
        tag.decompose()

    content_md = md(
        str(content_el),
        heading_style="ATX",
        bullets="-",
        strip=["img"],
    )
    content_md = re.sub(r"\n{3,}", "\n\n", content_md).strip()

    if len(content_md) < 100:
        return None

    return {"url": url, "title": title, "content": content_md}

def save(data: dict, output_dir: Path) -> Path:
    slug    = data["url"].rstrip("/").split("/")[-1]
    section = "apidocs" if "/apidocs/" in data["url"] else "docs"

    dest = output_dir / section
    dest.mkdir(parents=True, exist_ok=True)

    filepath = dest / f"{slug}.md"
    content  = (
        f"---\n"
        f"url: {data['url']}\n"
        f"title: \"{data['title']}\"\n"
        f"section: {section}\n"
        f"product: xendit\n"
        f"---\n\n"
        f"{data['content']}"
    )
    filepath.write_text(content, encoding="utf-8")
    return filepath

async def run():
    print("=" * 55)
    print("  Xendit Docs Scraper (hybrid)")
    print(f"  Output : {OUTPUT_DIR}")
    print("=" * 55 + "\n")

    visited = set()
    queue   = list(SEED_URLS)
    stats   = {"ok": 0, "skip": 0, "gagal": 0}

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=HEADERS["User-Agent"],
            )
        await context.route(
            "**/*.{png,jpg,jpeg,gif,svg,ico,webp,woff,woff2,ttf}",
            lambda route: route.abort()
        )
        page = await context.new_page()

        while queue:
            url = queue.pop(0)

            if url in visited:
                continue
            visited.add(url)

            slug    = url.rstrip("/").split("/")[-1]
            section = "apidocs" if "/apidocs/" in url else "docs"
            outfile = OUTPUT_DIR / section / f"{slug}.md"

            # Resume
            if outfile.exists():
                print(f"  [SKIP]   {slug}")
                stats["skip"] += 1
                continue

            is_apidocs = "/apidocs" in url
            mode_label = "Playwright" if is_apidocs else "requests "
            print(f"  [GET/{mode_label}] {slug}", end="", flush=True)

            if is_apidocs:
                soup = await fetch_apidocs(page, url)
            else:
                soup = fetch_static(url)

            if not soup:
                stats["gagal"] += 1
                print(" → GAGAL")
                continue

            new_links = extract_links(soup)
            added = 0
            for link in new_links:
                if link not in visited and link not in queue:
                    queue.append(link)
                    added += 1

            data = extract_markdown(soup, url)
            if not data:
                stats["gagal"] += 1
                print(" → KOSONG")
                continue

            save(data, OUTPUT_DIR)
            stats["ok"] += 1
            print(f" → OK  ({len(data['content']):,} chars, +{added} URL baru)")

            time.sleep(DELAY)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())