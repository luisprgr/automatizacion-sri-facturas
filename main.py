import json
from pathlib import Path

import typer
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from src.pantallas.emision_facturas.factura import emision_factura
from src.pantallas.login.login import login
from src.utilidades.cli_options import (
    DatosOption,
    FirmarOption,
    GuardarCapturasOption,
    HeadlessOption,
    TestOption,
)
from src.utilidades.utilidades import crear_directorio_capturas

app = typer.Typer(add_completion=False)


@app.command()
def crear_factura(
    datos_file: DatosOption = Path("datos.json"),
    headless: HeadlessOption = False,
    guardar_capturas: GuardarCapturasOption = True,
    test: TestOption = False,
    firmar_y_enviar: FirmarOption = False,
) -> None:
    app_data: dict = None

    print("\nConfiguración:")
    if headless:
        print("\t- El script se ejecutará en modo headless")
    else:
        print("\t- Se abrirá una ventana del navegador para ver los pasos que se van a seguir")

    if guardar_capturas:
        print("\t- Se guardaran capturas de pantalla de los formularios llenados (login y factura)")
    else:
        print("\t- No se guardaran capturas de pantalla")

    if test:
        print("\t- El script se pausará 2 minutos tras llenar la factura para revisión manual.")
    else:
        print("\t- Apenas el script termine se cerrará el navegador")

    if not test:
        if firmar_y_enviar:
            print("\t- Una vez llena la factura se procederá a firmarla y enviarla")
        else:
            print("\t- Se guardará la factura como borrador")

    print("\n")

    if guardar_capturas:
        crear_directorio_capturas()

    with datos_file.open() as f:
        app_data = json.load(f)

    if app_data:
        firefox_options = Options()
        firefox_options.headless = headless

        firefox = Firefox(options=firefox_options)

        firefox.set_window_size(1920, 1080)

        login(firefox, guardar_capturas, app_data.get("ruc"), app_data.get("password"))

        emision_factura(
            firefox,
            guardar_capturas,
            app_data.get("firma"),
            app_data.get("factura"),
            firmar_y_enviar,
            test,
        )

        firefox.close()
    else:
        print("no se pudo leer datos.json")


if __name__ == "__main__":
    app()
