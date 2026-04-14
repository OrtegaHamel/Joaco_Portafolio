# Joaco.fr - Portafolio Profesional

Este es mi primer proyecto como desarrollador independiente. Es el sitio web personal y portafolio profesional del realizador audiovisual Joaquín Fernández, una plataforma web desarrollada con **Django 5.2**, diseñada como un laboratorio técnico donde implementé soluciones de internacionalización, gestión de archivos en servidores de producción y animaciones interactivas en el frontend.

🌐 **Sitio en vivo:** [https://joaco.fr](https://joaco.fr)  

`![Home Page](screenshots/home.png)`
`![Home Page](screenshots/categoria.png)`
`![Home Page](screenshots/detalle_proyecto.png)`
`![Home Page](screenshots/aboutme.png)`

---

## 🚀 Desafíos Técnicos y Aprendizajes

### 1. Despliegue en Entorno Real (DirectAdmin)
Este sitio fue desplegado en un servidor privado mediante **DirectAdmin**. 
* **Gestión de Estáticos:** Implementé `WhiteNoise` con `CompressedManifestStaticFilesStorage` para servir archivos CSS y JS de forma eficiente sin depender de Nginx/Apache para los archivos estáticos de Django.
* **Media en Producción:** Configuré rutas dinámicas para que los archivos subidos por el administrador se almacenen directamente en la carpeta pública (`public_html/media`), permitiendo una persistencia real de datos.

### 2. Internacionalización Trilingüe (FR, ES, EN)
El sitio está diseñado para una audiencia global, gestionando tres idiomas simultáneamente:
* Uso de `django-modeltranslation` para traducir contenido dinámico desde la base de datos (títulos, descripciones de proyectos).
* Middleware de lenguaje para detectar y recordar la preferencia del usuario.
* Traducción de interfaces mediante archivos `.po` y `.mo` (GNU gettext).

### 3. Frontend Interactivo y Animaciones
El "Home" del sitio cuenta con una experiencia visual única:
* **Seguimiento Ocular:** Implementación de lógica en JavaScript para que los ojos del avatar sigan el movimiento del cursor del usuario.
* **Layout Dinámico:** Ubicación precisa de objetos mediante CSS avanzado y animaciones que dotan al sitio de una estética "retro".
* **Diseño Responsivo:** Adaptación completa a dispositivos móviles manteniendo la interactividad.

### 4. SEO y UX con Slugs
En lugar de IDs numéricos, el sitio utiliza **Slugs** para las URLs de los proyectos, lo que mejora drásticamente el posicionamiento SEO y hace que los enlaces sean legibles y amigables para el usuario.

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.11 + Django 5.2
* **Base de Datos:** MySQL (vía PyMySQL)
* **Servidor de Aplicaciones:** Gunicorn
* **Manejo de Estáticos:** WhiteNoise 6.6
* **Tratamiento de Imágenes:** Pillow (Procesamiento de fotos de perfil y proyectos)
* **Frontend:** HTML5, CSS3 (Custom Retro Design), JavaScript (Vanilla)

## 📦 Dependencias Principales

Django==5.2
django-modeltranslation==0.19.19
whitenoise==6.6.0
pillow==12.1.0
PyMySQL==1.1.2
python-dotenv==1.2.1

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)