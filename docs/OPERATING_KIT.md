# OPERATING_KIT.md

## Objetivo
Reunir plantillas y checklists reutilizables para trabajar con Codex en repositorios reales de forma consistente.

---

## 1. Prompt base para una PR

### Plantilla
Objetivo:
[qué cambio se quiere]

Contexto:
- Repo: [nombre]
- Estado actual: [breve]
- Hipótesis: [si aplica]

Restricciones:
- Haz el cambio mínimo necesario.
- No expandas alcance.
- No introduzcas dependencias nuevas.
- No cambies contratos visibles.
- Mantén una sola intención por PR.

Qué debes hacer:
1. identificar la causa o hotspot,
2. elegir la opción más conservadora,
3. aplicar solo ese cambio,
4. ejecutar checks relevantes,
5. separar claramente fallos del entorno y efectos reales del cambio.

Done when:
- [criterio 1]
- [criterio 2]
- [criterio 3]

Output esperado:
1. objetivo entendido
2. plan breve
3. archivos o áreas tocadas
4. cambios realizados
5. comandos/checks ejecutados y resultado
6. riesgos o supuestos
7. siguiente paso recomendado

---

## 2. Prompt base para PR documental

### Plantilla
Objetivo:
Crear una PR documental pequeña para [marco / retrospectiva / comparación / cierre].

Restricciones:
- Toca solo docs/ o un archivo documental específico.
- No cambies código, tests ni setup.
- Mantén la PR pequeña y fácil de revisar.

Contenido esperado:
- [lista breve]

Done when:
- exista el archivo esperado,
- no haya cambios no relacionados,
- la PR siga siendo pequeña y documental.

---

## 3. Checklist de revisión humana

### Alcance
- ¿Tiene una sola intención?
- ¿El cambio es más pequeño que razonable?
- ¿Toca solo lo necesario?

### Diseño
- ¿La solución es conservadora?
- ¿Evita abrir frentes nuevos?
- ¿No mezcla objetivos distintos?

### Validación
- ¿Se ejecutaron checks relevantes?
- ¿Se separó fallo del entorno y fallo del cambio?
- ¿La validación es suficiente para el tamaño de la PR?

### Riesgo
- ¿Es reversible?
- ¿El diff es barato de revisar?
- ¿Hay efectos laterales no justificados?

### Decisión
- aprobar
- aprobar con observación
- no aprobar aún
- detener y reformular

---

## 4. Microevaluaciones reutilizables

### General
Aprobada tras revisión.

Microevaluación:
- alcance bien acotado
- cambio pequeño, útil y revisable
- validación suficiente para el tamaño de la tarea
- sin expansión innecesaria del alcance

### Cleanup local
Aprobada tras revisión.

Microevaluación:
- alcance bien acotado
- cleanup local pequeño, útil y reversible
- sin cambios funcionales observables
- validación suficiente para el tamaño de la tarea

### Cleanup multiarchivo
Aprobada tras revisión.

Microevaluación:
- alcance bien acotado
- cleanup multiarchivo real, pequeño y reversible
- reducción clara de duplicación o mejora de frontera local
- sin cambios funcionales observables
- validación suficiente para el tamaño de la tarea

### Blindaje
Aprobada tras revisión.

Microevaluación:
- alcance bien acotado
- blindaje pequeño y útil de la frontera tratada
- sin cambios en producción ni expansión del alcance
- validación suficiente para el tamaño de la tarea

### Entorno de tests
Aprobada tras revisión.

Microevaluación:
- alcance bien acotado
- mejora útil de la infraestructura mínima de validación
- checks directos ya funcionan de forma explícita
- sin expansión innecesaria hacia packaging o arquitectura

### Documentación / cierre
Aprobada tras revisión.

Microevaluación:
- alcance bien acotado
- documento breve, claro y útil
- consolida bien aprendizajes
- sin tocar código ni expandir el alcance

---

## 5. Tipos de PR y su uso

### Cleanup local
Usar cuando:
- hay una única pieza de ruido técnico,
- el cambio cabe en un diff mínimo,
- no hace falta tocar más de una zona.

### Cleanup multiarchivo
Usar cuando:
- hay una frontera local real entre 2 o más archivos,
- existe duplicación o responsabilidad compartida clara,
- el refactor sigue siendo pequeño.

### Blindaje
Usar cuando:
- una frontera recién extraída necesita tests,
- quieres cerrar la zona antes de abrir otra,
- el refactor ya está hecho y ahora toca estabilizar.

### Entorno de tests
Usar cuando:
- la validación del repo añade ruido constante,
- puedes corregirla con una solución pequeña,
- el beneficio afecta a todas las PRs posteriores.

### Retrospectiva
Usar cuando:
- se cierra una fase,
- ya hay suficiente señal,
- quieres consolidar aprendizajes antes de continuar.

---

## 6. Señales de buen rendimiento de Codex
- mantiene el alcance,
- elige la solución más conservadora razonable,
- no introduce cambios laterales,
- produce diffs pequeños y claros,
- valida lo relevante,
- distingue correctamente entre fallo del entorno y efecto del cambio.

---

## 7. Señales de deriva
- mezcla varias intenciones,
- refactoriza más de lo pedido,
- introduce complejidad innecesaria,
- arregla cosas "de paso",
- no distingue problemas del repo y problemas del cambio,
- genera PRs costosas de revisar,
- aporta más ruido que señal estructural.

---

## 8. Cuándo cerrar un experimento
Cerrar cuando:
- ya hay evidencia suficiente,
- nuevas PRs aportan poco,
- el rendimiento marginal baja,
- o la siguiente pregunta exige otra hipótesis.

No continuar por inercia.

---

## 9. Qué debe incluir una retrospectiva
- propósito del ciclo,
- resumen de PRs,
- qué funcionó bien,
- qué fricciones aparecieron,
- qué patrones conviene mantener,
- qué no quedó probado,
- siguiente paso recomendado.

---

## 10. Qué debe incluir una comparativa entre casos
- propósito de la comparación,
- resumen de cada repo,
- diferencias clave,
- aprendizajes comunes,
- límites observados,
- recomendación del siguiente experimento.
