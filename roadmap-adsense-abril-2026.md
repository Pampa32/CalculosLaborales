# Roadmap AdSense e indexacion

Fecha inicio: 2026-04-13
Ultima actualizacion: 2026-05-09

## Objetivo
- Mantener el sitio en estado de calidad alta y estable para aumentar probabilidad de aprobacion AdSense.
- Reducir friccion de rastreo/indexacion con mejoras editoriales y SEO de bajo riesgo.

## Estado actual (09/05/2026)
- Fases 1 a 4 del roadmap original: completadas.
- Hardening editorial + SEO + QA tecnico: completado.
- Revision de AdSense: enviada (estado "Preparando").
- Sesion 04/05/2026 completada:
  - Correccion de acentos en titles y meta descriptions de 45 paginas (commits 6c8fda6 y 44a21b4).
  - Actualizacion de lastmod en sitemap para 9 paginas modificadas (commit 2f28b8c).
  - Publicacion nuevo articulo cluster confianza/E-E-A-T: `blog/contrato-de-trabajo-que-revisar-antes-de-firmar.html` (commits 42ff3d9 y fb4f987).
  - Actualizacion de feed.xml, blog/index.html y sitemap.xml con el nuevo articulo.
- Sesion 09/05/2026 completada:
   - Analisis de cobertura en Search Console: 63 URLs indexadas, 17 URLs en "Descubierta, actualmente sin indexar" y 1 URL "Rastreada, actualmente sin indexar".
   - Micro-ronda de interlinking aplicada en home, index del blog y hub de bajas para empujar rastreo de URLs descubiertas.
   - Actualizacion de `lastmod` en sitemap para `/`, `/blog/` y `/bajas/` tras los cambios de interlinking.
   - Actualizacion de fecha visible de ultima revision en home a mayo 2026.
- KPI a 09/05/2026: 63 URLs indexadas, 7,07 mil impresiones (28d), 79 clics (28d), CTR 1,1 %, posicion media 26,3 (28d) / 15,6 (24h).
- Proyecto subido al host: pendiente (usuario lo hace manualmente).
- Sitemap reenviado a Search Console: pendiente (usuario lo hace tras subir).

## Criterio de listo para subir
- READY_FOR_DEPLOY=YES en auditoria tecnica local.
- Canonical/meta/title presentes y coherentes en HTML.
- 0 errores de parseo en scripts JSON-LD.
- 0 enlaces internos rotos detectados.
- `sitemap.xml` parseable y consistente con el arbol publicado.

## Fase 5 (post-envio): contingencia y mejora continua
Objetivo: reaccionar con rapidez si persisten problemas de indexacion o rechazo AdSense.

### Bloque A - 7 a 14 dias
1. Reenviar sitemap en Search Console.
2. Solicitar inspeccion de 8 URLs clave reforzadas tras la micro-ronda de interlinking.
3. Medir cobertura en Search Console:
   - Descubierta, actualmente sin indexar
   - Rastreada, actualmente sin indexar
4. No tocar estructura global del sitio durante ventana de reevaluacion.

### Bloque B - si hay estancamiento de indexacion
1. Priorizar 10 URLs con mas impresiones y CTR bajo para ajustar title/meta.
2. Reforzar enlazado interno desde home, blog index y hubs tematicos.
3. Publicar 2 a 3 piezas de alto valor conectadas a herramientas clave.
4. Validar logs de cobertura cada 14 dias en `SEGUIMIENTO-QUINCENAL-KPI.md`.

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
- 2026-04-24: hardening extra completo (editorial + SEO + QA tecnico).
- 2026-04-25: limpieza documental, sitemap legible/validado y estado final pre-subida a host.
- 2026-05-04: correccion de 45 acentos/titles, actualizacion lastmod sitemap, publicacion articulo confianza editorial, limpieza de documentos obsoletos.
- 2026-05-09: analisis de indexacion en Search Console, refuerzo de interlinking en `/`, `/blog/` y `/bajas/`, actualizacion de `lastmod` y predeploy validado sin errores.

---

## Plan B — Si no mejora la indexacion en 30 dias

Senal de alerta: en la revision del 19/05/2026, si las URLs indexadas no aumentan o la posicion media no baja de 12.

1. Identificar en Search Console las URLs en estado "Descubierta, actualmente sin indexar" o "Rastreada, actualmente sin indexar".
2. Revisar si tienen enlazado interno suficiente (minimo 3 enlaces internos entrantes).
3. Reforzar enlazado desde home e index del blog hacia las URLs afectadas.
4. Revisar si el contenido de esas URLs supera 600 palabras con valor real (no relleno).
5. Publicar 1 articulo nuevo por quincena conectado a las URLs sin indexar (refuerzo de cluster).
6. Solicitar inspeccion manual de las 5 URLs mas importantes desde Search Console.
7. Si persiste tras 60 dias: revisar estructura de enlaces internos de forma global.

## Plan C — Si AdSense rechaza (motivo: contenido de poco valor)

1. Anotar el motivo exacto del panel de AdSense y la fecha.
2. Identificar las URLs senaladas (si AdSense da ejemplos concretos).
3. Para cada URL afectada aplicar:
   - Ampliar con ejemplo numerico propio y completo.
   - Anadir bloque "Errores frecuentes" con al menos 3 casos reales.
   - Incluir fuente oficial citada (ET, SEPE, Seguridad Social) por cada criterio normativo.
   - Anadir un decision tree o flujo practico de "que hacer".
   - Revisar que el FAQ tenga minimo 5 preguntas con respuestas sustantivas.
4. Prioridad especial si no estan completadas:
   - `/guia/cuanto-se-cobra-el-primer-mes-de-paro.html` (ejemplo completo con fechas reales).
   - `/guia/como-calcular-base-reguladora-paro.html` (doble metodo + checklist de verificacion).
   - `/guia/como-se-pagan-las-horas-extra.html` (escenarios numericos por tipo de convenio).
5. Reauditar encoding y datos tecnicos antes de reenviar.
6. No reenviar revision hasta tener minimo 3 URLs mejoradas cerradas.
7. Esperar al menos 7 dias tras la subida antes de solicitar nueva revision.

## Plan D — Si AdSense rechaza (motivo: trafico insuficiente o politicas)

- **Trafico insuficiente**: no hay atajos. Mantener publicacion mensual y esperar consolidacion organica. Revisar CTR de snippets con datos reales de Search Console.
- **Politicas de Google**: leer el motivo exacto. Los mas frecuentes en sitios de este tipo son: datos personales mal gestionados (cookies/privacidad), contenido con apariencia de YMYL sin autoría clara, o exceso de publicitario sobre contenido util. Cada uno tiene solucion especifica.
- **Sitio en construccion o insuficiente**: asegurarse de que el pie de pagina tiene aviso legal, privacidad y sobre nosotros accesibles; y que la metodologia explica como se hacen los calculos.
