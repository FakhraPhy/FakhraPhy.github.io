"""Download remote publication thumbnails into assets/images/covers/ and
point each publication's `cover:` field at the local copy.

Usage (from the repository root):  python scripts/download_covers.py
"""
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
COVERS = ROOT / "assets" / "images" / "covers"
COVERS.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

for md in sorted((ROOT / "_publications").rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    m = re.search(r"^cover:\s+(https?://\S+)\s*$", text, flags=re.M)
    if not m:
        continue
    url = m.group(1)
    ext = ".png" if url.lower().endswith(".png") else ".jpg"
    target = COVERS / (md.stem + ext)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=60) as resp:
            target.write_bytes(resp.read())
    except Exception as exc:  # keep the remote link if download fails
        print(f"[skip] {md.name}: {exc}")
        continue
    local = "/assets/images/covers/" + target.name
    md.write_text(text.replace(m.group(0), f"cover:          {local}"), encoding="utf-8")
    print(f"[ok]   {md.name} -> {local}")
