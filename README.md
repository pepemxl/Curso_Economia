# Curso de Economía

Programa de **40 semanas** para formar un analista financiero integral, combinando teoría
económica, herramientas cuantitativas y las aplicaciones prácticas de las finanzas modernas.

El temario completo, con las 160 sesiones, vive en **[`docs/index.md`](docs/index.md)** y se
publica como sitio MkDocs. Este README no lo duplica: solo explica cómo trabajar con el repositorio.

---

## Estructura

```
docs/                  Contenido del curso (fuente del sitio)
  index.md             Temario completo y estado de avance por semana
  nivel_01..04/        4 niveles × 10 semanas × 4 sesiones
  images/              Figuras generadas (NO editar a mano: ver `make figures`)
src/
  estilo_figuras.py    Paleta y utilidades comunes de las figuras
  nivel_*/semana_*/    Scripts `fig_*.py` que generan cada figura
  containers/docs/     Dockerfile e imagen del sitio
mkdocs.yml             Configuración del sitio
```

## Levantar la documentación

Con Docker (no requiere instalar nada más):

```bash
make up_docs          # build + run, sirve en http://localhost:8085
```

En local, con Python:

```bash
make docs_deps        # instala las dependencias fijadas
make docs_serve       # http://127.0.0.1:8085 con live-reload
```

## Regenerar las figuras

Las imágenes de `docs/images/` son **artefactos**: se generan desde los scripts de `src/`.
Para modificar una figura, edita su script y vuelve a ejecutar:

```bash
make figures_deps     # matplotlib + numpy (solo la primera vez)
make figures          # ejecuta todos los src/**/fig_*.py -> docs/images/
```

## Antes de hacer commit

```bash
make docs_build       # mkdocs build --strict: falla ante enlaces rotos o config inválida
```

Es el mismo comando que ejecuta la CI (`.github/workflows/docs.yml`).

## Convenciones del contenido

* Cada semana son 4 sesiones: **Fundamentos**, **Profundización**, **Aplicación Práctica** y
  **Caso de Estudio y Evaluación**.
* Los ejercicios de `session_04.md` llevan su solución en un bloque plegable
  `??? success "Solución del Ejercicio C"`, para que el alumno pueda intentarlo antes de verla.
* Las fórmulas usan LaTeX (`$...$` en línea, `$$...$$` en bloque). **Deja siempre una línea en
  blanco entre dos bloques `$$` consecutivos**, o se fusionan y no se renderizan.
* Los diagramas usan fences ```` ```mermaid ````.

## Recomendaciones para aprovechar el curso

1. **Materiales:** *Principios de Economía* (Mankiw) y *Fundamentos de Finanzas Corporativas*
   (Brealey, Myers, Allen) cubren la mayor parte del Nivel 1 y el Nivel 3.
2. **Herramientas:** domina Excel. El 80 % de las tareas en finanzas se resuelven con un Excel
   bien estructurado.
3. **Hábito de lectura:** sigue diariamente noticias económicas (Bloomberg, Financial Times,
   Wall Street Journal, Reuters) para aplicar la teoría a la realidad.
4. **Evaluación semanal:** resuelve el ejercicio de la sesión 4 **antes** de abrir la solución.
