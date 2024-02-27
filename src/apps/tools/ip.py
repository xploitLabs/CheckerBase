# Importando los modulos
from pyrogram import Client, filters
from moduls.utils.prl412 import utils
from moduls.utils import buttons
from moduls.utils import utils as utilsGeneral

# Lista de datos
diccionario = {
    "general": ["org", "ports", "longitude", "latitude", "isp", "city", "asn", "country_name", "os"],
    "vulnerabilidades": ["vulns"]
}

# Crear el filtrador del comando /ip
@Client.on_message(filters.text & filters.command("ip", ["/", "."]))
async def queryIP(clientC, responseR, postdata=0):
    # VARIABLES
    MENSAJE = responseR.text.split()
    COMANDO = " ".join(MENSAJE[1:]) if "/" in MENSAJE[0] else " ".join(MENSAJE) 

    # Si el comando o la postdata está vacío
    if not COMANDO and not postdata:
        await responseR.reply("El comando está vacío!")

    # Si el comando o la postdata no está vacío
    else:
        if COMANDO and not postdata: # Si se recibió un comando:
            if utils.is_ip(COMANDO):                
                utils.consultarIP(COMANDO)
                botones = buttons.keymakers([f"Acceder a: {i}" for i in diccionario],
                                            [f"queryIP-{i}|{COMANDO}" for i in diccionario])
                await responseR.reply(f"Se logró obtener los datos de la IP: {COMANDO}", reply_markup=botones)
            else:
                await responseR.reply("Pon una IP válida!")

        elif postdata: # Cuando se reciba la postdata (general o vulnerabilidad)
            postdata, IP = postdata.split("|")
            respuestaPRL = utils.consultarIP(IP)
            data = [respuestaPRL[elemento] for elemento in diccionario[postdata]]
            await responseR.reply(data) # Enviar la postdata recibida