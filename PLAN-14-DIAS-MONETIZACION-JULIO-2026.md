# Plan operativo 14 dias - Monetizacion principal (julio 2026)

Fecha de inicio sugerida: 06/07/2026  
Fecha de corte: 19/07/2026

## Objetivo del sprint
Convertir trafico organico en ingresos mediante leads y servicio orientativo, manteniendo AdSense en paralelo como canal secundario.

## Regla de foco
- No tocar arquitectura global.
- Ejecutar solo cambios en paginas con intencion alta.
- Medir semanalmente y decidir por datos.

## URLs a tocar primero (orden de prioridad)
1. /desempleo/cuanto-se-cobra-de-paro.html
2. /tools/sueldo-neto.html
3. /tools/finiquito.html
4. /blog/por-que-te-retienen-tanto-irpf-en-la-nomina.html
5. /guia/cuando-se-cobra-el-paro-tras-solicitarlo.html
6. /tools/duracion-paro.html
7. /tools/calculadora-dias-cotizados.html
8. /tools/calculadora-antiguedad-laboral.html

## Oferta principal del sprint
Revision orientativa personalizada (laboral/fiscal) con respuesta en 24-48h.

Propuesta de precio inicial:
- Entrada: 19-29 EUR (revision exprés)
- Escalado: 49-79 EUR (revision completa con recomendaciones)

## CTA exacto por tipo de pagina

### A. Paginas de calculadora (tools)
CTA principal (boton):
"Quiero una revision orientativa de mi caso (24-48h)"

CTA secundario (texto):
"Prefiero empezar con checklist gratis y ejemplos reales"

Microcopy de confianza:
"Respuesta personalizada, lenguaje claro y enfoque practico. No sustituye asesoria juridica formal."

### B. Guias y articulos informativos
CTA principal (boton):
"Enviar mi caso para revision orientativa"

CTA secundario (texto):
"Ver checklist para evitar errores frecuentes"

Microcopy de confianza:
"Te indicamos pasos, documentos y errores comunes segun tu situacion."

## Ubicacion recomendada del bloque CTA
1. Primer bloque: despues de la primera explicacion util (20-30% del contenido).
2. Segundo bloque: antes de FAQ o seccion final.
3. Nunca usar popups intrusivos.

## Instrumentacion minima (eventos)

Eventos GA4 recomendados:
1. cta_primary_click
2. cta_secondary_click
3. lead_form_start
4. lead_form_submit
5. mailto_click

Parametros recomendados por evento:
- page_path
- page_type (tool, guia, blog)
- cta_position (mid, end)
- cta_variant (A, B)
- cluster (paro, nomina, finiquito, irpf)

## Umbrales de decision (semana 1 y semana 2)

KPI por URL (minimo 200 sesiones para decidir con confianza):
1. CTR CTA principal = cta_primary_click / sesiones URL
2. CVR lead = lead_form_submit / sesiones URL
3. Ratio lead sobre clic = lead_form_submit / cta_primary_click

Semaforo operativo:
- Verde:
  - CTR CTA principal >= 2.0%
  - CVR lead >= 0.8%
  - Ratio lead sobre clic >= 20%
- Amarillo:
  - CTR entre 1.0% y 1.9%
  - CVR entre 0.3% y 0.79%
  - Ratio lead sobre clic entre 10% y 19%
- Rojo:
  - CTR < 1.0%
  - CVR < 0.3%
  - Ratio lead sobre clic < 10%

Accion por semaforo:
1. Verde: mantener copy y escalar a 3 URLs extra.
2. Amarillo: test A/B de titular CTA y posicion del bloque.
3. Rojo: rehacer propuesta de valor y simplificar friccion del contacto.

## Plan de ejecucion por dias

### Dias 1-3
1. Implementar CTA y microcopy en las 4 URLs top:
   - /desempleo/cuanto-se-cobra-de-paro.html
   - /tools/sueldo-neto.html
   - /tools/finiquito.html
   - /blog/por-que-te-retienen-tanto-irpf-en-la-nomina.html
2. Activar eventos GA4 minimos en esos bloques.
3. Verificar que los eventos llegan en tiempo real.

### Dias 4-7
1. Extender CTA y eventos a 4 URLs siguientes:
   - /guia/cuando-se-cobra-el-paro-tras-solicitarlo.html
   - /tools/duracion-paro.html
   - /tools/calculadora-dias-cotizados.html
   - /tools/calculadora-antiguedad-laboral.html
2. Revisar calidad UX movil y desktop.
3. Primera lectura de CTR CTA por URL.

### Dias 8-10
1. Ajuste de copy en URLs en amarillo/rojo.
2. Test A/B simple en 2 URLs:
   - Variante A: enfoque tiempo (24-48h).
   - Variante B: enfoque ahorro de errores y dinero.
3. Mantener SEO estable sin cambios estructurales.

### Dias 11-14
1. Cierre de datos por URL y cluster.
2. Decision de escalado:
   - Si 3 o mas URLs estan en verde: escalar modelo a 6-10 URLs adicionales.
   - Si menos de 3 estan en verde: refinar oferta y friccion de contacto antes de escalar.
3. Definir siguiente sprint de 14 dias segun resultados.

## Registro semanal sugerido
Registrar en cada URL:
1. Sesiones.
2. cta_primary_click.
3. cta_secondary_click.
4. lead_form_start.
5. lead_form_submit.
6. Observaciones cualitativas (dudas frecuentes, fricciones).

## Criterio de exito del sprint (19/07/2026)
1. Al menos 3 URLs en verde.
2. Al menos 1 cluster con señal de conversion estable.
3. Evidencia para fijar canal principal de monetizacion (leads/servicio), sin depender de aprobacion AdSense.

## Nota sobre AdSense
Mantener AdSense en paralelo sin detener este sprint. Si aparece nuevo rechazo por contenido de poco valor, no pausar la ejecucion comercial: solo mantener mantenimiento tecnico y editorial incremental.
