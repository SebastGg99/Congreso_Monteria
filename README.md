# Congreso Montería — slides

Presentación (LaTeX/Beamer, 16:9) del trabajo de grado

> **Estudio del crecimiento de cristales de hemozoína ($\beta$-hematina) en
> *Plasmodium falciparum* mediante un modelo de Monte Carlo cinético**
> Sebastian Gaviria Giraldo — asesores: Olga Lucía López Acevedo y Hernán David
> Salinas Jiménez. Instituto de Física, Universidad de Antioquia (2026).
> Código de las simulaciones: <https://github.com/SebastGg99/MalariaProject>

## Estructura

```
.
├── baseline/                       material de referencia (no se edita)
│   ├── slides.tex                  presentación previa: referente de estilo
│   └── references/
│       ├── tesis_latex/            FUENTE DE VERDAD (main.tex, calculo_mace.tex, figures/, results/)
│       ├── modern_kMC/             Nagpal et al. (2024), kMC adaptativo multirrégimen
│       ├── MACE/                   MACE-POLAR-1 (Batatia et al., 2026)
│       └── MACE_Polar/             MACE original (NeurIPS 2022)
├── slides/
│   └── v1/                         primera versión: slides.tex, slides.pdf, figures/
└── .claude/skills/slides-fisica/   skill con el estilo de las slides
    ├── SKILL.md                    guía de estilo y flujo de trabajo
    ├── assets/plantilla.tex        preámbulo + patrones de frame
    └── scripts/hoja_contactos.py   hoja de contactos PNG de un PDF
```

## Compilar

```bash
cd slides/v1
tectonic slides.tex      # o: pdflatex slides.tex  (dos pasadas)
```

Paquetes usados: `beamer`, `babel` (spanish), `amsmath`, `graphicx`, `booktabs`,
`array`, `tikz` (`arrows.meta`, `positioning`, `calc`). Compila también en Overleaf
subiendo la carpeta `slides/vN/` completa.

## Estilo

Resumen de la skill `slides-fisica`: barra de título verde redondeada con número
`n / N`, subtítulo en caja verde claro con filete rojo para la definición o el
mensaje de la slide, bloques verde claro sin sombra, ecuaciones y figuras
numeradas de forma continua, diagramas TikZ propios con la paleta
(verde `#145338`, verde claro `#E4F1E9`, gris `#5A5A5A`, rojo `#B03A2E`) y texto
telegráfico en español.

## Contenido de v1 (26 slides)

1. Portada · 2. Malaria y hemozoína · 3. Hipótesis y objetivo ·
4. Unidad de crecimiento · 5. Ensamblaje jerárquico · 6. Cinética (CNT, Avrami,
Pasternack, dos etapas) · 7. kMC · 8. Algoritmo BKL · 9. Modelos 2D y 3D ·
10. Tasas 2D · 11. Regímenes y sitios · 12. Termodinámica · 13. Adsorción y
desorción · 14. Migración e incorporación · 15. Selección de eventos ·
16. MACE-POLAR · 17. Relajación · 18. Energías de enlace · 19. Validación
(lisozima) · 20. Cinética de conversión · 21. Morfología 2D · 22. Morfología 3D
isotrópica · 23. Morfología 3D anisotrópica · 24. Comparación con AFM ·
25. Conclusiones · 26. Cierre
