# Automatización-sri-facturas
Automatización de la creación de facturas en "SRI &amp; Yo en Línea" de Ecuador usando python y selenium


### Limitaciones actuales:
- Los productos que se deseen facturar ya deben estar ingresados.
- Actualmente solo se puede agregar una unidad por producto.
- Funciones como propina, cambio del porcentaje de IVA y facturas negociables no están implementadas.
- Debido a que es una primera versión, el script está limitado a guardar la factura sin firmar, la cual luego debe ser firmada manualmente por el usuario en el sitio web de SRI &amp; Yo en Línea.

### Requerimientos:

- Python 3.11 o superior
- Poetry 1.2.2 o superior
- Firefox

### Instalación:

1. Clonar el repositorio

```bash
git clone https://github.com/luisprgr/automatizacion-sri-facturas.git
```

2. Instalar dependencias

```bash
poetry install
```

3. Crear archivo con los datos para la facturación

```bash
cp datos.json.example datos.json
```

4. Editar el archivo `datos.json` con los datos de la factura que se realizará

### Ejecución:

Para ejecutar el script se debe ejecutar el siguiente comando: 

```bash
poetry run python main.py
```

### Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
