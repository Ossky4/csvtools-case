# CODEX_CASE_PLAYBOOK.md

## Objetivo
Definir una secuencia estándar para ejecutar Case Projects con Codex en repositorios reales, manteniendo:
- alcance pequeño,
- señal útil,
- validación barata,
- y revisión humana disciplinada.

---

## Hipótesis operativa base
Codex rinde mejor cuando:
- el objetivo está delimitado,
- la PR tiene una sola intención,
- el cambio es pequeño y reversible,
- existe validación mínima ejecutable,
- y hay revisión humana breve al cierre.

---

## Perfil de repositorio candidato

### Buen candidato
- pequeño o mediano,
- ejecutable localmente,
- con tests o checks mínimos,
- con deuda estructural visible pero contenida,
- sin infraestructura pesada,
- sin alta criticidad.

### Señales favorables
- lógica mezclada con IO,
- validaciones repetidas,
- helpers mal ubicados,
- duplicación local,
- bootstrap repetido,
- entorno de tests frágil pero corregible.

### Señales desfavorables
- caos extremo,
- sin forma razonable de validar,
- despliegue o secretos en el camino crítico,
- demasiada ambigüedad de dominio,
- superficie demasiado grande para PRs pequeñas.

---

## Hotspots admisibles

### Sí
- validaciones duplicadas,
- helpers repetidos,
- mezcla local de lógica pura con IO,
- bootstrap repetido,
- acoplamiento ligero reducible,
- extracción pequeña de responsabilidad clara,
- mejora mínima del entorno de tests.

### No
- rediseño general,
- cambios de contrato visibles,
- consolidación masiva de carpetas,
- migraciones amplias,
- cleanup cosmético sin señal útil,
- múltiples hotspots a la vez.

---

## Secuencia estándar de un Case Project

### PR1 — marco del caso
Documento corto con:
- objetivo,
- alcance,
- hotspots admisibles,
- exclusiones,
- secuencia prevista.

### PR2 — cleanup local mínimo
Cambio pequeño, reversible y de una sola intención.

### PR3 — cleanup multiarchivo real
Refactor pequeño que mejora una frontera concreta entre 2 o más archivos.

### PR4 — blindaje
Tests o cobertura específica sobre la frontera tratada en PR3.

### PR5 — retrospectiva de fase
Documento breve con:
- qué se hizo,
- qué funcionó,
- qué fricciones aparecieron,
- qué no quedó probado.

---

## Fase 2 opcional
Abrir solo si existe una hipótesis nueva y explícita.

Ejemplos válidos:
- entorno de tests,
- segundo hotspot distinto,
- comparación con otro repo,
- caso con mayor ambigüedad estructural.

No continuar por inercia.

---

## Tipos de PR válidos

### Tipo A — documental
Marco, retrospectiva, comparación o cierre.

### Tipo B — cleanup local
Una sola zona, una sola intención, diff pequeño.

### Tipo C — cleanup multiarchivo
Mejora pequeña de frontera entre módulos o entrypoints.

### Tipo D — blindaje
Tests o cobertura focalizada sobre una frontera recién tocada.

### Tipo E — entorno mínimo de validación
Cambios pequeños que permiten ejecutar checks de forma directa y estable.

---

## Criterios de aprobación
Una PR merece aprobación si:
- tiene una sola intención,
- el diff es pequeño y revisable,
- la solución es conservadora,
- la validación es suficiente para su tamaño,
- no expande alcance,
- y distingue claramente entre fallo del entorno y efecto del cambio.

---

## Criterios de cierre de caso
Cerrar el caso cuando ocurra una de estas:
- ya hay suficiente evidencia útil,
- el rendimiento marginal de nuevas PRs baja,
- las nuevas tareas aportan más higiene que aprendizaje,
- el siguiente paso requiere una hipótesis distinta.

---

## Salidas útiles al cerrar un caso
Al final del caso debería existir, idealmente:
- AGENTS.md operativo,
- una retrospectiva breve,
- una comparación con otros casos si aplica,
- y aprendizajes convertidos en sistema reusable.

---

## Recomendación final
El valor no está en encadenar PRs indefinidamente, sino en:
1. abrir un caso con buena hipótesis,
2. ejecutar pocas PRs de buena señal,
3. cerrar el caso,
4. extraer método reusable,
5. pasar al siguiente experimento.
