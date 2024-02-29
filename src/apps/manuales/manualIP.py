# Importando los modulos
from pyrogram import Client, filters

# Filtrando los datos
@Client.on_message(filters.text & filters.command("manualIP", "/"))
# Creando la funcion

async def manualIP(clientC, responseR, postdata=0):
    await responseR.reply("Este es el manual del manual IP")