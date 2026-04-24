# Roadmap AdSense e indexacion - abril 2026

Fecha inicio: 2026-04-13
Ultima actualizacion: 2026-04-24

## Objetivo
- Mantener el sitio en estado de calidad alta y estable para aumentar probabilidad de aprobacion AdSense.
- Reducir friccion de rastreo/indexacion con mejoras editoriales y SEO de bajo riesgo.

## Estado actual (24/04/2026)
- Fases 1, 2, 3 y 4 del roadmap original: completadas.
- Revision de AdSense: ya enviada.
- Ronda adicional de hardening ejecutada y validada:
  - Normalizacion de fechas visibles y dateModified en contenido blog.
  - Expansiones FAQPage en articulos con baja densidad de Q&A (objetivo 6 a 8).
  - Mejora de snippets SEO: titles y meta descriptions dentro de rango operativo.
  - Eliminacion de duplicidades de meta description detectadas.
  - CTAs in-content en 19/19 articulos de blog enlazando a herramientas relevantes.
  - Auditoria tecnica final predeploy: OK (sin mojibake, sin enlaces internos rotos, sin JSON-LD roto, sin desbalances HTML criticos).

## Criterio de listo para subir
- READY_FOR_DEPLOY=YES en auditoria tecnica local.
- Canonical/meta/title presentes y coherentes en HTML.
- 0 errores de parseo en scripts JSON-LD.
- 0 enlaces internos rotos detectados.

## Fase 5 (post-envio): contingencia y mejora continua
Objetivo: reaccionar con rapidez si persisten problemas de indexacion o rechazo AdSense.

### Bloque A - 7 a 14 dias
1. Reenviar sitemap en Search Console.
2. Solicitar inspeccion de 10 a 15 URLs clave reforzadas.
3. Medir cobertura en Search Console:
   - Descubierta, actualmente sin indexar
   - Rastreada, actualmente sin indexar
4. No tocar estructura global del sitio durante ventana de reevaluacion.

### Bloque B - si hay estancamiento de indexacion
1. Priorizar 10 URLs con mas impresiones y CTR bajo para ajustar title/meta.
2. Reforzar enlazado interno desde home, blog index y hubs tematicos.
3. Publicar 2 a 3 piezas de alto valor conectadas a herramientas clave.
4. Validar logs de cobertura cada 14 dias en SEGUIMIENTO-QUINCENAL-KPI.md.

### Bloque C - si AdSense rechaza por contenido de poco valor
1. Extraer motivo exacto del panel y mapearlo a URLs afectadas.
2. Reforzar URLs con:
   - ejemplo numerico completo
   - bloque de errores frecuentes
   - decision tree practico
   - fuente oficial por criterio normativo
3. Reauditar calidad tecnica completa antes de reenviar.

## KPI de control vigentes
- 0 enlaces internos rotos.
- 0 errores editoriales criticos detectados.
- 0 incidencias de encoding/mojibake en auditoria local.
- 100% de articulos blog con fecha consistente y CTA in-content.
- 100% de articulos blog con FAQPage y densidad Q&A util.

## Riesgos a evitar
- Cambios estructurales grandes sin evidencia en Search Console.
- Publicar volumen sin mejorar utilidad real por URL.
- Introducir cambios masivos de encoding sin validacion inmediata.
- Reenviar a AdSense sin iterar sobre motivo concreto de rechazo (si lo hubiera).

## Registro de avance resumido
- 2026-04-13: fases 1 a 4 completadas y revision de AdSense enviada.
- 2026-04-24: hardening extra completo (editorial + SEO + QA tecnico) y estado listo para deploy.
