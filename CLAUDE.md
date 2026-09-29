# CLAUDE.md

Repositorio para construir las slides (Beamer) de una ponencia en un congreso en
Montería sobre el trabajo de grado de Sebastian Gaviria Giraldo (Instituto de
Física, UdeA, 2026): *Estudio del crecimiento de cristales de hemozoína
($\beta$-hematina) en Plasmodium falciparum mediante un modelo de Monte Carlo
cinético*. Asesores: Olga Lucía López Acevedo y Hernán David Salinas Jiménez.

## Reglas

- **Estilo de slides:** usar siempre la skill `slides-fisica`
  (`.claude/skills/slides-fisica/`). Su plantilla `assets/plantilla.tex` define la
  identidad visual; no reinventar el preámbulo.
- **Fuente de verdad del contenido:** `baseline/references/tesis_latex/`, en
  concreto `main.tex` (capítulos, ecuaciones, resultados) y `calculo_mace.tex`
  (MACE). Los archivos `seccion_0.tex`, `seccion_1.tex`, `seccion_resumen.tex` y
  `anexos.tex` son restos de la plantilla UdeA y **no** contienen contenido del
  trabajo. No inventar números: si algo no está en la tesis, dejar `% TODO:` y
  avisar.
- **Contexto secundario** (solo para motivar/definir, nunca contradice la tesis):
  - `baseline/references/modern_kMC/` — Nagpal *et al.*, Chem. Eng. Sci. 299
    (2024) 120472, en markdown (`result.md`) + figuras. Modelo kMC adaptativo que
    la tesis adapta.
  - `baseline/references/MACE/` — **ojo, nombres cruzados**: contiene
    *MACE-POLAR-1* (Batatia *et al.*, 2026).
  - `baseline/references/MACE_Polar/` — contiene el *MACE* original
    (NeurIPS 2022).
- **Referente estético:** `baseline/slides.tex` (journal alert previo del
  usuario; sus figuras están en `baseline/references/modern_kMC/images/`).
- **No modificar `baseline/`.** Es material de referencia.
- **Versionado:** cada iteración vive en `slides/vN/slides.tex`. Las figuras son
  **compartidas** en `slides/figures/` (desde v4, `\graphicspath{{../figures/}}`);
  las figuras nuevas se añaden ahí. Para iterar, copiar `vN` a `vN+1` y editar la copia.
- Idioma de las slides y de la comunicación con el usuario: español.

## Compilar y revisar

```bash
cd slides/v4
tectonic slides.tex            # o pdflatex slides.tex (dos veces)
python3 ../../.claude/skills/slides-fisica/scripts/hoja_contactos.py slides.pdf /tmp/hoja.png 3
```

En este entorno no hay TeX Live del sistema; `tectonic` está instalado en
`~/snap/claude-code/common/local/bin/` (ya en el `PATH`). PyMuPDF (`import pymupdf`)
está disponible para renderizar páginas.

Detalle práctico: los PNG de `results/` de la tesis están a 120 dpi
(1 px = 0.6 bp); tenerlo en cuenta al usar `trim` en `\includegraphics`.

## Pendientes conocidos (v4)

- Fecha en la portada (el nombre del congreso ya está; `% TODO` en la portada).
- Charla de **15 minutos**: v4 tiene 16 slides principales + 6 de respaldo tras
  `\appendix` (`appendixnumberbeamer`, numeración aparte).
