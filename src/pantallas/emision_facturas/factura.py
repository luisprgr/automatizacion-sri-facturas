import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.utilidades.comun import URL_SRI_Y_YO_FACTURA
from src.utilidades.utilidades import guardar_captura
from src.pantallas.emision_facturas import ids


dropdown_xpath = lambda value: f"//li[contains(text(),'{value}')]"
pagos_dropdown_xpath = lambda value: f"//td[contains(text(),'{value}')]"

wait_time_dropdown = lambda: time.sleep(0.5)
wait_time_popup = lambda: time.sleep(0.5)
wait_time_search = lambda: time.sleep(1)


def emision_factura(driver, guardar_capturas: bool, firma: str, factura: dict, borrador: bool, test: bool):
    
    driver.get(URL_SRI_Y_YO_FACTURA)
    wait = WebDriverWait(driver, 10)
    hover = ActionChains(driver)

    def click_element(element_id, by=By.ID):
        wait.until(expected.presence_of_element_located((by, element_id)))
        element = driver.find_element(by=by, value=element_id)
        hover.move_to_element(element).perform()
        element = driver.find_element(by=by, value=element_id)
        hover.click(element).perform()

    def write_in_element(element_id, by=By.ID, value=""):
        wait.until(expected.presence_of_element_located((by, element_id)))
        element = driver.find_element(by=by, value=element_id)
        element.send_keys(value)
        element.send_keys(Keys.TAB)

    def scroll_to_element(element_id, by=By.ID):
        wait.until(expected.presence_of_element_located((by, element_id)))
        element = driver.find_element(by=by, value=element_id)
        driver.execute_script("arguments[0].scrollIntoView();", element)


    click_element(ids.ESTABLECIMIENTO_DROPDOWN_ID)
    wait_time_dropdown()
    click_element(dropdown_xpath(factura.get('establecimiento')), By.XPATH)
    
    if factura.get("guia_remision") != "":
        click_element(ids.GUIA_REMISION_INPUT_ID)
        write_in_element(ids.GUIA_REMISION_INPUT_ID, value=factura.get("guia_remision"))

    # Adquiriente

    click_element(ids.TIPO_IDENTIFICACION_DROPDOWN_ID)
    wait_time_dropdown()
    click_element(dropdown_xpath(factura.get('adquiriente').get('tipo_identificacion')), By.XPATH)

    click_element(ids.IDENTIFICACION_INPUT_ID)
    write_in_element(ids.IDENTIFICACION_INPUT_ID, value=factura.get('adquiriente').get('identificacion'))


    click_element(ids.RAZON_SOCIAL_INPUT_ID)
    write_in_element(ids.RAZON_SOCIAL_INPUT_ID, value=factura.get('adquiriente').get('razon_social'))
    
    if factura.get('adquiriente').get('direccion') != "":
        click_element(ids.DIRECCION_INPUT_ID)
        write_in_element(ids.DIRECCION_INPUT_ID, value=factura.get('adquiriente').get('direccion'))

    if factura.get('adquiriente').get('telefono') != "":
        click_element(ids.TELEFONO_INPUT_ID)
        write_in_element(ids.TELEFONO_INPUT_ID, value=factura.get('adquiriente').get('telefono'))
    
    click_element(ids.CORREO_ELECTRONICO_INPUT_ID)
    write_in_element(ids.CORREO_ELECTRONICO_INPUT_ID, value=factura.get('adquiriente').get('correo_electronico'))

    # Producto
    
    for producto in factura.get('productos'):
        click_element(ids.ADD_PRODUCTO_BUTTON_ID)
        wait_time_popup()
    
        click_element(ids.CODIGO_PRODUCTO_INPUT_ID)
        write_in_element(ids.CODIGO_PRODUCTO_INPUT_ID, value=producto.get('codigo_producto'))
        click_element(ids.BUSCAR_PRODUCTO_BUTTON_ID)
        wait_time_search()
    
        click_element(ids.PRODUCTO_ENCONTRADO_BUTTON_ID)
        wait_time_popup()

    # Forma de pago

    scroll_to_element(ids.ADD_FORMA_PAGO_BUTTON_ID)

    for forma_pago in factura.get('formas_pago'):
        click_element(ids.ADD_FORMA_PAGO_BUTTON_ID)
        wait_time_popup()
    
        click_element(ids.FORMA_PAGO_DROPDOWN_ID)
        wait_time_dropdown()
        click_element(pagos_dropdown_xpath(forma_pago.get('forma_pago')), By.XPATH)

        click_element(ids.FORMA_PAGO_VALOR_INPUT_ID)
        write_in_element(ids.FORMA_PAGO_VALOR_INPUT_ID, value=forma_pago.get('valor'))

        click_element(ids.FORMA_PAGO_PLAZO_INPUT_ID)
        click_element(ids.FORMA_PAGO_PLAZO_INPUT_ID)
        write_in_element(ids.FORMA_PAGO_PLAZO_INPUT_ID, value=forma_pago.get('plazo'))

        click_element(ids.FORMA_PAGO_TIEMPO_DROPDOWN_ID)
        wait_time_dropdown()
        click_element(pagos_dropdown_xpath(forma_pago.get('tiempo')), By.XPATH)

        click_element(ids.FORMA_PAGO_GUARDAR_BUTTON_ID)
        wait_time_popup()
    
    # Campos adicionales

    if factura.get('campos_adicionales') != None and len(factura.get('campos_adicionales')) > 0:
        for campo_adicional in factura.get('campos_adicionales'):
            click_element(ids.ADD_CAMPO_ADICIONAL_BUTTON_ID)
            wait_time_popup()
            
            click_element(ids.CAMPO_ADICIONAL_NOMBRE_INPUT_ID)
            write_in_element(ids.CAMPO_ADICIONAL_NOMBRE_INPUT_ID, value=campo_adicional.get('nombre'))

            click_element(ids.CAMPO_ADICIONAL_DESCRIPCION_INPUT_ID)
            write_in_element(ids.CAMPO_ADICIONAL_DESCRIPCION_INPUT_ID, value=campo_adicional.get('descripcion'))

            click_element(ids.CAMPO_ADICIONAL_GUARDAR_BUTTON_ID)
            wait_time_popup()

    if guardar_capturas:
        guardar_captura(driver, "factura")

    # Guardar factura

    if borrador:
        click_element(ids.GUARDAR_SIN_FIRMAR_BUTTON_ID)
        print("Factura guardada como borrador")
    else:
        click_element(ids.GUARDAR_Y_FIRMAR_BUTTON_ID)
        wait_time_popup()
        click_element(ids.CLAVE_CERTIFICADO_INPUT_ID)
        write_in_element(ids.CLAVE_CERTIFICADO_INPUT_ID, value=firma)
        if test:
            click_element(ids.CANCELAR_ENVIO_FACTURA_FIRMADA_BUTTON_ID)
        else:
            click_element(ids.ENVIAR_FACTURA_FIRMADA_BUTTON_ID)
    
    time.sleep(2)
