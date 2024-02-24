# Importando los módulos
from pyrogram import Client, filters
from apps.prl412.utils import prl412
from moduls.utils import utils
from moduls.utils import buttons

@Client.on_message(filters.text & filters.command("query", "/"))
async def queryPRL(clientR, responseC):
    # VARIABLES
    TEXT = responseC.text.split()
    TEXT_FILTRADO = " ".join(TEXT[1:]) if "/" in TEXT[0] else " ".join(TEXT)

    # Recibiendo la postdata
    postdata = utils.get_postdata("prl412")

    # Cuando el mensaje esté vacío
    if not TEXT_FILTRADO and not postdata:
        botones = buttons.keymakers(["Stripe", "Braintree", "Ir a google", "ELIMINAR"], 
                                    ["prl412-stripe", "prl412-braintree", "WEB-https://google.com", "rm"])
        await responseC.reply("El sistema PRL412 te permite buscar páginas web por tecnología web. (es experimental)", reply_markup=botones) # enviar mensaje

    # Cuando el mensaje no esté vacío
    else:
        TEXT_FILTRADO = postdata if postdata else TEXT_FILTRADO
        # Cuando el sistema esté a punto de enviar el comando al sistema PRL412, enviará el sticker
        sticker = await utils.loading_message(responseC, 0)
        respuesta_de_prl412 = prl412.consultar(TEXT_FILTRADO)
        # Cuando el sistema PRL412 haya respondido, el sistema eliminará el sticker y enviará la respuesta
        await sticker.delete()
        sitios = "\n".join(respuesta_de_prl412)
        MENSAJE = f"""<b>CONSULTA:</b> {TEXT_FILTRADO}
- - - - -
{sitios}"""
        await responseC.reply(MENSAJE) # enviar mensaje