# acá es donde crearemos la herramienta que va a obtener los datos de la IP.

# Primero importamos los modulos (es decir, complemnentos de python)
import requests # Nos permitirá comunicarnos con páginas webs

def buscarIP(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}").json() # Con esto obtenemos los datos de la IP indicada por medio de una API.
    return response # La función responderá con los datos de la IP