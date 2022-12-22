import os


def guardar_captura(driver, nombre_archivo):
    driver.save_full_page_screenshot(f"capturas/{nombre_archivo}.png")

def crear_directorio_capturas():
    current_directory = os.getcwd()
    directorio_capturas = os.path.join(current_directory, 'capturas')
    if not os.path.isdir(directorio_capturas):
        os.mkdir(directorio_capturas)
