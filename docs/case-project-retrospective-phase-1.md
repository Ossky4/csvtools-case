# Case Project — Retrospectiva de la fase 1 en csvtools-case

## Propósito del ciclo
Validar si Codex puede ejecutar cleanup de arquitectura pequeño, reversible y revisable en un repositorio más real que el sandbox inicial, manteniendo control de alcance y bajo riesgo.

## Resumen de PRs realizadas

### PR1 — Marco del Case Project
Se añadió un documento de alcance y hotspots admisibles para enmarcar el experimento.

### PR2 — Cleanup local mínimo
Se eliminó un import no usado en `csvtools/add_count.py` como primer cambio conservador y reversible.

### PR3 — Cleanup multiarchivo real
Se extrajo la inicialización compartida de CLI desde `csvtools/add_count.py` y `csvtools/csvadd.py` a `csvtools/cli_utils.py`, reduciendo duplicación sin cambiar comportamiento observable.

### PR4 — Blindaje de la frontera extraída
Se añadieron tests focalizados para `csvtools.cli_utils`, cubriendo la frontera limpiada en la PR3 sin tocar producción.

## Qué funcionó bien
- PRs pequeñas y de una sola intención.
- Buen control de alcance por parte de Codex.
- Capacidad para distinguir entre limpieza local, refactor multiarchivo y blindaje.
- Validación suficiente para cambios pequeños y reversibles.
- Revisión humana barata y trazable mediante microevaluaciones.

## Fricciones observadas
- El entorno de tests requiere `PYTHONPATH=.` para evitar fallos de importación de `csvtools`.
- Esa fricción no bloqueó el ciclo, pero obliga a distinguir entre problemas del entorno y efectos reales del cambio.
- Conviene no mezclar todavía cleanup de código con arreglos de setup de tests.

## Patrones operativos que conviene mantener
- Una sola intención por PR.
- Cambios pequeños, reversibles y fáciles de revisar.
- Separar cleanup, blindaje y documentación en PRs distintas.
- Reportar explícitamente qué falló por entorno y qué falló por el cambio.
- Añadir microevaluación humana después de cada revisión.

## Qué no quedó probado todavía
- Cambios de arquitectura de mayor alcance.
- Cleanup que afecte más de una frontera relevante a la vez.
- Decisiones con impacto en packaging, setup de tests o contratos CLI.
- Evaluación de Codex en zonas con mayor ambigüedad estructural.

## Recomendación de siguiente paso
Cerrar esta fase como primer ciclo válido del Case Project.

A partir de aquí, hay dos opciones razonables:
1. continuar en este repositorio con una segunda fase explícita (por ejemplo, entorno de tests o segundo hotspot distinto),
2. o cerrar el caso aquí y comparar este resultado con otro repositorio candidato.

La recomendación actual es no continuar por inercia: cualquier siguiente PR debería responder a una hipótesis nueva y explícita.
