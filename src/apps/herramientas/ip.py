# Importando los modulos
from pyrogram import Client, filters # Controlar los comandos y filtrarlos
# Acá es donde importaremos la herramienta que acabamos de crear
from moduls.utils.herramientas.ipBuscador import buscarIP
# Con esto le decimos al sistema que, DENTRO DE LA CARPETA PRINCIPAL "MODULS", EN LA CARPETA UTILS, EN LA CARPETA HERRAMIENTAS, dentro del archivo "ipbuscador.py" importe nuestra herramienta llamada buscarIP

# Crear un controlador
@Client.on_message(filters.text & filters.command("ip", "/"))
async def consultarIP(clientC, responseR, postdata=0): # Una función asíncrona
    # acá es donde nosotros le diremos al sistema qué hacer cuando reciba un comando.
    # VAMOS A GUARDAR LAS VARIABLES MAS IMPORTANTES.
    TEXTO_DEL_MENSAJE = responseR.text.split() # Es decir: /ip, o todo el texto que el usuario envíe al bot.
    IP = " ".join(TEXTO_DEL_MENSAJE[1:]) if "/" in TEXTO_DEL_MENSAJE[0] else " ".join(TEXTO_DEL_MENSAJE[0:]) # Con esto eliminamos el comando /ip y nos quedamos con el resto del texto

    # Si no hay comando ni postdata
    if not IP:
        # Como el texto restante está vacío, vamos a enviar una introducción a este comando
        await responseR.reply("El comando /ip nos permite obtener información de otra IP, usalo con: /ip tu_ip")
    
    # Caso contrario:
    else:
        # Caso contrario, vamos a enviar el resto del comando a la herramienta que obtendrá datos de la IP
        info_ip = buscarIP(IP) # Obtenemos los datos de la IP y lo almacenamos en "info_ip"
        await responseR.reply(info_ip) # respondemos con un mensaje indicando los datos de la IP