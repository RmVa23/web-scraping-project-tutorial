# Este código ha sido ejecutado en local tal cual está a continuación, con resultado favorable.
# A continuación del código, comento los pasos realizados para intentar adaptar y ejecutarlo en el codespace, sin éxito.

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

# Configuramos el driver de Selenium
driver = webdriver.Firefox()

url ='https://coinmarketcap.com/es/currencies/ethereum/historical-data/'

# Cargamos la página con Selenium
driver.get(url)

# Esperamos a que la página cargue completamente (se puede ajustar el tiempo según sea necesario)
driver.implicitly_wait(100)  # Esperamos hasta 100 segundos

# Obtenemos el HTML de la página después de que se haya cargado completamente
html = driver.page_source

# Cierramos el driver de Selenium
driver.quit()

# Parseamos el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

tabla = soup.find('table', {'class':"sc-14cb040a-3 eGIvUX cmc-table"})

datos = []

if tabla:
    elementos = tabla.find_all('tr')
    for elemento in elementos:
        celdas = elemento.find_all('td')
        if len(celdas) == 7:
            fecha = celdas[0].text.strip()
            abrir = celdas[1].text.strip()
            alto = celdas[2].text.strip()
            bajo = celdas[3].text.strip()
            cerrar = celdas[4].text.strip()
            volumen = celdas[5].text.strip()
            cap_mercado = celdas[6].text.strip()

            fila = {
                'Fecha': fecha,
                'Abrir': abrir,
                'Alto': alto,
                'Bajo': bajo,
                'Cerrar': cerrar,
                'Volumen': volumen,
                'Cap. de Mercado': cap_mercado}

            datos.append(fila)

data = pd.DataFrame(datos)
print(data)

# Obtenemos un dataframe con los datos de ETH del último trimestre.
# Para obtener otro período, tendríamos que recurrir a la API del sitio,
# lo que haremos en el proyecto API, para obtener los datos mensuales de los últimos años

data.to_csv('1-trimestre-2024-ETH.csv', index=False)

# ------------------------Fin del código de obtención de datos---------------------------------------------------

# He probado sin resultado favorable las siguientes soluciones para ejecutar este código desde el codespace:
# - 1. En el Jupyter Notebook use HtmlUnitDriver: Navegador sin cabeza que está integrado directamente en Selenium WebDriver y no requiere la instalación de controladores externos.
# - 2. Tambien descargue del driver de Firefox (geckodriver) y probe distintas formas, como las expuestas a continuación:


# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options

# gecko_driver = r'C:\Users\rmace\Gecko Driver - Webdriver Firefox\geckodriver-v0.34.0-win-aarch64\geckodriver.exe'

# firefox_options = Options()
# firefox_options.headless = True 

# driver = Firefox(options=firefox_options, executable_path=gecko_driver)
#---------------------------------------------------------------

# from selenium import webdriver

# gecko_driver = r'C:\Users\rmace\Gecko Driver - Webdriver Firefox\geckodriver-v0.34.0-win-aarch64\geckodriver.exe'

# firefox_options = webdriver.FirefoxOptions()
# firefox_options.headless = True  

# driver = webdriver.Firefox(executable_path=gecko_driver, options=firefox_options)


# Además, consideré usar Selenium Grid (para ejecutar pruebas automatizadas en una máquina remota
# sin necesidad de descargar e instalar un controlador específico en el entorno local). 
# También Sauce Labs (servicio en la nube que ofrece navegadores y ambientes preconfigurados para pruebas automatizadas), y proporciona una API.
# Seguiré trabajando en encontrar una solución que me permita ejecutar el código, tanto si es una de las mencionadas anteriormente,
# como si es la descarga de otro driver como el de Chrome.
