# Amortiguadores para Capot — sitio Django

Landing page lista para producción para la venta de amortiguadores (bipulsores)
de capot, con buscador de marca/modelo y contacto directo por WhatsApp.

## Estructura

```
amortiguadores_capot/
├── manage.py
├── requirements.txt
├── config/                 # proyecto Django (settings, urls, wsgi)
└── catalog/                # app con el catálogo y la landing
    ├── models.py            # Brand, VehicleModel
    ├── views.py             # vista index()
    ├── urls.py
    ├── admin.py              # alta/edición de marcas y modelos desde /admin
    ├── fixtures/catalog_data.json   # datos precargados (VW, Chevrolet, Fiat, Renault, Peugeot)
    ├── templates/catalog/
    │   ├── base.html
    │   └── index.html
    └── static/catalog/
        ├── css/style.css
        └── js/main.js
```

## Puesta en marcha

```bash
# 1. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Migrar la base de datos
python manage.py migrate

# 3. Cargar marcas y modelos de ejemplo
python manage.py loaddata catalog_data

# 4. (Opcional) crear un superusuario para el panel /admin
python manage.py createsuperuser

# 5. Levantar el servidor
python manage.py runserver
```

Abrí http://127.0.0.1:8000/ para ver la landing.

## Configurar el número de WhatsApp

En `config/settings.py`:

```python
WHATSAPP_NUMBER = "5491112345678"  # código de país + área + número, sin "+" ni espacios
```

Todos los botones de "Consultar por WhatsApp" y los chips de modelo arman
automáticamente el link `https://wa.me/...` con un mensaje predefinido
(incluyendo marca y modelo cuando corresponde).

## Agregar o editar marcas y modelos

Dos opciones:

1. **Panel de administración**: entrá a `/admin/`, agregá una `Marca` y sus
   `Modelo` relacionados (inline en la misma pantalla).
2. **Fixture**: editá `catalog/fixtures/catalog_data.json` y volvé a correr
   `python manage.py loaddata catalog_data`.

## Integrar esta app en un proyecto Django existente

Si ya tenés un proyecto Django y solo querés sumar esta app:

1. Copiá la carpeta `catalog/` dentro de tu proyecto.
2. Agregá `"catalog"` a `INSTALLED_APPS`.
3. Incluí sus URLs en tu `urls.py` raíz: `path("", include("catalog.urls"))`.
4. Corré `python manage.py makemigrations catalog && python manage.py migrate`.
5. Cargá los datos: `python manage.py loaddata catalog/fixtures/catalog_data.json`.
6. Definí `WHATSAPP_NUMBER` en tu `settings.py`.

## Diseño

- **Paleta**: grafito/acero (`#14181D`, `#2E3944`) + amarillo de taller
  (`#F5B400`) como acento, y verde WhatsApp (`#25D366`) reservado exclusivamente
  para los botones de contacto.
- **Tipografía**: Oswald condensada para títulos, Inter para texto, JetBrains
  Mono para etiquetas técnicas (specs, contadores).
- **Elemento distintivo**: ilustración SVG de un bipulsor a gas que se
  comprime y extiende suavemente en el hero, representando el producto en sí.
- 100% responsive (mobile, tablet, desktop), sin frameworks CSS externos.
