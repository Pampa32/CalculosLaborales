# CalculosLaborales.es

> 📊 Herramientas interactivas y guías prácticas para entender cálculos laborales, impuestos y prestaciones sociales en España

[![GitHub](https://img.shields.io/badge/repo-CalculosLaborales-blue?logo=github)](https://github.com/Pampa32/CalculosLaborales)
[![License](https://img.shields.io/badge/license-MIT-green)](#licencia)
[![Static Site](https://img.shields.io/badge/site-static%20HTML-orange)](#tecnologías)

## 🎯 Descripción

CalculosLaborales es un sitio web especializado en **cálculos y consultas laborales en España**. Ofrece:

- **Calculadoras interactivas** para nóminas, finiquitos, indemnizaciones, paro, impuestos
- **Guías prácticas** sobre despidos, bajas, jubilación, teletrabajo, cambios 2026
- **Información estructurada** sobre derechos y obligaciones laborales
- **Contenido de referencia** actualizado con normativa vigente

### Audiencia Objetivo
- Trabajadores por cuenta ajena
- Autónomos
- Empresarios
- Profesionales de RRHH

---

## ✨ Características Principales

### 📱 Calculadoras Incluidas
- **Calculadora de Finiquito**: calcula liquidación completa de trabajador
- **Calculadora IRPF Nómina**: simula impuestos sobre salario
- **Calculadora Paro**: estima prestación de desempleo según contribuciones
- **Calculadora Indemnización**: cuantifica despidos procedentes/improcedentes
- **Calculadora Jubilación**: proyecta pensión por años cotizados
- **Calculadora Pagas Extra**: distribuye pagas según convenio colectivo

### 📚 Secciones de Contenido
- **Blog** (19+ artículos): análisis profundos de temas laborales
- **Guías** (15+ guías): pasos prácticos y procedimientos
- **Bajas Laborales**: enfermedad, maternidad, accidente laboral
- **Desempleo**: paro, compatibilidad, cálculos
- **Autónomos**: seguridad social, impuestos
- **Legal**: privacidad, metodología, cookies

### 🔍 SEO & Accesibilidad
- Títulos y meta descriptions optimizados
- Structured data (FAQPage, BreadcrumbList, Calculator)
- Canonical links
- Sitemap XML + Feed RSS
- Responsive mobile-first
- Cumplimiento WCAG básico

---

## 📁 Estructura del Proyecto

```
CalculosLaborales/
├── blog/                      # Artículos de blog (19 archivos)
├── tools/                     # Calculadoras interactivas (19 herramientas)
├── guia/                      # Guías prácticas (15+ archivos)
├── bajas/                     # Sección bajas laborales
├── desempleo/                 # Sección desempleo/paro
├── autonomos/                 # Sección autónomos
├── legal/                     # Página legal, privacidad, cookies
├── assets/
│   ├── css/                   # Estilos CSS
│   ├── js/                    # Scripts JavaScript
│   ├── icons/                 # Iconos SVG
│   └── og/                    # Open Graph images
├── index.html                 # Página de inicio
├── 404.html                   # Página error 404
├── robots.txt                 # Directivas de robots
├── sitemap.xml                # Sitemap XML
├── ads.txt                    # Configuración AdSense
├── site.webmanifest           # PWA manifest
└── README.md                  # Este archivo
```

---

## 🚀 Cómo Usar

### 📖 Para Visitantes
1. Accede a **[CalculosLaborales.es](https://calculoslaborales.es)**
2. Navega por calculadoras en la sección **Tools**
3. Lee guías en **Blog** y **Guía**
4. Consulta términos legales en **Legal**

### 💻 Para Desarrolladores

#### Clonar el Repositorio
```bash
git clone https://github.com/Pampa32/CalculosLaborales.git
cd CalculosLaborales
```

#### Estructura de Archivos
- HTML estático (sin servidor necesario)
- CSS modular en `assets/css/`
- JavaScript vanilla en `assets/js/`
- Optimizado para servir desde cualquier host estático

#### Hacer Cambios Locales
```bash
# Edita cualquier archivo .html
# Sirve localmente (Python):
python -m http.server 8000

# O con Node.js:
npx http-server
```

#### Deploy
1. Compila/valida HTMLs localmente
2. Sube a tu host estático (Netlify, Vercel, tu servidor)
3. Configura certificado SSL
4. Valida en Search Console

---

## 🛠️ Tecnologías

- **HTML5**: Semántica y estructura
- **CSS3**: Responsive design, flexbox/grid
- **JavaScript**: Interactividad y cálculos (vanilla, sin frameworks)
- **JSON-LD**: Structured data (Google Rich Snippets)
- **Meta Tags**: Open Graph, Twitter Card
- **Tools**: Git, VS Code, PowerShell

---

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Archivos HTML | 79 |
| Artículos Blog | 19 |
| Calculadoras | 19 |
| Guías | 15+ |
| Commits Git | 100+ |
| Encoding | UTF-8 sin BOM |
| Tamaño Total | ~1.7 MiB |

---

## 🗺️ Roadmap 2026

### ✅ Completado (Abril 2026)
- [x] SEO hardening: titles, meta descriptions, duplicates
- [x] CTAs in-content en artículos
- [x] FAQ expansion (6-8 Q&A por artículo)
- [x] Validación pre-deploy (encoding, mojibake, links, JSON-LD)
- [x] Publicación en GitHub

### 📋 En Progreso
- [ ] Post-deploy monitoring (Search Console)
- [ ] Ajustes según datos de indexación
- [ ] Nuevas herramientas (vacaciones, reformas)

### 🔮 Futuro (Mayo-Junio 2026)
- [ ] Calculadora vacaciones
- [ ] Calculadora indemnización avanzada
- [ ] Blog en inglés (opcional)
- [ ] PWA offline support

---

## 📈 Estrategia de Calidad

### Pre-Deploy Checklist
- ✅ Encoding: UTF-8 sin BOM en todos los archivos
- ✅ Links: sin URLs rotas o redirects infinitos
- ✅ JSON-LD: estructura parseable y válida
- ✅ Títulos: 35-70 caracteres
- ✅ Meta descriptions: 110-170 caracteres
- ✅ Canonical: presente en todas las URLs
- ✅ Breadcrumb: navegación clara en todas las secciones
- ✅ Mobile: responsive en todos los dispositivos

### Validación automatizada rápida (SEO on-page)
Puedes ejecutar un guard básico para revisar etiquetas clave en todos los HTML:

```bash
python scripts/seo_guard.py
```

El script valida: `title`, `meta description`, `canonical`, `viewport` y presencia de `h1`.

### Checklist técnica de monetización (AdSense)
Para revisar la base técnica mínima de monetización, ejecuta:

```bash
python scripts/adsense_readiness.py
```

Este check verifica:
- Archivos legales y técnicos esenciales (`ads.txt`, privacidad, cookies, aviso legal).
- Cobertura por página de scripts de consentimiento y carga de AdSense.

### Auditoría general antes de subir a hosting
Para ejecutar un repaso completo (SEO + AdSense + enlaces internos + cobertura de sitemap):

```bash
python scripts/predeploy_audit.py
```

### Auditoría de “contenido de poco valor” (AdSense)
Si AdSense reporta *Contenido de poco valor*, puedes priorizar mejoras con:

```bash
python scripts/content_value_audit.py
```

Este reporte detecta en blog/guías:
- páginas con pocas palabras (umbral por defecto: 600),
- enlazado interno bajo (umbral por defecto: 5 enlaces internos).

Plan recomendado de remediación editorial (prioridades URL a URL):
- `PLAN-REMEDIACION-ADSENSE-2026-04-24.md`

### Post-Deploy Monitoring
1. **Semanas 1-2**: Reenviar sitemap en Search Console, inspeccionar 10-15 URLs
2. **Semanas 3-4**: Revisar impresiones/CTR, ajustar titles/metas si es necesario
3. **Mes 2**: Evaluar tráfico orgánico y ranking de keywords

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Puedes:

1. **Reportar errores**: Abre un [issue](https://github.com/Pampa32/CalculosLaborales/issues)
2. **Sugerir mejoras**: Propón cambios en contenido o funcionalidad
3. **Fork + Pull Request**: Implementa cambios directamente
4. **Feedback**: Comenta sobre cálculos o contenido inaccesible

### Guía de Contribución
- Mantén encoding UTF-8 sin BOM
- Valida HTML5 antes de commit
- Usa commits semánticos: `feat:`, `fix:`, `docs:`, `style:`, `test:`
- Describe cambios claramente en el commit

---

## 📝 Licencia

Este proyecto está bajo licencia **MIT**. Ver [LICENSE](LICENSE) para detalles.

Resumen: Puedes usar, modificar y distribuir el código con mención de autoría.

---

## 📞 Contacto & Información

- **Repositorio**: [github.com/Pampa32/CalculosLaborales](https://github.com/Pampa32/CalculosLaborales)
- **Autor**: Pampa32
- **Email**: Consulta la página [Sobre Nosotros](legal/sobre-nosotros.html)

---

## 🎓 Notas de Desarrollo

### Decisiones de Arquitectura
- **Sitio estático**: Sin backend, maximiza velocidad y minimiza costos
- **No JavaScript frameworks**: Vanilla JS para reducir dependencias
- **JSON-LD embebido**: Rich snippets nativos sin librerías externas
- **CSS modular**: Fácil mantenimiento sin preprocessadores

### Lecciones Aprendidas
- Encoding UTF-8 sin BOM es crítico para AdSense compliance
- FAQPage schema density (6-8 Q&A) es señal de autoridad
- CTAs inline (post-breadcrumb) > CTAs footer-only
- Batch validation + staged commits = menos riesgo de mojibake

---

## 📅 Última Actualización

**24 de abril de 2026** - v1.0.0

Proyecto listo para deploy. Todos los archivos validados, encoding correcto, JSON-LD parseable, 0 broken links.

---

**⭐ Si te resulta útil, considera dar una star al repositorio** ⭐
