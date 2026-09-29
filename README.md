# Congreso Montería — slides

Presentación (LaTeX/Beamer, 16:9) para el *X Encuentro Regional de Física y
I Congreso Internacional de Ciencias Físicas de Montería*, basada en el trabajo
de grado

> **Estudio del crecimiento de cristales de hemozoína ($\beta$-hematina) en
> *Plasmodium falciparum* mediante un modelo de Monte Carlo cinético**
> Sebastian Gaviria Giraldo — asesores: Olga Lucía López Acevedo y Hernán David
> Salinas Jiménez. Instituto de Física, Universidad de Antioquia (2026).
> Cálculos MACE: D. J. Duque Tamayo.
> Código de las simulaciones: <https://github.com/SebastGg99/MalariaProject>

Charla de **15 minutos**, con un arco **multiescala**: de la estructura
microscópica de la $\beta$-hematina y sus energías de enlace (MACE-POLAR) a la
nucleación 2D y el crecimiento mesoscópico del cristal (kMC 3D).

## Estructura

```
.
├── baseline/                       material de referencia (no se edita)
│   ├── slides.tex                  presentación previa: referente de estilo
│   └── references/
│       ├── tesis_latex/            FUENTE DE VERDAD (main.tex, calculo_mace.tex, figures/, results/)
│       ├── modern_kMC/             Nagpal et al. (2024), kMC adaptativo multirrégimen
│       ├── MACE/                   MACE-POLAR-1 (Batatia et al., 2026)   ← nombres cruzados
│       └── MACE_Polar/             MACE original (NeurIPS 2022)          ←
├── slides/
│   ├── figures/                    figuras compartidas por todas las versiones
│   ├── v3/                         orden multiescala, 24 slides
│   └── v4/                         versión actual: 15 min (16 + 6 de respaldo)
└── .claude/skills/slides-fisica/   skill con el estilo de las slides
    ├── SKILL.md                    guía de estilo y flujo de trabajo
    ├── assets/plantilla.tex        preámbulo + patrones de frame
    └── scripts/hoja_contactos.py   hoja de contactos PNG de un PDF
```

Cada versión vive en `slides/vN/slides.tex`; para iterar se copia `vN` a
`vN+1` y se edita la copia. Las figuras nuevas se añaden a `slides/figures/`
(v4 las carga con `\graphicspath{{../figures/}}`).

## Compilar

```bash
cd slides/v4
tectonic slides.tex      # o: pdflatex slides.tex  (dos pasadas)
python3 ../../.claude/skills/slides-fisica/scripts/hoja_contactos.py slides.pdf /tmp/hoja.png 4
```

Paquetes usados: `beamer`, `babel` (spanish), `amsmath`, `graphicx`, `booktabs`,
`array`, `tikz` (`arrows.meta`, `positioning`, `calc`), `appendixnumberbeamer`.
Para Overleaf, subir la carpeta `slides/` conservando `figures/` junto a `vN/`.

## Estilo

Resumen de la skill `slides-fisica`: barra de título verde redondeada con número
`n / N`, subtítulo en caja verde claro con filete rojo para la definición o el
mensaje de la slide, bloques verde claro sin sombra, ecuaciones y figuras
numeradas de forma continua, diagramas TikZ propios con la paleta
(verde `#145338`, verde claro `#E4F1E9`, gris `#5A5A5A`, rojo `#B03A2E`) y texto
telegráfico en español.

## Contenido de v4 (15 min)

**Charla (16 slides)**

| # | Slide | Escala / bloque |
|---|---|---|
| 1 | Portada | |
| 2 | La malaria: detoxificación del hemo en hemozoína | Introducción |
| 3 | Hipótesis, objetivo y hoja de ruta (microscópico → mesoscópico) | |
| 4 | Estructura de la $\beta$-hematina: UC $\pi$--$\pi$ y ensamblaje jerárquico | Microscópica |
| 5 | Potencial MACE-POLAR (arquitectura, Batatia *et al.*, 2026) | |
| 6 | Energías de enlace $E_{pb}$ por dirección | |
| 7 | Cinética de cristalización: CNT, Avrami, Pasternack, dos etapas | Nucleación y crecimiento |
| 8 | Nucleación 2D y regímenes de crecimiento superficial | |
| 9 | Monte Carlo cinético y algoritmo BKL | kMC |
| 10 | Modelo kMC 3D: red SOS y sitios de adsorción | |
| 11 | Modelo kMC 3D: tasas de transición (anisotrópicas) | |
| 12 | Resultados: cinética de conversión | Resultados y discusión |
| 13 | Resultados: morfología superficial (kMC 3D anisotrópico) | |
| 14 | Comparación con experimento: AFM (Olafson *et al.*, 2017) | |
| 15 | Conclusiones y perspectivas | |
| 16 | ¡Gracias! / Preguntas | |

**Respaldo** (tras `\appendix`, numeración aparte): relajación estructural del
cristal · red kMC (vecindad, fronteras periódicas, SOS) · selección y ejecución
de eventos · validación con lisozima · morfología 3D isotrópica.

## Historial de versiones

- **v1** — primera versión completa (26 slides), modelos kMC 2D y 3D.
- **v2** — se retira el modelo kMC 2D; solo el modelo 3D (24 slides).
- **v3** — reordenada con el arco multiescala (24 slides).
- **v4** — recorte a 15 min, figura de arquitectura de MACE-POLAR, material de
  respaldo y figuras compartidas en `slides/figures/`.

v1 y v2 quedan solo en el historial de git.
