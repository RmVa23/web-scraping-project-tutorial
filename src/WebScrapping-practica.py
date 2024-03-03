import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Guardamos la url que nos interesa en una variable
link = 'https://loscochesmasvendidos.com/'

# 2. Con la libreria request, extraemos la información de la url y la guardamos en otra variable 'resultado'
resultado = requests.get(link)

print(resultado.status_code)
print(resultado.reason)

# 3. Comprobamos que la solicitud fue exitosa:
if resultado.status_code == 200:

    # 4. Convertimos el resultado en formato texto con BS4, ya que necesitamos analizar y extraer datos específicos del HTML de la página web
    soup = BeautifulSoup(resultado.text, "html.parser")

    # 5. Buscamos dentro de la clase container (donde están almacenados todos los articulos de la página)
    cuadros = soup.find("div", class_="col-lg-8 content-area")
    contenedor_articulos = cuadros.find("div", class_="row gutter-parent-14 post-wrap")
    articulos = contenedor_articulos.find_all("div", class_="col-sm-6 col-xxl-4 post-col")

    # 6. Lista para almacenar los datos de los artículos
    datos_articulos = []

    for articulo in articulos:
        # Extraemos el título y la URL del título
        titulo = articulo.find("h2", class_="entry-title").text.strip()
        url = articulo.find("h2", class_="entry-title").a["href"]

        # Buscamos las etiquetas que contienen el país y el mes+año
        etiquetas = articulo.find("div", class_="cat-links").find_all("a")
        pais = None
        mes_y_anio = None
        for etiqueta in etiquetas:
            if "paises" in etiqueta["href"]:
                pais = etiqueta.text.strip()
            elif "mes" in etiqueta["href"]:
                mes_y_anio = etiqueta.text.strip()


        # Buscamos la etiqueta que contiene el autor
        autor = articulo.find("div", class_="by-author vcard author").a.text.strip()

        # Almacenamos los datos en un diccionario
        datos_articulo = {
            "Título": titulo,
            "URL": url,
            "País": pais,
            "Mes y Año": mes_y_anio,
        }
        # Añadimos los datos recopilados a un diccionario
        datos_articulos.append(datos_articulo)

    # Creamos un DataFrame a partir de los datos almacenados
    data = pd.DataFrame(datos_articulos)

# Imprimimos el DataFrame

print(data[['País', 'Mes y Año']])

# Convertimos a archivo CSV
#data.to_csv('coches-mas-vendidos.csv', index=False)
