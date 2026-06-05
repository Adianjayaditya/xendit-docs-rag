import re
import asyncio
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from playwright.async_api import async_playwright

BASE_URL   = "https://docs.xendit.co"

SEED_URLS  = [
    "https://docs.xendit.co/apidocs",
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

OUTPUT_DIR = Path(r"C:\rag-midtrans-docs\data\raw\apidocs")

DELAY = 2.5 

VALID_PATTERN = re.compile(
    r"^https://docs\.xendit\.co/(docs|apidocs)/[\w\-]+"
)

async def fetch_page(page, url: str, retries: int = 3) -> str | None:
    for attempt in range(1, retries + 1):
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=45000)
            await page.wait_for_selector("h1", timeout=20000)
            await asyncio.sleep(2.0)

            expand_buttons = await page.query_selector_all(
                ".expand-collapse-btn, .expand-btn, [aria-expanded='false']"
            )
            for btn in expand_buttons:
                try:
                    await btn.click()
                    await asyncio.sleep(0.15)
                except Exception:
                    pass
            if expand_buttons:
                await asyncio.sleep(1.0)

            return await page.content()

        except Exception as e:
            print(f" -> Attempt {attempt}/{retries} gagal: {e}")
            if attempt < retries:
                wait = attempt * 5  # tunggu 5s, 10s, 15s
                print(f"    Tunggu {wait}s sebelum retry...")
                await asyncio.sleep(wait)

    return None

def get_validation(el: Tag) -> str:
    """Kumpulkan semua validation rules → string dipisah ' | '."""
    container = el.find(class_="api-schema-validation-container")
    if not container:
        return ""
    parts = []
    for v in container.find_all(class_="api-schema-validation"):
        text = re.sub(r"\s+", " ", v.get_text(" ", strip=True)).strip()
        if text:
            parts.append(text)
    return " | ".join(parts)


def parse_property(el: Tag, depth: int = 0) -> list[str]:
    """Parse satu .api-schema-property → satu baris markdown dengan indentasi."""
    indent = "  " * depth
    title_el = el.find(class_="api-schema-title")
    if not title_el:
        return []

    name_el  = title_el.find(class_="name")
    dtype_el = title_el.find(class_="data-type-name")
    req_el   = title_el.find(class_="data-type-required")
    desc_el  = title_el.find(class_="description")

    name_t  = name_el.get_text(strip=True) if name_el else ""
    type_t  = dtype_el.get_text(strip=True) if dtype_el else ""
    req_t   = "required" if req_el else "optional"
    desc_t  = re.sub(r"\s+", " ", desc_el.get_text(" ", strip=True)).strip() if desc_el else ""
    valid_t = get_validation(el)

    if not name_t:
        return []

    line = f"{indent}- **{name_t}** ({type_t}, {req_t})"
    if desc_t:
        line += f": {desc_t}"
    if valid_t:
        line += f" [{valid_t}]"
    return [line]


def parse_object(el: Tag, depth: int = 0) -> list[str]:
    """
    Parse satu .api-schema-object → header + children ter-indent.
    Punya struktur:
      div.api-schema-title (header: name fw-700, data-type, description)
      div.indent-level     (children properties)
    """
    indent = "  " * depth
    lines  = []

    name_el  = el.find(class_="fw-700") or el.find(class_="name")
    dtype_el = el.find(class_="data-type-name")
    req_el   = el.find(class_="data-type-required")
    title_el = el.find(class_="api-schema-title")
    desc_el  = title_el.find(class_="description") if title_el else None

    name_t  = name_el.get_text(strip=True) if name_el else ""
    type_t  = dtype_el.get_text(strip=True) if dtype_el else "object"
    req_t   = "required" if req_el else "optional"
    desc_t  = re.sub(r"\s+", " ", desc_el.get_text(" ", strip=True)).strip() if desc_el else ""

    if not name_t:
        return []

    hdr = f"{indent}- **{name_t}** ({type_t}, {req_t})"
    if desc_t:
        hdr += f": {desc_t}"
    lines.append(hdr)

    indent_level = el.find(class_="indent-level")
    if indent_level:
        lines.extend(parse_children(indent_level, depth + 1))
    return lines


def parse_array(el: Tag, depth: int = 0) -> list[str]:
    """
    Parse satu .api-schema-array → header + children ter-indent.
    Punya struktur:
      div.api-schema-title (header: name fw-700, description)
      div (wrapper) → children items
    """
    indent = "  " * depth
    lines  = []

    title_el = el.find(class_="api-schema-title", recursive=False)
    name_el  = el.find(class_="fw-700") or el.find(class_="name")
    desc_el  = title_el.find(class_="description") if title_el else None

    name_t = name_el.get_text(strip=True) if name_el else ""
    desc_t = re.sub(r"\s+", " ", desc_el.get_text(" ", strip=True)).strip() if desc_el else ""

    if not name_t:
        return []

    hdr = f"{indent}- **{name_t}** (array, optional)"
    if desc_t:
        hdr += f": {desc_t}"
    lines.append(hdr)

    for child in el.children:
        if not isinstance(child, Tag):
            continue
        if "api-schema-title" in child.get("class", []):
            continue
        lines.extend(parse_children(child, depth + 1))
    return lines


def parse_children(container: Tag, depth: int) -> list[str]:
    """
    Rekursif parse semua children dari container.
    Menangani: api-schema-property, api-schema-object, api-schema-array,
               dan div wrapper tanpa class.
    """
    lines = []
    for child in container.children:
        if not isinstance(child, Tag):
            continue
        cls = child.get("class", [])

        if "api-schema-property" in cls:
            lines.extend(parse_property(child, depth))

        elif "api-schema-object" in cls:
            lines.extend(parse_object(child, depth))

        elif "api-schema-array" in cls:
            lines.extend(parse_array(child, depth))

        else:
            inner_obj  = child.find(class_="api-schema-object",  recursive=False)
            inner_arr  = child.find(class_="api-schema-array",   recursive=False)
            inner_prop = child.find(class_="api-schema-property", recursive=False)

            if inner_obj:
                lines.extend(parse_object(inner_obj, depth))
            elif inner_arr:
                lines.extend(parse_array(inner_arr, depth))
            elif inner_prop:
                for prop in child.find_all(class_="api-schema-property", recursive=False):
                    lines.extend(parse_property(prop, depth))
            elif child.get_text(strip=True):
                lines.extend(parse_children(child, depth))

    return lines


def clean_variant_label(raw: str) -> str:
    """
    'Payments_API_Pay'            → 'PAY'
    'Payments_API_PayAndSave'     → 'PAY_AND_SAVE'
    'Payments_API_Http400InvalidValueError' → 'HTTP_400_INVALID_VALUE_ERROR'
    """
    label = re.sub(r"^Payments_API_", "", raw)
    label = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", label).upper()
    label = re.sub(r"HTTP(\d)", r"HTTP_\1", label)
    return label


def get_schema_content_from_media(media_container: Tag) -> Tag | None:
    """
    Dari div.api-media-type, ambil api-content yang berisi schema property.
    Pola: api-media-type > api-content (bukan example-container)
    """
    api_media = media_container.find(class_="api-media-type")
    if not api_media:
        return None
    for child in api_media.children:
        if isinstance(child, Tag) and "api-content" in child.get("class", []):
            return child
    return None


def extract_body_params(body_section: Tag) -> list[str]:
    """
    Ekstrak Body Parameters dari api-request-body.
    Mendukung oneOf variant (PAY, PAY_AND_SAVE, PAY_WITH_TOKEN, REUSABLE_PAYMENT_CODE).
    """
    lines = []
    variants = body_section.find_all(class_="api-response")
    if not variants:
        return lines

    lines.append("## Body Parameters\n")
    if len(variants) > 1:
        lines.append(
            "> Endpoint ini memiliki beberapa skema request (oneOf). "
            "Pilih variant sesuai kebutuhan.\n"
        )

    for variant in variants:
        label_el  = variant.find(class_="api-status-oneOfSchema")
        raw_label = label_el.get_text(strip=True) if label_el else ""
        label     = clean_variant_label(raw_label) if raw_label else "DEFAULT"

        if len(variants) > 1:
            lines.append(f"### Variant: {label}\n")

        api_content = variant.find(class_="api-content")
        if not api_content:
            continue

        media_type_content = api_content.find(class_="api-media-type-content")
        if not media_type_content:
            lines.extend(parse_children(api_content, 0))
        else:
            schema_content = get_schema_content_from_media(media_type_content)
            if schema_content:
                lines.extend(parse_children(schema_content, 0))

        lines.append("")

    return lines



def extract_response_schema(http_code: str, resp_el: Tag) -> list[str]:
    """
    Ekstrak schema dari satu api-response (satu HTTP status block).
    Mendukung:
    - Response tunggal (201): api-schema-object langsung
    - Response oneOf (400, 403, dll.): api-schema-object berisi api-response-body > api-response (×N)
    """
    lines = []

    inner_content = resp_el.find(class_="api-content")
    if not inner_content:
        return lines

    media_type_content = inner_content.find(class_="api-media-type-content")
    if not media_type_content:
        lines.extend(parse_children(inner_content, 0))
        return lines

    schema_content = get_schema_content_from_media(media_type_content)
    if not schema_content:
        return lines

    root_obj = schema_content.find(class_="api-schema-object")
    if not root_obj:
        lines.extend(parse_children(schema_content, 0))
        return lines
    nested_rb = root_obj.find(class_="api-response-body")

    if nested_rb:
        oneof_variants = nested_rb.find(class_="api-content")
        if not oneof_variants:
            return lines

        error_responses = oneof_variants.find_all(class_="api-response", recursive=False)
        if len(error_responses) > 1:
            lines.append(f"> Status **{http_code}** memiliki beberapa schema error (oneOf).\n")

        for ev in error_responses:
            ev_label_el  = ev.find(class_="api-status-oneOfSchema")
            ev_raw_label = ev_label_el.get_text(strip=True) if ev_label_el else ""
            ev_label     = clean_variant_label(ev_raw_label) if ev_raw_label else "ERROR"

            if len(error_responses) > 1:
                lines.append(f"#### {ev_label}\n")

            ev_content = ev.find(class_="api-content")
            if ev_content:
                lines.extend(parse_children(ev_content, 0))
            lines.append("")
    else:
        indent_level = root_obj.find(class_="indent-level")
        if indent_level:
            lines.extend(parse_children(indent_level, 0))
        else:
            lines.extend(parse_children(root_obj, 0))
        lines.append("")

    return lines


def extract_responses(resp_body_el: Tag) -> list[str]:
    """
    Ekstrak semua HTTP response dari api-response-body (direct child api-endpoint).
    """
    lines = []

    api_content = resp_body_el.find(class_="api-content")
    if not api_content:
        return lines

    # Ambil daftar kode HTTP dari response-tab
    response_tab = api_content.find(class_="response-tab")
    if response_tab:
        status_els = response_tab.find_all(class_="api-status")
        http_codes = [el.get_text(strip=True) for el in status_els]
    else:
        http_codes = []

    api_responses = api_content.find_all(class_="api-response", recursive=False)

    if not api_responses:
        return lines

    lines.append("## Responses\n")

    for i, resp in enumerate(api_responses):
        http_code = http_codes[i] if i < len(http_codes) else f"Status {i+1}"

        desc_el = resp.find(class_="description")
        desc_t  = ""
        if desc_el:
            desc_t = re.sub(r"\s+", " ", desc_el.get_text(" ", strip=True)).strip()
            desc_t = re.sub(r"Show example.*", "", desc_t, flags=re.DOTALL).strip()

        lines.append(f"### {http_code}{' — ' + desc_t if desc_t else ''}\n")

        schema_lines = extract_response_schema(http_code, resp)
        if schema_lines:
            lines.extend(schema_lines)
        else:
            lines.append("_(Tidak ada schema)_\n")
            lines.append("")

    return lines


def extract_content(soup: BeautifulSoup, url: str) -> dict | None:
    lines = []
    h1 = soup.find("h1")
    if not h1:
        return None
    title = h1.get_text(strip=True)
    lines.append(f"# {title}\n")

    api_endpoint = soup.find(class_="api-endpoint")
    if not api_endpoint:
        body = soup.find("main") or soup.find(class_="content") or soup.body
        if body:
            lines.append(body.get_text("\n", strip=True)[:5000])
        content = "\n".join(lines)
        if len(content) < 100:
            return None
        return {"url": url, "title": title, "content": content}

    path_section = api_endpoint.find(class_="api-path")
    if path_section:
        method = path_section.find(class_="api-http-method")
        path   = path_section.find(class_="api-url")
        desc   = path_section.find(class_="description")

        m = method.get_text(strip=True).upper() if method else ""
        p = path.get_text(strip=True) if path else ""
        d = re.sub(r"\s+", " ", desc.get_text(" ", strip=True)).strip() if desc else ""

        if m and p:
            lines.append(f"## Endpoint\n`{m} {p}`\n")
        if d:
            lines.append(f"{d}\n")
    else:
        ep = api_endpoint.find(class_="api-endpoint")
        if ep:
            method = ep.find(class_="api-http-method")
            path   = ep.find(class_="api-url")
            desc   = ep.find(class_="description")
            m = method.get_text(strip=True).upper() if method else ""
            p = path.get_text(strip=True) if path else ""
            d = re.sub(r"\s+", " ", desc.get_text(" ", strip=True)).strip() if desc else ""
            if m and p:
                lines.append(f"## Endpoint\n`{m} {p}`\n")
            if d:
                lines.append(f"{d}\n")

    param_section = api_endpoint.find(class_="api-parameter-container")
    if param_section:
        params = param_section.find_all(class_="api-parameter")
        if params:
            lines.append("## Header Parameters\n")
            for p in params:
                name_el  = p.find(class_="api-parameter-name")
                dtype_el = p.find(class_="api-parameter-data-type")
                desc_el  = p.find(class_="description")

                n = name_el.get_text(strip=True) if name_el else ""
                t = dtype_el.get_text(strip=True) if dtype_el else ""
                d = re.sub(r"\s+", " ", desc_el.get_text(" ", strip=True)).strip() if desc_el else ""

                line = f"- **{n}** ({t})"
                if d:
                    line += f": {d}"
                lines.append(line)
            lines.append("")

    body_section = api_endpoint.find(class_="api-request-body")
    if body_section:
        variants = body_section.find_all(class_="api-response")
        if variants:
            lines.extend(extract_body_params(body_section))
        else:
            ac  = body_section.find(class_="api-content")
            mtc = ac.find(class_="api-media-type-content") if ac else None
            if mtc:
                schema_content = get_schema_content_from_media(mtc)
                if schema_content:
                    for child in schema_content.children:
                        if not isinstance(child, Tag):
                            continue
                        if "btn-container" in " ".join(child.get("class", [])):
                            continue
                        root_obj = child.find(class_="api-schema-object")
                        if root_obj:
                            indent_level = root_obj.find(class_="indent-level")
                            lines.append("## Webhook Payload Schema\n")
                            if indent_level:
                                lines.extend(parse_children(indent_level, 0))
                            else:
                                lines.extend(parse_children(root_obj, 0))
                            lines.append("")
                        break

    main_resp_body = api_endpoint.find(class_="api-response-body", recursive=False)
    if main_resp_body:
        resp_lines = extract_responses(main_resp_body)
        if not resp_lines:
            body_section = api_endpoint.find(class_="api-request-body")
            if body_section:
                mtc = body_section.find(class_="api-media-type-content")
                if mtc:
                    schema_content = get_schema_content_from_media(mtc)
                    if schema_content:
                        lines.append("## Webhook Payload Schema\n")
                        lines.extend(parse_children(schema_content, 0))
                        lines.append("")
        else:
            lines.extend(resp_lines)

    content = "\n".join(lines)
    if len(content) < 100:
        return None

    return {"url": url, "title": title, "content": content}


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


def extract_links(soup: BeautifulSoup) -> list[str]:
    """Temukan semua link /apidocs/... dari halaman."""
    found = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].split("#")[0].rstrip("/")
        if href.startswith("/"):
            href = BASE_URL + href
        if VALID_PATTERN.match(href):
            found.add(href)
    return list(found)

async def run():
    print("=" * 60)
    print("  Xendit Apidocs Scraper v4")
    print(f"  Base  : {BASE_URL}/apidocs")
    print(f"  Output: {OUTPUT_DIR}")
    print("=" * 60 + "\n")

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
        failed_urls = []
        while queue:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)

            slug    = url.rstrip("/").split("/")[-1]
            outfile = OUTPUT_DIR / f"{slug}.md"

            if outfile.exists():
                print(f"  [SKIP]  {slug}")
                stats["skip"] += 1
                continue

            print(f"  [GET]   {slug}", end="", flush=True)

            html = await fetch_page(page, url)
            if not html:
                stats["gagal"] += 1
                print(" -> GAGAL, lanjut ke URL berikutnya")
                failed_urls.append(url)
                continue

            soup = BeautifulSoup(html, "html.parser")
            for link in extract_links(soup):
                if link not in visited and link not in queue:
                    queue.append(link)
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
        if failed_urls:
            failed_path = OUTPUT_DIR / "_failed_urls.txt"
            failed_path.write_text("\n".join(failed_urls), encoding="utf-8")
            print(f"\n  [INFO] {len(failed_urls)} URL gagal disimpan ke {failed_path}")
            print("  Jalankan ulang script untuk retry — file yang sudah ada akan di-skip otomatis")

    print("\n" + "=" * 60)
    print("  SELESAI")
    print(f"  OK    : {stats['ok']}")
    print(f"  Skip  : {stats['skip']}")
    print(f"  Gagal : {stats['gagal']}")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(run())