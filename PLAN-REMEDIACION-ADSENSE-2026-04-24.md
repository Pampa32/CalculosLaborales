# Plan de remediación AdSense — "Contenido de poco valor"

Fecha: **24 de abril de 2026**
Ventana estimada para nueva solicitud de revisión: **a partir del 28 de abril de 2026**.
Ultima revision de estado: **25 de abril de 2026**.

## Objetivo
Subir el valor percibido de contenido en URLs estratégicas con mejoras editoriales **concretas, originales y útiles** para usuario real.

## Top 10 URLs priorizadas (primera oleada)

| Prioridad | URL | Mejora obligatoria (minimo) | Estado |
|---|---|---|---|
| 1 | `/guia/como-calcular-indemnizacion-por-despido.html` | 3 casos reales + comparativa + errores frecuentes | Completado |
| 2 | `/guia/derechos-del-trabajador-2026.html` | Checklist accionable + mini flujos + documentos por tramite | Completado |
| 3 | `/guia/reanudar-paro-despues-de-trabajar.html` | Decision reanudar vs nuevo derecho + supuestos reales + contexto SEPE | Completado |
| 4 | `/guia/como-solicitar-el-paro-paso-a-paso.html` | Errores frecuentes + tiempos + bloque de denegacion | Completado |
| 5 | `/guia/gastos-deducibles-autonomos-iva-irpf.html` | Matriz si/no/depende + prueba documental + ejemplos | Completado |
| 6 | `/blog/teletrabajo-derechos-2026.html` | Casos de conflicto + plantillas de comunicacion | Completado |
| 7 | `/guia/como-leer-una-nomina.html` | Nomina comentada + checklist descargable | Completado |
| 8 | `/guia/como-se-pagan-las-horas-extra.html` | Simulador/casos por escenario + bloque practico de reclamacion | Parcial |
| 9 | `/guia/cuanto-se-cobra-el-primer-mes-de-paro.html` | Ejemplo por fechas + primer pago parcial + retencion | Pendiente |
| 10 | `/guia/como-calcular-base-reguladora-paro.html` | Metodo manual + metodo rapido + verificacion | Pendiente |

## Siguiente bloque operativo (antes de nueva solicitud)
1. Cerrar prioridad 9 con ejemplo completo y calendario real.
2. Cerrar prioridad 10 con doble metodo de calculo y checklist de validacion.
3. Completar prioridad 8 con escenarios numericos minimos por convenio/tipo.

## Criterios editoriales mínimos por URL (para pasar revisión)
1. **Originalidad verificable**: incluir ejemplos propios numéricos y/o tablas de elaboración propia.
2. **Valor accionable**: cada página debe resolver "qué hago ahora" con pasos concretos.
3. **E-E-A-T visible**: fecha de revisión, fuente oficial citada y limitaciones del cálculo.
4. **No thin affiliate pattern**: evitar texto de relleno; cada bloque debe aportar decisión, cálculo o documento.
5. **Enlazado útil**: mínimo 6 enlaces internos relevantes (no solo menú global).

## Regla de cierre
- No solicitar nueva revision hasta que 9 y 10 esten en estado **Completado** y 8 pase a **Completado**.
- Tras esos cierres, ejecutar auditoria tecnica completa y revisar snippets de URLs con mas impresiones y CTR bajo.

## Gate de publicación
Antes de reenviar revisión en AdSense:

```bash
python scripts/seo_guard.py
python scripts/adsense_readiness.py
python scripts/predeploy_audit.py
python scripts/content_value_audit.py
```

Si todo está OK y ya pasó la fecha de bloqueo, solicitar revisión de nuevo.
