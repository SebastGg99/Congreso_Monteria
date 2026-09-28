---
name: slides-fisica
description: Estilo y flujo de trabajo para construir slides académicas de física en LaTeX/Beamer con la estética personal del usuario (barra de título verde redondeada con numeración, subtítulo con filete rojo, bloques verde claro, ecuaciones numeradas de forma continua, diagramas TikZ propios, texto telegráfico en español). Usa esta skill siempre que haya que crear, reescribir, extender, revisar o pulir slides, diapositivas, presentaciones, ponencias, charlas, journal alerts, seminarios o defensas en este repositorio, aunque el usuario no mencione Beamer ni "la skill"; también al convertir una tesis, artículo o resultados en una presentación.
---

# Slides académicas de física — estilo del usuario

El usuario construye presentaciones de física con criterios altos de ponencia:
sobrias, densas en física pero ligeras en texto, donde cada slide tiene **una idea**
y la ecuación o la figura es el protagonista. El referente canónico es
`baseline/slides.tex` (journal alert sobre kMC adaptativo). La plantilla lista
para copiar está en `assets/plantilla.tex`: úsala siempre como punto de partida
del preámbulo en lugar de reescribirlo, porque la identidad visual depende de
detalles finos (anchos de caja, filete de 2.5 pt, tamaños de fuente) que se
pierden al reinventarlos.

## 1. Fuente de verdad del contenido

- El contenido científico sale **solo** de la fuente que el usuario designe
  (tesis, artículo, resultados). No inventes números, parámetros, tiempos,
  ajustes ni conclusiones; si un dato falta en la fuente, déjalo fuera o marca
  un `% TODO:` en el `.tex` y menciónalo al usuario.
- Otros artículos pueden dar contexto (motivar, definir, citar), pero cuando
  contradigan la fuente de verdad, manda la fuente de verdad.
- Conserva la notación de la fuente (símbolos, subíndices, nombres de
  parámetros). Si la fuente es inconsistente, unifica y avisa.
- Las citas van en forma corta dentro de la slide: *Autor et al.* (año), en gris
  pequeño o dentro del pie de figura. Sin bibliografía completa salvo que se pida.

## 2. Identidad visual (no negociable salvo pedido explícito)

| Elemento | Especificación |
|---|---|
| Clase | `beamer`, `aspectratio=169`, `11pt`, `babel` español con `es-nodecimaldot,es-noshorthands` |
| Fuente | `lmodern` + `professionalfonts`; sin símbolos de navegación, sin pie de página |
| Paleta | `azul` RGB(20,83,56) verde principal · `azulclaro` RGB(228,241,233) fondo suave · `gris` RGB(90,90,90) texto secundario · `acento` RGB(176,58,46) rojo para énfasis/flechas |
| Título de frame | barra verde redondeada, texto blanco `\large\bfseries`, número `n / N` alineado a la derecha en verde claro |
| Subtítulo | caja `azulclaro` con filete rojo de 2.5 pt a la izquierda, `\small\itshape`; se usa para la **definición** o el **mensaje central** de la slide, no para un subtítulo decorativo |
| Bloques | redondeados, sin sombra, título verde/blanco, cuerpo verde claro. Un `block` con título vacío `{}` es el recurso para **resaltar la ecuación clave** |
| Viñetas | `\small$\blacktriangleright$` |
| Pies de figura | macro `\fig{Fig.~N. Descripción.}`: `\scriptsize` gris, numeración continua en todo el deck, en español |
| Portada | frame `[plain]`: caja verde redondeada con título en `\Large\bfseries`, filete fino, evento en cursiva; autores `\large`; afiliación `\small` gris; caja clara con dato de publicación/tesis |
| Cierre | frame `¡Gracias por su atención!` con un `block{}` centrado `\Large ¿Preguntas?` |

El verde encaja con la identidad UdeA; si el usuario pide otra paleta, cambia
solo los cuatro `\definecolor` y conserva los roles.

## 3. Cómo se escribe una slide

- **Una idea por slide.** El título dice el tema; el subtítulo (si hay) dice la
  conclusión o la definición en una línea.
- **Texto telegráfico.** Frases nominales, no párrafos. Cadenas lógicas con
  flechas: `$\sigma\uparrow \Rightarrow \Delta\mu\uparrow \Rightarrow l_c\downarrow$`.
  Negrita para la palabra que el público debe retener; `\emph{}` para conceptos.
  Máximo ~5 viñetas, con `\setlength{\itemsep}{0.6em}` o `0.7em`.
- **Términos técnicos** en inglés cuando son de uso común (*kink*, *adatom*,
  *step*), en cursiva o tal cual en tablas; el resto en español.
- **Ecuaciones** con `\tag{n}` manual y numeración **continua** a lo largo de
  todo el deck (la audiencia puede referirse a "la ecuación 7"). `align` para
  familias de ecuaciones; `\!\left(...\right)` en exponenciales; `\dfrac` dentro
  de texto. Debajo, una línea `\footnotesize` que define los símbolos nuevos.
- **Tablas** con `booktabs` (`\toprule/\midrule/\bottomrule`), `@{}` en los
  bordes, `\renewcommand{\arraystretch}{1.15–1.35}`, fila destacada en negrita.
  Etiqueta de tabla estilo `{\color{azul}\bfseries Tabla 1.} descripción`.
- **Figuras**: `\includegraphics` con `width=\linewidth` dentro de columnas, o
  `height=0.60–0.74\textheight` cuando son altas. Copia las figuras usadas a
  `figures/` junto al `.tex` (la carpeta debe compilar sola, p. ej. en Overleaf).
- **Diagramas propios en TikZ** cuando una idea se entiende mejor dibujada que
  importada (paisaje de energía, red SOS con alturas, vecindad de von Neumann,
  fronteras periódicas, flujos de cajas). Siempre con la paleta: estructura en
  `azul`/`azul!NN`, énfasis y flechas en `acento`, anotaciones `\scriptsize`
  en `gris`. Estilos `cab`, `caja`, `paso`, `etapa` ya definidos en la plantilla.
- **Recortes**: muchas figuras de simulación traen mucho blanco; recorta con
  `trim=l b r t,clip` en vez de achicarlas. Las unidades son bp de la figura
  *a su dpi*: revisa el chunk `pHYs` del PNG (a 120 dpi, 1 px = 0.6 bp). Si un
  mismo recorte se repite, define una macro (p. ej. `\snap{altura}{archivo}`).

## 4. Patrones de layout (catálogo)

Todos con `\begin{columns}[c|T,onlytextwidth]` y anchos que sumen ≈0.97–0.98.

1. **Figura | ecuaciones** (0.47/0.51 o 0.42/0.55): figura con `\fig{}` a un
   lado, `align` numerado al otro.
2. **Ecuaciones | bloque clave** (0.52/0.45): derivación a la izquierda, bloque
   con el resultado a la derecha.
3. **Tres paneles TikZ** (3×0.32) con etiqueta `{\color{azul}\bfseries\small …}`
   debajo de cada uno, y un `block` centrado abajo que resume.
4. **Flujo de cajas** Motivación → Causa → Problema con flechas `paso` y una
   barra verde de *Propuesta* abajo.
5. **Resultados**: dos figuras (2×0.385) + columna estrecha (0.22) con tabla
   de parámetros `\scriptsize`; pie de figura común abajo.
6. **Resultado + interpretación**: figura (0.56) | tabla + `block` con la
   lectura física (0.40).
7. **Snapshot a ancho completo** con `height≈0.62\textheight` y subtítulo que
   explica el código de colores.
8. **Conclusiones**: viñetas (0.56) | bloques *Limitaciones* y *Perspectivas* (0.40).

## 5. Arco narrativo típico

Portada → motivación/problema → concepto base (definición en subtítulo) →
supuestos del modelo (geometría, eventos) → termodinámica/ecuaciones →
tasas/algoritmo → validación → resultados (cinética, morfología) → comparación
con experimento → conclusiones y perspectivas → cierre con preguntas.
Ajusta la longitud a la duración: ~1 slide por minuto de charla.

## 6. Convenciones de archivo

- Cabecera del `.tex` con bloque de comentario `% ====` que dice qué es la
  charla, la referencia y cómo compilar.
- Separador por frame: `% ---------------------------------------------------------------- N`.
- Preferir **comentar** variantes descartadas en vez de borrarlas cuando el
  usuario esté iterando; en una versión nueva limpia, no arrastrar basura.
- Versiones en `slides/vN/` (cada una autocontenida: `slides.tex` + `figures/`).
  Una iteración nueva copia la anterior a `vN+1/` en lugar de sobrescribir.

## 7. Compilar y revisar (obligatorio antes de entregar)

1. Compilar: `tectonic slides.tex` (o `pdflatex` dos veces). En este entorno
   `tectonic` puede estar en `~/snap/claude-code/common/local/bin/`.
2. Revisar el log: ningún `Overfull \hbox` mayor a ~5 pt, ningún `Overfull \vbox`
   (contenido que se sale por abajo), ninguna figura faltante.
3. Mirar el resultado: `python3 scripts/hoja_contactos.py slides.pdf hoja.png 3`
   y leer la imagen; renderizar individualmente (`pdftoppm -r 80 -f N -l N`)
   las slides dudosas. Buscar: texto que choca con el borde, figuras diminutas,
   slides vacías o recargadas, columnas desbalanceadas.
4. Iterar hasta que todas las slides respiren. Reportar al usuario qué
   decisiones de contenido tomaste y qué datos faltaban en la fuente.

## Checklist rápido

- [ ] Preámbulo copiado de `assets/plantilla.tex` sin alterar el estilo
- [ ] Cada número/parámetro verificado contra la fuente de verdad
- [ ] Ecuaciones `\tag` continuas; figuras `Fig.~N.` continuas
- [ ] Subtítulos solo donde aportan definición o mensaje
- [ ] Figuras copiadas a `figures/`; compila sin errores ni desbordes
- [ ] Hoja de contactos revisada visualmente
