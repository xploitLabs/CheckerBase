# Importando los modulos
from pyrogram import Client, filters
from moduls.utils import utils
from moduls.utils.buttons import keymakers

# Controlando el mensaje con las siguientes características
@Client.on_message(filters.command(["start", "iniciar", "inicio"], prefixes=["!", "/", "."]) | filters.text)
async def start(client, response):
    postdata = utils.get_postdata("start")

    # Page initial
    if not postdata:
        buttons = keymakers(["✅ Continue", "IP API DEMO"], ["start-1", "ipQ-0"])
        await response.reply("""✅ The bot is on now!.

You can use other functions for the control commands.""", reply_markup=buttons)

    # Process other pages
    else:
        botones = keymakers(
            [f"{number}" for number in range(postdata-1, postdata+3)],
            [f"start-{number}" for number in range(postdata-1, postdata+3)],
        )
        await response.reply(f"Postdata received: {postdata}", reply_markup=botones)