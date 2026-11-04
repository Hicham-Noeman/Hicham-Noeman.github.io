# _brand

Source files and personal assets. Folders starting with `_` are **not published** by GitHub Pages.

| File | What it is |
|---|---|
| `qr-code.png` | QR code (with HN logo) to the website, for business cards and print. Scans as `https://hicham-noeman.dev/?utm_source=qr`. |
| `qr-code-plain.svg` | Same QR code without the logo, as a vector for professional printing. |
| `email-signature.html` | Email signature. Open it in a browser, copy between the lines, paste into Outlook or Gmail signature settings. |
| `cv.html` | Source of `/cv/Hicham-Noeman-CV.pdf`. |
| `build_ar.py` | Generates the Arabic page `ar/index.html` from `index.html`. |
| `build_en.py` | One-off script that added the FAQ, CV buttons and language switch to `index.html` (already applied; don't run again). |

## After editing the English page

Run `python _brand/build_ar.py` to regenerate the Arabic page. If it stops with an error, the English text it
needs to translate has changed: update the matching line in `build_ar.py`.

## Rebuilding the CV PDF

From the repo folder, start a local server (`python -m http.server 8765`), then:

```
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --no-pdf-header-footer --virtual-time-budget=6000 --print-to-pdf="cv/Hicham-Noeman-CV.pdf" "http://127.0.0.1:8765/_brand/cv.html"
```
