# Importando los modulos
from pyrogram import Client, filters
from moduls.utils import utils
from moduls.utils.prl412 import utils
from moduls.utils import buttons

# Creando el filtrador de mensajes
@Client.on_message(filters.text & filters.command("query", "/"))
async def queryPRL(clientC, responseR, postdata=0):
    # variables
    MENSAJE = responseR.text.split()
    COMANDO = " ".join(MENSAJE[1:]) if "/" in MENSAJE[0] else " ".join(MENSAJE) 

    # Si no hay postdata ni comando
    if not postdata and not COMANDO:

        listaTECH = ["braintree", "paypal", "woocommerce", "recaptcha", "cloudflare", "bootstrap"]

        textos = [f"Buscar: {tech}" for tech in listaTECH]
        postdatas = [f"prl412-{tech}" for tech in listaTECH]

        botones = buttons.keymakers(textos, 
                                    postdatas, True, 2)
        await responseR.reply("El sistema PRL412 te permite buscar páginas web por tecnología web. (es experimental)", reply_markup=botones) # enviar mensaje

    # Caso contrario
    # Cuando el mensaje no esté vacío
    else:
        TEXT_FILTRADO = postdata if postdata else COMANDO
        # Cuando el sistema esté a punto de enviar el comando al sistema PRL412, enviará el sticker
        sticker = await utils.loading_message(responseR, 0)
        respuesta_de_prl412 = utils.consultar(TEXT_FILTRADO)
        # Cuando el sistema PRL412 haya respondido, el sistema eliminará el sticker y enviará la respuesta
        await sticker.delete()
        sitios = "\n".join(respuesta_de_prl412)
        MENSAJE = f"""<b>Presentando sitios web con:</b> {TEXT_FILTRADO}
- - - - -
{sitios}"""
        await responseR.reply(MENSAJE) # enviar mensaje