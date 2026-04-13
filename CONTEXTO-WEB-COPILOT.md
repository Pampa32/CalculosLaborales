# Contexto Web CalculosLaborales (para nuevas sesiones)

Fecha de inicio: 2026-04-13
Ultima actualizacion: 2026-04-13

## Resumen rapido
- Proyecto: sitio estatico en espanol sobre calculos laborales.
- Objetivo principal: mejorar calidad editorial y tecnica para aprobar AdSense.
- Roadmap activo: roadmap-adsense-abril-2026.md.
- Estado actual: fases 1, 2, 3 y 4 tecnicas completadas; revision de AdSense ya enviada.

## Lo que ya se hizo
- Fase 1: saneamiento critico de contenido y enlaces.
- Fase 2: refuerzo de 10 URLs prioritarias con mas profundidad (casos, checklist, fuentes).
- Fase 3: consistencia global editorial y enlace a metodologia.
- Fase 4 tecnica: validaciones previas (ads.txt, robots, sitemap, enlaces internos, viewport).
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

## Checklist de arranque en una nueva conversacion
1. Leer roadmap-adsense-abril-2026.md.
2. Leer este archivo (CONTEXTO-WEB-COPILOT.md).
3. Confirmar estado git y posibles cambios no comiteados.
4. Validar rapidamente en produccion:
   - /ads.txt
   - /robots.txt
   - /sitemap.xml
   - 2-3 URLs clave de contenido
5. Continuar desde el siguiente paso del roadmap o desde el ultimo pedido del usuario.

## Proximos pasos recomendados
- Esperar respuesta de AdSense.
- Mantener estabilidad tecnica mientras dura la revision.
- Si hay rechazo, preparar iteracion con hallazgos concretos del panel.
