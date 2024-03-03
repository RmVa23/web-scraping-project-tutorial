import requests

url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
respuesta = requests.get(url, headers=h)

# Nos da todos los atributos disponibles
atributos = dir(respuesta)

# Da el código de respuesta de la página web a la que intentamos acceder (200 - éxito)
if respuesta.status_code == 200:
    print(f"La conexión se ha realizado con éxito: {respuesta.status_code}")

else:
    print(f"Hay un error con la conexión: {respuesta.status_code}")

# Da una breve descripción del código de respuesta
descript = respuesta.reason
print(f"El error {respuesta.status_code} significa: {descript}")
print(f"{descript} - Error de Cliente: El cliente no posee los permisos necesarios para cierto contenido,"
      "por lo que el servidor está rechazando dar una respuesta apropiada")
print()

# Análisis de la petición

# Información de la petición:
# -* La peticion se llama REQUEST de la libreria REQUESTS (es decir, en sigular es una petición de informacion dentro de la librería,
# y en plural es la propia librería.
info = respuesta.request
print(f"{info} - nos devuelve un objeto.")
print()

# Vemos los atributos del objeto que nos devuelve
# Es decir, las cabeceras de la petición (request)
atributos_peticion = dir(respuesta.request) # o dir(info)

# Al observar las cabeceras que nos devuelve en el terminal vemos que nos da 'headers'
user_agent = respuesta.request.headers # o info.headers
# Nos devuelve el User-Agent que estamos usando, con unos valores predeterminados.
# Estos valores podemos cambiarlos.

# Podemos acceder a más cabeceras de la petición, las más interesantes sería 'url' y 'path_url':
direccion = respuesta.request.url # info.url
# Nos devuelve la url a la que intentamos acceder

subdireccion = respuesta.request.path_url # info.path_url
# Nos devuelve el recurso al que querermos acceder dentro del host del servidor, que en este caso sería www.macrotrends.net

# Analisis respuesta

# Analizamos algunos atributos de la respuesta, los vimos al principio: 'atributos = dir(respuesta)'
# Como podemos observar, para acceder a los atributos de la respuesta, escribimos 'respuesta + . + nombre atributo que queramos'
# A diferencia de la petición, que sería: 'respuesta + request (peticion) + . + nombre atributo de la peticion que queramos'
# Si nombrasemos la peticion con una variable, sería: 'nombre variable + . + nombre atributo de la petición que queramos'

# Vemos si hemos recibido alguna cookie del servidor
cookies = respuesta.cookies
# Nos devuelve un objeto del tipo RequestsCokkieJar[] con una lista de las cookies recibidas entre corchetes,
# en este caso vemos que nos ha enviado una.

header = respuesta.headers

conexion = respuesta.ok
# Devuelve un booleano: True o False
# Será True cuando el código de respuesta sea inferior a 400, ya que en la mayoría de los casos un codigo de <400 es una respuesta existosa

historial = respuesta.history
# Devuelve el historial si hemos hecho alguna redireccion, en nuestro caso está vacío porque ni hemos logrado acceder correctamente


# 3 formas de acceder al cuerpo de la respuesta

bytes = respuesta.content
# Devuelve el cuerpo o contenido en bytes

texto = respuesta.text
# Devuelve el cuerpo de la respuesta en strings, lo que evita que tengamos que decodificarlo nosotros
# Vemos como nos explica los pasos para ser incluídos en una lista blanca (en plazo de 24h.) y permitirnos el acceso

# En este caso usamos un método, no un atributo
jason = respuesta.json
# Devuelve el cuerpo de la respuesta en formato json



# Whatmybrowser - página web que nos da nuestro user-agent (buscar: 'cual es mi agente de ususario?')
