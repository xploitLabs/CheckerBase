# Importando los modulos
from pyrogram import Client, filters
from moduls.utils.buttons import keymakers
from moduls.utils import utils

# Controlando el mensaje con las siguientes características
@Client.on_message(filters.command(["start", "iniciar", "inicio"], prefixes=["!", "/", "."]) & filters.text)
async def start(client, response, postdata=0):
    # Page initial
    if not postdata:
        var = "This is a large text"
        continuevar = 1
        codeVARstr = utils.saveVAR(var) # Save the key
        codeVARint = utils.saveVAR(continuevar) # Save the key
        buttons = keymakers(["✅ Continue", "IP API DEMO", "Testing"], [f"start-{codeVARint}", "ipQ-0", f"start-{codeVARstr}"])
        await response.reply("""✅ The bot is on now!.

You can use other functions for the control commands.""", reply_markup=buttons)

    elif type(postdata) is str:
        await response.reply(f"Postdata VAR received: {postdata}")

    # Process other pages
    else:
        botones = keymakers(
            [f"{number}" for number in range(postdata-1, postdata+3)],
            [f"start-{number}" for number in range(postdata-1, postdata+3)],
        )
        await response.reply(f"Postdata INT received: {postdata}", reply_markup=botones)