# Automatización-sri-facturas
Automatización de la creación de facturas en "SRI &amp; Yo en Línea" de Ecuador usando python y selenium


### Limitaciones actuales:
- Los productos que se deseen facturar ya deben estar ingresados.
- Actualmente solo se puede agregar una unidad por producto.
- Funciones como propina, cambio del porcentaje de IVA y facturas negociables no están implementadas.
- No tiene una interfaz de línea de comandos (_WIP_).

### Comportamiento actual:
- Por defecto el script guarda la factura como borrador, para que el usuario pueda revisarla, firmarla y enviarla. Si se desea que el script envíe la factura automáticamente, se debe cambiar las variables `borrador` y `test` a `False` en el archivo `main.py`.
- Otra comportamiento que puede tener la aplicación es mostrar todo el flujo de creación de la factura hasta el ingreso de la firma, para que el usuario pueda supervisar este proceso, pero cancelando el envío de la factura al final. Para esto se debe cambiar la variable `test` a `True` y `borrador` a `False` en el archivo `main.py`. 

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
