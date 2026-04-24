import re
import asyncio
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

# ── Konfigurasi ───────────────────────────────────────────────────────────

SEED_URLS = [
    "https://docs.xendit.co/apidocs/create-payment-request",
]

OUTPUT_DIR = Path(r"C:\rag-midtrans-docs\data\raw\apidocs")

DELAY = 1.2  # detik antar request

VALID_PATTERN = re.compile(r"^$")

# ── Playwright fetch ──────────────────────────────────────────────────────

async def fetch_page(page, url: str) -> str | None:
    """Fetch halaman dengan Playwright, tunggu JS selesai render."""
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_selector("h1", timeout=15000)
        await asyncio.sleep(2.0)

        # Klik tombol Expand All jika ada
        expand_buttons = await page.query_selector_all(
            "button:has-text('Expand All'), "
            "button[aria-label*='expand'], "
            "[class*='expand-all']"
        )
        for btn in expand_buttons:
            try:
                await btn.click()
                await asyncio.sleep(0.3)
            except Exception:
                pass
        if expand_buttons:
            await asyncio.sleep(1.0)

        return await page.content()
    except Exception as e:
        print(f"  [GAGAL fetch] {e}")
        return None

# ── Custom extractor ──────────────────────────────────────────────────────

def prop_to_line(el) -> str:
    """Konversi satu api-schema-property menjadi satu baris teks."""
    name     = el.find(class_="name")
    dtype    = el.find(class_="data-type-name")
    required = el.find(class_="data-type-required")
    desc     = el.find(class_="description")
    valid    = el.find(class_="api-schema-validation")

    name_t  = name.get_text(strip=True) if name else ""
    type_t  = dtype.get_text(strip=True) if dtype else ""
    req_t   = "required" if required else "optional"
    desc_t  = desc.get_text(strip=True) if desc else ""
    valid_t = re.sub(r"\s+", " ", valid.get_text(strip=True)) if valid else ""

    line = f"- **{name_t}** ({type_t}, {req_t})"
    if desc_t:
        line += f": {desc_t}"
    if valid_t:
        line += f" [{valid_t}]"
    return line


def extract_content(soup: BeautifulSoup, url: str) -> dict | None:
    """
    Ekstrak konten dari halaman apidocs menjadi Markdown terstruktur.
    Menggunakan class name spesifik Xendit.
    """
    lines = []

    # ── 1. Title ─────────────────────────────────────────────────────────
    h1 = soup.find("h1")
    if not h1:
        return None
    title = h1.get_text(strip=True)
    lines.append(f"# {title}\n")

    # ── 2. Endpoint (method + path + deskripsi) ───────────────────────────
    ep = soup.find(class_="api-endpoint")
    if ep:
        method = ep.find(class_="api-http-method")
        path   = ep.find(class_="api-url")
        desc   = ep.find(class_="description")

        m = method.get_text(strip=True).upper() if method else ""
        p = path.get_text(strip=True) if path else ""
        d = desc.get_text(strip=True) if desc else ""

        lines.append(f"## Endpoint\n`{m} {p}`\n")
        if d:
            lines.append(f"{d}\n")

    # ── 3. Header parameters ──────────────────────────────────────────────
    param_section = soup.find(class_="api-parameter-container")
    if param_section:
        params = param_section.find_all(class_="api-parameter")
        if params:
            lines.append("## Header Parameters\n")
            for p in params:
                name  = p.find(class_="api-parameter-name")
                dtype = p.find(class_="api-parameter-data-type")
                desc  = p.find(class_="description")

                n = name.get_text(strip=True) if name else ""
                t = dtype.get_text(strip=True) if dtype else ""
                d = desc.get_text(strip=True) if desc else ""

                line = f"- **{n}** ({t})"
                if d:
                    line += f": {d}"
                lines.append(line)
            lines.append("")

    # ── 4. Body parameters ────────────────────────────────────────────────
    body_section = soup.find(class_="api-request-body")
    if body_section:
        props = body_section.find_all(class_="api-schema-property")
        if props:
            lines.append("## Body Parameters\n")
            for p in props:
                lines.append(prop_to_line(p))
            lines.append("")

    # ── 5. Response codes ─────────────────────────────────────────────────
    known_codes = {"200", "201", "204", "400", "401", "403", "404", "409", "422", "500", "503"}
    response_codes = []
    for code_el in soup.find_all(class_="api-code"):
        code_text = code_el.get_text(strip=True)
        if code_text in known_codes:
            response_codes.append(code_text)

    if response_codes:
        lines.append("## Response Codes\n")
        for code in sorted(set(response_codes)):
            lines.append(f"- **{code}**")
        lines.append("")

    # ── 6. Response body properties ───────────────────────────────────────
    resp_body = soup.find(class_="api-response-body")
    if resp_body:
        props = resp_body.find_all(class_="api-schema-property")
        if props:
            lines.append("## Response Body\n")
            for p in props:
                lines.append(prop_to_line(p))
            lines.append("")

    content = "\n".join(lines)

    if len(content) < 100:
        return None

    return {"url": url, "title": title, "content": content}

# ── Simpan file ───────────────────────────────────────────────────────────

def save(data: dict) -> Path:
    slug = data["url"].rstrip("/").split("/")[-1]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    filepath = OUTPUT_DIR / f"{slug}.md"
    content  = (
        f"---\n"
        f"url: {data['url']}\n"
        f"title: \"{data['title']}\"\n"
        f"section: apidocs\n"
        f"product: xendit\n"
        f"---\n\n"
        f"{data['content']}"
    )
    filepath.write_text(content, encoding="utf-8")
    return filepath

# ── Ekstrak link ──────────────────────────────────────────────────────────

def extract_links(soup: BeautifulSoup) -> list[str]:
    found = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].split("#")[0].rstrip("/")
        if href.startswith("/"):
            href = "https://docs.xendit.co" + href
        if VALID_PATTERN.match(href):
            found.add(href)
    return list(found)

# ── Main crawler ──────────────────────────────────────────────────────────

async def run():
    print("=" * 55)
    print("  Xendit Apidocs Scraper")
    print(f"  Output : {OUTPUT_DIR}")
    print("=" * 55 + "\n")

    visited = set()
    queue   = list(SEED_URLS)
    stats   = {"ok": 0, "skip": 0, "gagal": 0}

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context()
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
            outfile = OUTPUT_DIR / f"{slug}.md"

            if outfile.exists():
                print(f"  [SKIP] {slug}")
                stats["skip"] += 1
                continue

            print(f"  [GET]  {slug}", end="", flush=True)

            html = await fetch_page(page, url)
            if not html:
                stats["gagal"] += 1
                print(" -> GAGAL")
                continue

            soup = BeautifulSoup(html, "html.parser")

            # Kumpulkan link baru
            for link in extract_links(soup):
                if link not in visited and link not in queue:
                    queue.append(link)

            # Ekstrak dan simpan
            data = extract_content(soup, url)
            if not data:
                stats["gagal"] += 1
                print(" -> KOSONG")
                continue

            save(data)
            stats["ok"] += 1
            print(f" -> OK ({len(data['content']):,} chars)")

            await asyncio.sleep(DELAY)

        await browser.close()

    print("\n" + "=" * 55)
    print("  SELESAI")
    print(f"  OK    : {stats['ok']}")
    print(f"  Skip  : {stats['skip']}")
    print(f"  Gagal : {stats['gagal']}")
    print("=" * 55)


if __name__ == "__main__":
    asyncio.run(run())