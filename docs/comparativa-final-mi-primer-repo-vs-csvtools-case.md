# Comparativa final — mi-primer-repo vs csvtools-case

## Propósito
Comparar los dos casos realizados para evaluar en qué condiciones Codex trabaja mejor y qué tipo de señal aporta cada entorno.

## Caso 1 — mi-primer-repo
Este repositorio funcionó como sandbox inicial para validar el método de trabajo con Codex en condiciones controladas.

### Qué se probó
- PRs pequeñas y de una sola intención.
- Tests puntuales.
- Bugfixes pequeños.
- Mejoras de UX acotadas.
- Refactors pequeños, incluyendo un caso multiarchivo.
- Cambios mixtos de código + tests + documentación.

### Qué señal aportó
`mi-primer-repo` permitió confirmar que el método básico funciona bien cuando:
- el contexto es simple,
- el riesgo es bajo,
- la validación es barata,
- y el alcance está bien delimitado.

También sirvió para establecer un patrón operativo:
- AGENTS.md claro,
- PR pequeña,
- checks explícitos,
- microevaluación humana tras revisión.

## Caso 2 — csvtools-case
Este repositorio funcionó como Case Project de cleanup de arquitectura en un entorno más real que el sandbox inicial.

### Qué se probó
- PR1 documental para delimitar alcance y hotspots.
- Cleanup local mínimo.
- Cleanup multiarchivo real con extracción de bootstrap CLI compartido.
- Blindaje con tests de la frontera extraída.
- Estabilización del entorno de tests para permitir `pytest -q` directo.
- Un segundo hotspot distinto, de menor entidad estructural.

### Qué señal aportó
`csvtools-case` permitió verificar que Codex también puede trabajar con control en un repo más real, siempre que:
- el hotspot esté bien delimitado,
- la PR siga siendo pequeña,
- el cambio sea reversible,
- y la validación del repo sea suficientemente estable.

Además, mostró que mejorar primero la infraestructura mínima de validación (`pytest -q`) aumenta la calidad de todas las PRs posteriores.

## Diferencias clave entre ambos casos

### mi-primer-repo
- contexto más simple y controlado,
- señal rápida,
- bajo coste de revisión,
- más útil para establecer el método base.

### csvtools-case
- contexto más real y menos artificial,
- más valor para evaluar cleanup arquitectónico pequeño,
- más necesidad de separar problemas del repo de efectos del cambio,
- mejor señal sobre disciplina multiarchivo y sobre la importancia del entorno de tests.

## Aprendizajes operativos comunes
En ambos casos, Codex rindió mejor cuando se mantuvieron estas condiciones:
- una sola intención por PR,
- cambios pequeños y revisables,
- restricciones explícitas,
- validación clara,
- distinción entre fallo del entorno y fallo del cambio,
- microevaluación humana breve tras cada revisión.

## Límites observados
- El valor disminuye cuando la tarea es demasiado pequeña y se acerca más a higiene local que a mejora estructural significativa.
- No se ha probado todavía comportamiento en cambios de mayor ambigüedad o mayor alcance estructural.
- El entorno de validación importa mucho: si el repo tiene fricción operativa, la calidad de la señal baja.

## Conclusión
Los dos casos, en conjunto, sugieren que Codex funciona bien como operador de ejecución para:
- cleanup pequeño,
- refactors locales o multiarchivo acotados,
- blindaje con tests,
- y cambios controlados en repositorios con validación barata.

La evidencia es especialmente fuerte cuando el sistema de trabajo incluye:
- contrato operativo claro,
- PRs pequeñas,
- checks explícitos,
- y revisión humana disciplinada.

## Recomendación del siguiente experimento
No seguir por inercia en ninguno de estos dos repositorios.

El siguiente paso debería ser un nuevo Case Project con una hipótesis distinta y explícita, por ejemplo:
1. un repo más real con hotspots algo más ambiguos,
2. un caso de integración con dependencias entre módulos un poco más ricas,
3. o un caso donde haya que decidir entre varias alternativas de cleanup con más juicio estructural.

## Estado de revisión
Aprobada tras revisión.

### Microevaluación
- alcance bien acotado,
- documento de cierre útil y revisable,
- consolida bien los aprendizajes de ambos casos,
- sin tocar código ni expandir el alcance,
- buena base para decidir el siguiente experimento.

