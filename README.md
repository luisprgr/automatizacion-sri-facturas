# Automatización-sri-facturas

Automatización de la creación de facturas en "SRI & Yo en Línea" de Ecuador usando Python y Selenium

### Limitaciones actuales:

- Los productos que se deseen facturar ya deben estar ingresados.
- Actualmente solo se puede agregar una unidad por producto.
- Funciones como propina, cambio del porcentaje de IVA y facturas negociables no están implementadas.

### Comportamiento por defecto del script:

- Por defecto el script guarda la factura como borrador, para que el usuario pueda revisarla y luego manualmente firmarla y enviarla. 
- El script muestra la ventana del navegador, en la cual se puede ver como se va llenando la factura
- Se guardan capturas de pantalla de los formularios llenados en la carpeta `capturas/` para su posterior revisión

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

### Ejecución

Para probar si se puede ejecutar el script se puede user el siguiente comando (esto mostrará un mensaje con la documentación de la cli del script): 

Con uv:
```bash
uv run main.py --help
```

O dentro del entorno virtual creado anteriormente:
```bash
python3 main.py --help
```

Cualquier comando mencionado puede ejecutarse anteponiendo `uv run` o `python3`/`python` (si el entorno virtual está activado).
Para simplificar, en los ejemplos utilizaré `python`, pero esta parte es intercambiable por `python3` o `uv run`.

### Diferentes formas de ejecutar el script:

- Para ejecutar el script con su comportamiento por defecto (llenar las facturas y guardarlas como borrador):

    ```bash
    python main.py
    ```

- Para verificar que el script complete correctamente la factura, se puede activar el modo de prueba con `--test`. En este modo, el programa inicia sesión y llena la factura con los datos del archivo `datos.json`, pero en lugar de enviarla o guardarla como borrador, congela la ejecución durante 3 minutos. Esto permite al usuario revisar manualmente la factura y asegurarse de que los datos se están ingresando correctamente. Es una opción ideal para validar la información del archivo `datos.json` y confirmar que las facturas contendrán los datos esperados. Transcurridos los 3 minutos, la ventana del navegador se cerrará automáticamente sin enviar la factura ni guardarla como borrador.

    ```bash
    python main.py --test
    ```

- Una vez comprobado que las facturas se generan según lo esperado, y para evitar tener que ingresar al facturador del SRI para enviar manualmente las facturas guardadas como borrador, se puede configurar el script para que firme y envíe automáticamente las facturas. Esto se logra con:

    ```bash
    python main.py --firmar-y-enviar
    ```

- Otras opciones que se pueden añadir a cualquiera de los comandos:
    - `--datos <archivo.json>`: permite pasar el directorio a el archivo json con los datos de la factura que se deben enviar, puede ser util si se quieren enviar varias facturas por ejemplo, para `datos.factura1.json` y `datos.factura2.json` el comando sería de esta forma:
        ```bash
        python main.py --datos datos.factura1.json --firmar-y-enviar
        python main.py --datos datos.factura2.json --firmar-y-enviar
        ```
    - `--no-capturas`: Evita que el script guarde capturas de los formularios llenados en la carpeta `capturas`
    - `--headless`: Ejecuta el script sin mostrar la ventana del navegador, lo que resulta util si se quiere ejecutar el script mediante un cron job o algo similar y se quiere evitar interrumpir al usuario.


### Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
