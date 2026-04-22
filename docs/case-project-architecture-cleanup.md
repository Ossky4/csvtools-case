# Case Project — Cleanup de arquitectura en csvtools

## Objetivo
Usar este repositorio como caso de prueba para cleanup de arquitectura pequeño, reversible y de bajo riesgo con Codex.

El objetivo no es rediseñar el sistema ni añadir features nuevas, sino identificar y ejecutar mejoras pequeñas de estructura que:
- reduzcan duplicación,
- aclaren fronteras entre módulos,
- mejoren legibilidad,
- y preserven el comportamiento observable.

---

## Contexto mínimo del repositorio

### Naturaleza del proyecto
`csvtools` es un conjunto de utilidades de línea de comandos para manipular datos tabulares CSV/TSV.

### Estructura visible relevante
- `.github/workflows/`
- `csvtools/`
- `test/`
- `tests/`
- `README.md`
- `requirements.txt`
- `setup.py`

### Señales relevantes para este Case Project
- El README lista muchas utilidades CLI distintas.
- Existen dos carpetas de pruebas (`test/` y `tests/`), lo que sugiere una frontera potencialmente interesante de entender antes de refactorizar.
- El repositorio tiene suficiente superficie para cleanup pequeño sin necesidad de cambios amplios.

---

## Alcance de este Case Project

### Sí entra en alcance
- validaciones duplicadas o mal ubicadas,
- helpers pequeños repetidos,
- mezcla local de lógica pura con IO/CLI,
- extracción mínima de una responsabilidad clara,
- reducción de acoplamiento ligero entre módulos,
- cleanup multiarchivo pequeño y revisable.

### No entra en alcance
- rediseño general de arquitectura,
- cambios de contrato CLI,
- renombrados masivos,
- migraciones amplias,
- features nuevas,
- cambios de packaging o despliegue,
- consolidación grande de toda la estrategia de tests.

---

## Reglas para las primeras PRs
- una sola intención por PR,
- cleanup pequeño y reversible,
- sin cambiar comportamiento observable,
- sin introducir dependencias nuevas,
- sin expandir alcance por iniciativa propia,
- con validación mínima y tests relevantes.

---

## Mapa inicial de hotspots admisibles

### Hotspot 1 — Duplicación de parsing o validación en utilidades CLI
El README sugiere una familia amplia de comandos con comportamiento parecido. Es plausible que existan validaciones o parsing repetidos entre herramientas similares.

**Tipo de cambio permitido:**
extraer o centralizar una validación o helper pequeño, sin cambiar interfaz visible.

---

### Hotspot 2 — Mezcla de lógica de transformación con lectura/escritura
En un repositorio de utilidades CSV, es probable que algunas herramientas mezclen:
- lectura de entrada,
- transformación de filas/columnas,
- y salida,
dentro del mismo flujo.

**Tipo de cambio permitido:**
separar una pieza de lógica pura de una capa de IO en un punto muy localizado.

---

### Hotspot 3 — Frontera poco clara entre `test/` y `tests/`
La coexistencia de ambas carpetas sugiere una posible deuda histórica o una convención no explícita.

**Tipo de cambio permitido:**
primero documentar o entender la diferencia; no consolidar ni mover tests todavía sin una razón clara.

---

### Hotspot 4 — Helpers pequeños incrustados en scripts o módulos principales
En un set amplio de herramientas CLI, es plausible que existan helpers locales que podrían vivir en un módulo compartido pequeño.

**Tipo de cambio permitido:**
mover un helper concreto y reutilizable a una ubicación más adecuada, con diff pequeño.

---

### Hotspot 5 — Acoplamiento ligero evitable entre módulos cercanos
Puede haber imports o dependencias pequeñas que hagan más difícil revisar o reutilizar lógica común.

**Tipo de cambio permitido:**
reducir una dependencia concreta si el cambio sigue siendo local, reversible y fácil de validar.

---

## Criterio de admisibilidad para futuras PRs
Una PR futura solo será admisible si cumple todo esto:
1. se puede describir en una frase,
2. tiene una sola intención clara,
3. cabe en una PR pequeña,
4. preserva comportamiento observable,
5. su validación posterior es barata.

---

## Secuencia recomendada del Case Project

### PR1
Mapa mínimo de arquitectura y hotspots admisibles.

### PR2
Cleanup local pequeño en una sola zona.

### PR3
Cleanup multiarchivo real, todavía pequeño y reversible.

### PR4
Blindaje con tests o ajuste de cobertura en la zona tocada.

### PR5
Retrospectiva del caso y comparación con el experimento anterior.

---

## Resultado esperado
Si el caso sale bien, deberíamos poder concluir que Codex puede ejecutar cleanup arquitectónico pequeño en un repositorio más real que el sandbox inicial, manteniendo:
- alcance acotado,
- PRs revisables,
- validación suficiente,
- y bajo riesgo de regresión.

Output esperado:
1. objetivo entendido,
2. plan breve,
3. archivos o áreas tocadas,
4. cambios realizados,
5. comandos/checks ejecutados y resultado,
6. riesgos o supuestos,
7. siguiente paso recomendado.
