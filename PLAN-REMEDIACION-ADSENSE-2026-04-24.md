# Plan de remediación AdSense — "Contenido de poco valor"

Fecha: **24 de abril de 2026**
Ventana estimada para nueva solicitud de revisión: **a partir del 28 de abril de 2026**.

## Objetivo
Subir el valor percibido de contenido en URLs estratégicas con mejoras editoriales **concretas, originales y útiles** para usuario real.

## Top 10 URLs priorizadas (primera oleada)

| Prioridad | URL | Señal actual | Mejora obligatoria (mínimo) |
|---|---|---|---|
| 1 | `/guia/como-calcular-indemnizacion-por-despido.html` | Cobertura corta para tema YMYL | Añadir 3 casos reales completos (procedente/improcedente/nulo) con cifras, tabla comparativa por antigüedad y sección "errores frecuentes". |
| 2 | `/guia/derechos-del-trabajador-2026.html` | Página amplia pero genérica | Reescribir en formato checklist accionable + mini flujos (despido, impago, baja) + documentos necesarios por trámite. |
| 3 | `/guia/reanudar-paro-despues-de-trabajar.html` | Puede solaparse con otras del paro | Añadir diagrama de decisiones (reanudar vs nueva prestación), 5 supuestos reales y enlaces a SEPE con contexto. |
| 4 | `/guia/como-solicitar-el-paro-paso-a-paso.html` | Riesgo de contenido "how-to" estándar | Añadir captura/explicación de errores frecuentes de solicitud, tiempos reales, y bloque "si te lo deniegan" con pasos. |
| 5 | `/guia/gastos-deducibles-autonomos-iva-irpf.html` | Tema competitivo, requiere profundidad | Separar por gasto (sí/no/depende), prueba documental exigible y ejemplos de deducción parcial. |
| 6 | `/blog/teletrabajo-derechos-2026.html` | Artículo informativo de baja profundidad | Añadir casos de conflicto (equipos, gastos, horario), plantillas de comunicación y resolución práctica paso a paso. |
| 7 | `/guia/como-leer-una-nomina.html` | Útil pero mejorable en valor diferencial | Incluir nómina comentada línea a línea (ejemplo real anonimizado) + checklist descargable. |
| 8 | `/guia/como-se-pagan-las-horas-extra.html` | Tema potencialmente repetido | Añadir calculadora embebida o simulador simple y 4 escenarios (normal/festivo/nocturno/convenio). |
| 9 | `/guia/cuanto-se-cobra-el-primer-mes-de-paro.html` | Intención muy concreta | Añadir explicación por fechas de alta/baja, primer pago parcial, retención y ejemplo con calendario real. |
| 10 | `/guia/como-calcular-base-reguladora-paro.html` | Puede parecer puente hacia calculadora | Añadir 2 métodos de cálculo (manual y rápido), plantilla de hoja de cálculo y verificación de inconsistencias. |

## Criterios editoriales mínimos por URL (para pasar revisión)
1. **Originalidad verificable**: incluir ejemplos propios numéricos y/o tablas de elaboración propia.
2. **Valor accionable**: cada página debe resolver "qué hago ahora" con pasos concretos.
3. **E-E-A-T visible**: fecha de revisión, fuente oficial citada y limitaciones del cálculo.
4. **No thin affiliate pattern**: evitar texto de relleno; cada bloque debe aportar decisión, cálculo o documento.
5. **Enlazado útil**: mínimo 6 enlaces internos relevantes (no solo menú global).

## Plan de ejecución (72 horas)
- **Día 1**: actualizar prioridades 1–3.
- **Día 2**: actualizar prioridades 4–7.
- **Día 3**: actualizar prioridades 8–10 + revisión transversal de títulos/H2/FAQ.

## Gate de publicación
Antes de reenviar revisión en AdSense:

```bash
python scripts/seo_guard.py
python scripts/adsense_readiness.py
python scripts/predeploy_audit.py
python scripts/content_value_audit.py
```

Si todo está OK y ya pasó la fecha de bloqueo, solicitar revisión de nuevo.
