# Roadmap AdSense e indexacion

Fecha inicio: 2026-04-13
Ultima actualizacion: 2026-05-09

## Objetivo
- Mantener el sitio en estado de calidad alta y estable para aumentar probabilidad de aprobacion AdSense.
- Reducir friccion de rastreo/indexacion con mejoras editoriales y SEO de bajo riesgo.
- Coordinar este plan con `roadmap-monetizacion-2026.md` para no depender de un unico canal de ingresos.

## Situacion operativa resumida
- La siguiente accion inmediata fuera del repo es subir el sitio al host.
- Despues de publicar: reenviar sitemap y solicitar inspeccion manual de 8 URLs prioritarias.
- Hasta la siguiente revision no conviene tocar estructura global, plantillas ni lanzar cambios masivos.

## Estado actual (09/05/2026)
  - Correccion de acentos en titles y meta descriptions de 45 paginas (commits 6c8fda6 y 44a21b4).
  - Actualizacion de lastmod en sitemap para 9 paginas modificadas (commit 2f28b8c).
  - Publicacion nuevo articulo cluster confianza/E-E-A-T: `blog/contrato-de-trabajo-que-revisar-antes-de-firmar.html` (commits 42ff3d9 y fb4f987).
  - Actualizacion de feed.xml, blog/index.html y sitemap.xml con el nuevo articulo.
   - Analisis de cobertura en Search Console: 63 URLs indexadas, 17 URLs en "Descubierta, actualmente sin indexar" y 1 URL "Rastreada, actualmente sin indexar".
   - Micro-ronda de interlinking aplicada en home, index del blog y hub de bajas para empujar rastreo de URLs descubiertas.
   - Actualizacion de `lastmod` en sitemap para `/`, `/blog/` y `/bajas/` tras los cambios de interlinking.
   - Actualizacion de fecha visible de ultima revision en home a mayo 2026.
## Estado actual (19/05/2026)
- Fases 1 a 4 completadas.
- Hardening editorial + SEO + QA técnico: completado.
- Revisión de AdSense: enviada (estado "Preparando").
- Cambios de monetización y CTA/leads integrados (ver roadmap-monetizacion-2026.md y CHECKLIST-SEMANA-CTA-LEADS.md).

## Checklist inmediata tras subir al host
1. Confirmar que `/`, `/blog/`, `/bajas/`, `/sitemap.xml`, `/robots.txt` y `/ads.txt` responden bien en producción.
2. Reenviar `sitemap.xml` en Search Console.
3. Solicitar inspección manual de estas 8 URLs:
   - `/blog/como-saber-si-tienes-derecho-a-paro-2026.html`
   - `/blog/que-documentos-necesitas-para-pedir-el-paro-sin-errores.html`
   - `/blog/motivos-por-los-que-el-sepe-puede-denegarte-el-paro.html`
   - `/blog/como-revisar-una-nomina-paso-a-paso-sin-que-te-enganen.html`
   - `/blog/como-pasar-de-sueldo-bruto-anual-a-neto-mensual-con-ejemplos-reales.html`
   - `/blog/por-que-te-retienen-tanto-irpf-en-la-nomina.html`
   - `/blog/diferencia-entre-finiquito-e-indemnizacion-con-ejemplos-reales.html`
   - `/blog/cuanto-paga-un-autonomo-seguridad-social-2026.html`
4. No tocar arquitectura, menús ni estructura de enlaces durante 7-10 días.
## Checklist inmediata tras subir al host
1. Confirmar que `/`, `/blog/`, `/bajas/`, `/sitemap.xml`, `/robots.txt` y `/ads.txt` responden bien en produccion.
2. Reenviar `sitemap.xml` en Search Console.
3. Solicitar inspeccion manual de estas 8 URLs:
   - `/blog/como-saber-si-tienes-derecho-a-paro-2026.html`
   - `/blog/que-documentos-necesitas-para-pedir-el-paro-sin-errores.html`
   - `/blog/motivos-por-los-que-el-sepe-puede-denegarte-el-paro.html`
   - `/blog/como-revisar-una-nomina-paso-a-paso-sin-que-te-enganen.html`
   - `/blog/como-pasar-de-sueldo-bruto-anual-a-neto-mensual-con-ejemplos-reales.html`
   - `/blog/por-que-te-retienen-tanto-irpf-en-la-nomina.html`
   - `/blog/diferencia-entre-finiquito-e-indemnizacion-con-ejemplos-reales.html`
   - `/blog/cuanto-paga-un-autonomo-seguridad-social-2026.html`
4. No tocar arquitectura, menus ni estructura de enlaces durante 7-10 dias.

## Proxima revision programada
- Ventana objetivo: 19/05/2026 a 24/05/2026.
- Objetivo: medir si la micro-ronda de interlinking y la reindexacion manual han reducido friccion de rastreo.

### Que revisar en Search Console
1. URLs validas indexadas.
2. URLs en "Descubierta, actualmente sin indexar".
3. URLs en "Rastreada, actualmente sin indexar".
4. Impresiones, clics, CTR y posicion media en 28 dias.
5. Estado de las 8 URLs inspeccionadas manualmente.
6. Si persisten los errores/redirecciones ya vistos en cobertura.

### Senales de exito
- Las indexadas suben por encima de 63.
- "Descubierta, actualmente sin indexar" baja de 17.
- Alguna de las 8 URLs reforzadas pasa a indexada o al menos muestra ultimo rastreo.
- La posicion media de 28 dias mejora o se mantiene mientras suben impresiones.

### Senales de alerta
- Las indexadas siguen planas.
- "Descubierta" no baja o incluso sube.
- Ninguna de las 8 URLs reforzadas muestra avance de rastreo.
- El CTR cae con mas impresiones en URLs ya visibles.

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
3. Publicar 1 pieza de alto valor conectada a herramientas clave, no volumen masivo.
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

## Plan B — Si la revision de 19/05 a 24/05 sale plana
1. Identificar que URLs siguen en "Descubierta" o "Rastreada" sin indexar.
2. Revisar si tienen minimo 3 enlaces internos entrantes y al menos 600 palabras utiles.
3. Reforzar enlazado desde home, index del blog y piezas que ya reciben impresiones.
4. Ajustar title/meta solo en URLs con muchas impresiones y CTR claramente bajo.
5. Publicar 1 articulo nuevo conectado al cluster que peor avance.
6. Solicitar inspeccion manual solo de las 5 URLs mas importantes que sigan atascadas.
7. Si tras otra quincena no mejora: revisar estructura interna de enlaces de forma mas amplia.

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
