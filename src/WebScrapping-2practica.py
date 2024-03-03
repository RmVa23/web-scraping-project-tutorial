import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web
url = 'https://loscochesmasvendidos.com/'

# Realizar la solicitud GET
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    articulos = soup.find_all("div", class_="col-sm-6 col-xxl-4 post-col")

    # Crear una lista para almacenar los datos
    datos = []

    # Iterar sobre cada artículo
    for articulo in articulos:
        # Obtener el enlace a la página individual del artículo
        enlace_articulo = articulo.find("h2", class_="entry-title").a["href"]

        # Realizar una solicitud GET a la página individual del artículo
        response_articulo = requests.get(enlace_articulo)

        # Comprobar si la solicitud fue exitosa
        if response_articulo.status_code == 200:
            # Parsear el contenido HTML de la página individual del artículo
            soup_articulo = BeautifulSoup(response_articulo.content, 'html.parser')

            # Encontrar el elemento que contiene el título del ranking
            titulo_ranking_elemento = soup_articulo.find("h2")
            if titulo_ranking_elemento:
                strong_element = titulo_ranking_elemento.strong
                if strong_element:
                    titulo_ranking = strong_element.text.strip()
                else:
                    titulo_ranking = None
            else:
                titulo_ranking = None

            # Encontrar todos los elementos li que representan el ranking de coches
            ranking_coches = soup_articulo.find_all("li")

            # Crear una lista para almacenar el ranking de coches
            ranking = [ranking_coche.text.strip() for ranking_coche in ranking_coches]

             # Agregar los datos a la lista de datos
            datos.append({
                'Título del ranking': titulo_ranking,
                'Enlace del artículo': enlace_articulo,
                'Ranking': ranking})

# Crear el DataFrame
df = pd.DataFrame(datos)

# Imprimir el DataFrame
print(df)




