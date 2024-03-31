# Automatización-sri-facturas
Automatización de la creación de facturas en "SRI &amp; Yo en Línea" de Ecuador usando python y selenium


### Limitaciones actuales:
- Los productos que se deseen facturar ya deben estar ingresados.
- Actualmente solo se puede agregar una unidad por producto.
- Funciones como propina, cambio del porcentaje de IVA y facturas negociables no están implementadas.
- No tiene una interfaz de línea de comandos (_WIP_).

### Comportamiento actual:
Por defecto el script guarda la factura como borrador, para que el usuario pueda revisarla y luego manualmente firmarla y enviarla. 

También por defecto el script corre en modo headless (sin mostrar el navegador), si se desea ver visualmente los pasos del script se debe crear una variable `ASRI_HEADLESS` con el valor False

Si se desea que el script firme y envíe la factura automáticamente, se debe crear la variable de entorno `ASRI_BORRADOR` con el valor `False`.

Otra comportamiento que puede tener la aplicación es mostrar todo el flujo de creación de la factura hasta el ingreso de la firma, pero cancelando el envío de la factura al final. Con el objetivo de que el usuario pueda supervisar todo el flujo de la aplicación. 

Para esto se debe crear la variable de entorno `ASRI_TEST` con el valor `True` y `ASRI_BORRADOR` con el valor `False` para que la factura no se guarde como borrador.

Bajo este modo, la aplicación no se cerrará al finalizar el proceso, en vez de eso se quedará abierta durante 3 minutos para que el usuario pueda revisar el resultado.

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
