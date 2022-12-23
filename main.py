import json
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from src.pantallas.login.login import login
from src.pantallas.emision_facturas.factura import emision_factura
from src.utilidades.utilidades import crear_directorio_capturas


if __name__ == '__main__':

    app_data: dict = None
    guardar_capturas: bool = True
    headless: bool = False
    borrador: bool = True
    test: bool = True

    if guardar_capturas:
        crear_directorio_capturas()

    with open('datos.json') as f:
        app_data = json.load(f)

    if app_data is not None:
        firefox_options = Options()
        firefox_options.headless = headless

        firefox = Firefox(options=firefox_options)
        
        firefox.set_window_size(1920, 1080)

        login(firefox, guardar_capturas, app_data.get('ruc'), app_data.get('password'))
        emision_factura(firefox, guardar_capturas, app_data.get('firma'), app_data.get('factura'), borrador, test)

        firefox.close()
    else:
        print('no se pudo leer datos.json')
