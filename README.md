# Automatización-sri-facturas
Automatización de la creación de facturas en "SRI & Yo en Línea" de Ecuador usando python y selenium


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

- Python 3.13 o superior
- Firefox

### Requerimientos opcionales:

- [uv](https://docs.astral.sh/uv/) 

### Preparación del entorno:

1. Clonar el repositorio

    ```bash
    git clone https://github.com/luisprgr/automatizacion-sri-facturas.git
    ```

2. Instalar dependencias

    ##### Si `uv` está instalado:

    ```bash
    uv sync
    ```

    ##### O mediante `venv` + `pip`:

    Creamos un entorno virtual
    
    ```bash
    python -m venv .venv
    ```

    Activamos el entorno virtual (en Windows):

    ```Powershell
    .venv\Scripts\activate
    ```

    Activamos el entorno virtual (en macOS/Linux):

    ```bash
    source .venv/bin/activate
    ```

    Finalmente, instalamos las dependencias con:
    ```bash
    pip install .
    ````

3. Creamos un archivo con los datos para la facturación (en datos.json.example hay un ejemplo de como se debe crear la factura)

    ```bash
    cp datos.json.example datos.json
    ```

4. Editar el archivo `datos.json` con los datos de la factura que se realizará

### Ejecución:

Para ejecutar el script se debe ejecutar el siguiente comando: 

Con uv:
```bash
uv run main.py
```

O ejecutando dentro del entorno virtual creado anteriormente:
```bash
python3 main.py
```

### Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
