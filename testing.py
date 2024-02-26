# Importando los módulos
import requests, json

# Creando una funcion
def obtenerDatosIP(IP):
    # URL de la API
    URL = f"http://ip-api.com/json/{IP}"

    # Obteniendo datos de la IP usando la API con la librería
    respuesta_de_la_API = requests.get(URL).json()

    # Ordenando json
    JSON_ORDENADO = json.dumps(respuesta_de_la_API, indent=4)

    # mostrando por pantalla el json ordenado
    print (JSON_ORDENADO)

# --- 1RA VEZ PIDIENDO DATOS ---
IP_del_usuario = input("Pon una IP a continuación: ")
obtenerDatosIP(IP_del_usuario)

# --- 2DA VEZ PIDIENDO DATOS ---
IP_del_usuario = input("Pon una IP a continuación: ")
obtenerDatosIP(IP_del_usuario)

# --- 3RA VEZ PIDIENDO DATOS ---
IP_del_usuario = input("Pon una IP a continuación: ")
obtenerDatosIP(IP_del_usuario)