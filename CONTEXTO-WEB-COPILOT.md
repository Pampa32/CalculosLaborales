# Contexto Web CalculosLaborales (para nuevas sesiones)

Fecha de inicio: 2026-04-13
Última actualización: 2026-05-19

## Contexto operativo
- Proyecto: sitio estático en español sobre cálculos laborales.
- Objetivo: monetización sostenible (AdSense + leads/afiliación), calidad editorial y técnica alta, crecimiento SEO progresivo.
- Roadmaps activos:
  - roadmap-adsense-abril-2026.md (calidad, indexación, contingencias AdSense)
  - roadmap-monetizacion-2026.md (estrategia dual: AdSense + monetización alternativa)
  - CHECKLIST-SEMANA-CTA-LEADS.md (medición semanal de conversión y leads)


## Reglas de trabajo activas
- Ejecutar cambios por fases, validando al final de cada bloque.
- Priorizar calidad editorial y técnica sobre cantidad.
- Medir impacto de cada cambio en SEO, AdSense y monetización alternativa.
- Mantener transparencia y aviso legal en todos los bloques comerciales.
- No hacer cambios estructurales masivos sin datos claros.
- Usar los checklists y roadmaps activos como referencia obligatoria.

## Checklist de arranque en cada sesión
1. Leer roadmap-adsense-abril-2026.md y roadmap-monetizacion-2026.md.
2. Leer este archivo (CONTEXTO-WEB-COPILOT.md).
3. Leer CHECKLIST-SEMANA-CTA-LEADS.md si hay cambios de conversión/monetización.
4. Confirmar estado git y cambios no comiteados.
5. Validar en producción:
   - /ads.txt, /robots.txt, /sitemap.xml
   - 2-3 URLs clave de contenido
6. Si hay cambios pendientes de subida: ejecutar QA predeploy (encoding, enlaces internos, JSON-LD, SEO mínimo).
7. Continuar desde el siguiente paso del roadmap o del último pedido del usuario.

## Próximos pasos recomendados
- Subir cambios al host y confirmar que ads.txt responde con 200.
- Reenviar sitemap y solicitar inspección de 8 URLs clave en Search Console.
- Mantener estabilidad técnica mientras dura la revisión de AdSense.
- Siguiente revisión quincenal de KPI: ver SEGUIMIENTO-QUINCENAL-KPI.md.
- Si hay rechazo de AdSense, consultar planes de contingencia en roadmap-adsense-abril-2026.md.
- Si no mejora la indexación, consultar Plan B en roadmap-adsense-abril-2026.md.

## Documentación operativa activa
- roadmap-adsense-abril-2026.md: roadmap, decisiones y contingencias AdSense.
- roadmap-monetizacion-2026.md: estrategia dual y fases de monetización.
- SEGUIMIENTO-QUINCENAL-KPI.md: plantilla de seguimiento SEO, AdSense y monetización.
- CHECKLIST-SEMANA-CTA-LEADS.md: checklist semanal de conversión/leads.

## Plantilla operativa
- Usar SEGUIMIENTO-QUINCENAL-KPI.md cada 14 días para métricas y decisiones.
- Usar CHECKLIST-SEMANA-CTA-LEADS.md para medir semanalmente la conversión y calidad de leads.
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
- Actualizacion 04/05/2026 (sesion activa):
  - Correccion de acentos en titles y meta descriptions de 45 paginas (2 commits).
  - Actualizacion de lastmod en sitemap para 9 paginas.
  - Publicacion nuevo articulo cluster E-E-A-T: `blog/contrato-de-trabajo-que-revisar-antes-de-firmar.html`.
  - Feed.xml, blog/index.html y sitemap.xml actualizados.
  - Eliminados documentos obsoletos: `PLAN-REMEDIACION-ADSENSE-2026-04-24.md` y `roadmap-contenido-mayo-2026.md`.
  - Estado AdSense: "Preparando" (en revision). Proyecto pendiente de subir al host.
- Actualizacion 09/05/2026 (sesion activa):
  - Revisada cobertura en Search Console: 63 URLs indexadas, 17 en "Descubierta, actualmente sin indexar" y 1 en "Rastreada, actualmente sin indexar".
  - Aplicada micro-ronda de interlinking en `index.html`, `blog/index.html` y `bajas/index.html` para reforzar rastreo de URLs descubiertas.
  - Actualizados `lastmod` de `/`, `/blog/` y `/bajas/` en `sitemap.xml`.
  - Actualizada la fecha visible de revision en home a mayo 2026.
  - QA predeploy final completado sin errores en los archivos tocados. Sitio listo para subir al host.
- Correccion de codificacion en produccion:
  - Se configuro UTF-8 por cabecera HTTP en .htaccess.
  - Verificado en vivo: content-type con charset UTF-8 y sin mojibake en URLs clave.

## Estado de produccion validado (ultimo check completo: 13/04/2026)
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
- Subir cambios al host y confirmar que ads.txt responde con 200.
- Reenviar sitemap y solicitar inspeccion de 8 URLs clave en Search Console.
- Mantener estabilidad tecnica mientras dura la revision de AdSense.
- Proxima revision quincenal de KPI: 18-19 de mayo de 2026.
- Si hay rechazo de AdSense, consultar Plan C o D en `roadmap-adsense-abril-2026.md`.
- Si no mejora la indexacion, consultar Plan B en `roadmap-adsense-abril-2026.md`.
- Articulos pendientes de refuerzo (si AdSense rechaza): `/guia/cuanto-se-cobra-el-primer-mes-de-paro.html`, `/guia/como-calcular-base-reguladora-paro.html`, `/guia/como-se-pagan-las-horas-extra.html`.

## Guion para la proxima revision (10-15 dias)
1. Confirmar que el deploy quedo bien en produccion: `/`, `/blog/`, `/bajas/`, `/sitemap.xml`, `/robots.txt`, `/ads.txt`.
2. Revisar en Search Console:
  - URLs indexadas
  - "Descubierta, actualmente sin indexar"
  - "Rastreada, actualmente sin indexar"
  - estado de las 8 URLs inspeccionadas manualmente
3. Comparar rendimiento 28 dias vs corte anterior:
  - impresiones
  - clics
  - CTR
  - posicion media
4. Tomar decision con este criterio:
  - si baja "Descubierta" y suben indexadas: mantener estabilidad
  - si indexacion plana: aplicar Plan B del roadmap
  - si hay rechazo AdSense: aplicar Plan C o D del roadmap segun motivo

## Documentacion operativa activa
- `roadmap-adsense-abril-2026.md`: roadmap, decisiones del sprint y planes de contingencia (B/C/D).
- `roadmap-monetizacion-2026.md`: roadmap dual de monetizacion (afiliacion/leads/activos propios en paralelo con AdSense).
- `SEGUIMIENTO-QUINCENAL-KPI.md`: plantilla de seguimiento cada 14 dias.

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

## Estado tecnico validado local (09/05/2026)
- Sin errores en `index.html`, `blog/index.html`, `bajas/index.html` y `sitemap.xml` tras la micro-ronda de interlinking.
- `lastmod` sincronizado en sitemap para `/`, `/blog/` y `/bajas/`.
- Home actualizada con fecha visible de revision en mayo 2026.
- Predeploy listo para subida a host.

## Plantilla operativa
- Usar SEGUIMIENTO-QUINCENAL-KPI.md en cada revision de 14 dias para registrar metricas, decisiones y acciones.
