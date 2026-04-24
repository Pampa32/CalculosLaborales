# Contexto Web CalculosLaborales (para nuevas sesiones)

Fecha de inicio: 2026-04-13
Ultima actualizacion: 2026-04-24

## Resumen rapido
- Proyecto: sitio estatico en espanol sobre calculos laborales.
- Objetivo de negocio final: generar ingresos pasivos de forma sostenible mediante publicidad de AdSense.
- Objetivo operativo actual: mantener calidad editorial y tecnica alta para facilitar aprobacion AdSense y consolidar indexacion.
- Roadmap activo: roadmap-adsense-abril-2026.md.
- Estado actual: fases 1 a 4 completadas + ronda adicional de hardening editorial/SEO/QA cerrada; revision de AdSense ya enviada.
- Contexto temporal: web publicada hace aproximadamente 1 mes y medio; indexacion aun parcial.

## Lo que ya se hizo
- Fase 1: saneamiento critico de contenido y enlaces.
- Fase 2: refuerzo de 10 URLs prioritarias con mas profundidad (casos, checklist, fuentes).
- Fase 3: consistencia global editorial y enlace a metodologia.
- Fase 4 tecnica: validaciones previas (ads.txt, robots, sitemap, enlaces internos, viewport).
- Ronda adicional 24/04/2026:
  - Normalizacion de fechas visibles y dateModified en contenido blog.
  - Expansion de FAQPage en articulos con baja densidad de preguntas.
  - Hardening de titles y meta descriptions (longitud, duplicados, coherencia).
  - Insercion de CTA in-content en 19/19 articulos de blog.
  - Correccion JSON-LD puntual en tools/finiquito.html.
  - Auditoria tecnica final sin hallazgos bloqueantes (ready for deploy).
- Correccion de codificacion en produccion:
  - Se configuro UTF-8 por cabecera HTTP en .htaccess.
  - Verificado en vivo: content-type con charset UTF-8 y sin mojibake en URLs clave.

## Estado de produccion validado (13/04/2026)
- Home: 200 OK, UTF-8, sin mojibake.
- legal/metodologia-calculos.html: 200 OK, UTF-8, sin mojibake.
- blog/como-rellenar-el-modelo-145-paso-a-paso.html: 200 OK, UTF-8, sin mojibake.
- blog/incapacidad-permanente-total-cuanto-se-cobra-como-tramitar.html: 200 OK, UTF-8, sin mojibake.
- guia/declarar-irpf-2026.html: 200 OK, UTF-8, sin mojibake.
- tools/calculadora-paro.html: 200 OK, UTF-8, sin mojibake.
- robots.txt: correcto con sitemap.
- ads.txt: correcto y accesible.

## Reglas de trabajo acordadas con el usuario
- Ejecutar cambios directamente por fases, con validacion al final.
- Priorizar calidad real frente a cantidad de contenido.
- Evitar errores de codificacion en reemplazos masivos.
- No abrir lineas nuevas fuera de roadmap mientras haya tareas abiertas del sprint.
- Mantener foco constante en crecimiento progresivo (indexacion + calidad + monetizacion), evitando cambios impulsivos que rompan estabilidad.
- Medir cada mejora por impacto en aprobacion de AdSense y salud SEO (rastreo/indexacion/cobertura).
- Antes de publicar: ejecutar auditoria predeploy completa y corregir bloqueantes.

## Checklist de arranque en una nueva conversacion
1. Leer roadmap-adsense-abril-2026.md.
2. Leer este archivo (CONTEXTO-WEB-COPILOT.md).
3. Confirmar estado git y posibles cambios no comiteados.
4. Validar rapidamente en produccion:
   - /ads.txt
   - /robots.txt
   - /sitemap.xml
   - 2-3 URLs clave de contenido
5. Si hay cambios pendientes de subida: ejecutar QA predeploy (encoding, enlaces internos, JSON-LD, SEO minimo).
6. Continuar desde el siguiente paso del roadmap o desde el ultimo pedido del usuario.

## Proximos pasos recomendados
- Publicar en host el estado actual validado.
- Reenviar sitemap y solicitar inspeccion de 10-15 URLs clave en Search Console.
- Mantener estabilidad tecnica mientras dura la revision.
- Si hay rechazo de AdSense, iterar con el motivo exacto del panel.
- Seguir mejora continua quincenal (contenido util + enlazado interno + CTR snippets).

## Proyeccion de seguimiento (30/60/90 dias)
- 30 dias:
  - Objetivo: consolidar rastreo e indexacion.
  - Senal positiva: suben URLs validas indexadas y bajan "descubierta/rastreada sin indexar".
  - Senal de riesgo: indexacion plana durante varias semanas.
- 60 dias:
  - Objetivo: mejorar visibilidad organica estable.
  - Senal positiva: crecimiento sostenido de impresiones y mejora de posicion media en URLs clave.
  - Senal de riesgo: impresiones sin tendencia clara.
- 90 dias:
  - Objetivo: convertir visibilidad en trafico mas estable.
  - Senal positiva: mejora de CTR en queries con muchas impresiones.
  - Senal de riesgo: CTR estancado pese a mas impresiones.

## Criterio de decision (iterativo)
- No aplicar cambios estructurales grandes sin datos.
- Revisar cada 2 semanas Search Console (indexacion, impresiones, CTR, posicion media).
- Priorizar mejoras de bajo riesgo y alto impacto:
  - snippets (title/meta) en URLs con impresiones altas y CTR bajo,
  - refuerzo de enlazado interno hacia URLs objetivo,
  - actualizacion de contenido con ejemplos/fuentes cuando haya estancamiento.

## Estado tecnico validado local (24/04/2026)
- READY_FOR_DEPLOY=YES.
- Sin mojibake detectado.
- Sin enlaces internos rotos detectados.
- Sin errores de parseo JSON-LD detectados.
- Sin faltantes de title/meta/canonical en HTML auditado.

## Plantilla operativa
- Usar SEGUIMIENTO-QUINCENAL-KPI.md en cada revision de 14 dias para registrar metricas, decisiones y acciones.
