#!/usr/bin/env python3
"""Genera una hoja de contactos (PNG) con las páginas de un PDF de slides.

Sirve para revisar de un vistazo el ritmo visual del deck: desbordes,
slides vacías o recargadas, consistencia de márgenes.

Uso:
    python3 hoja_contactos.py slides.pdf salida.png [columnas] [inicio] [n] [dpi]

    columnas  número de columnas de la grilla (defecto 3)
    inicio    índice (base 0) de la primera página (defecto 0)
    n         número de páginas a incluir (defecto: todas)
    dpi       resolución del PNG (defecto 60)

Requiere PyMuPDF (`import pymupdf`).
"""
import sys

import pymupdf


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src = pymupdf.open(sys.argv[1])
    out = sys.argv[2]
    cols = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    start = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    n = int(sys.argv[5]) if len(sys.argv) > 5 else len(src)
    dpi = int(sys.argv[6]) if len(sys.argv) > 6 else 60

    pages = list(range(start, min(start + n, len(src))))
    w, h = src[0].rect.width, src[0].rect.height
    pad = 6
    rows = (len(pages) + cols - 1) // cols

    doc = pymupdf.open()
    sheet = doc.new_page(width=cols * (w + pad) + pad, height=rows * (h + pad) + pad)
    sheet.draw_rect(sheet.rect, color=None, fill=(0.6, 0.6, 0.6))
    for k, i in enumerate(pages):
        r, c = divmod(k, cols)
        x, y = pad + c * (w + pad), pad + r * (h + pad)
        sheet.show_pdf_page(pymupdf.Rect(x, y, x + w, y + h), src, i)
    sheet.get_pixmap(dpi=dpi).save(out)
    print(f"{out}: {len(pages)} páginas")


if __name__ == "__main__":
    main()
