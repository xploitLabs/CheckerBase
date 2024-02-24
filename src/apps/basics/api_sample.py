# Importing the moduls
from pyrogram import Client, filters
from moduls.utils.buttons import keymakers
from moduls.utils import utils
import requests, json

# Control text messages with the "ipquery", "ip", "ipQ" commands
@Client.on_message(filters=filters.command(["ipuery", "ip", "ipQ"], prefixes=["/"]) & filters.text)
async def ipQuery(client, response):
    postdata = utils.get_postdata("ipQ") # Query the 2 ID postdata

    if not postdata:
        message = """Query data from any public IP address with:

/ipQ <ip>"""
        buttons = keymakers(["Query 1.1.1.1", "View API Documentation"],
                            ["ipQ-1.1.1.1", "WEB-https://ip-api.com/docs"], True)
        
        await response.reply(message, reply_markup=buttons)
    
    else:
        # Loader ticker
        sticker = await utils.loading_message(response, 1)
        try:
            responseAPI = requests.get(f"http://ip-api.com/json/{postdata}").json()
            message = json.dumps(responseAPI, indent=4)
            buttons = keymakers(["Query 2.2.2.2"],
                                ["ipQ-2.2.2.2"], True)
            
            # Deleting sticker
            await sticker.delete()
            
            await client.edit_message_text(
                text=message,
                message_id=response.id,
                chat_id=response.chat.id,
                reply_markup=buttons
            )

        except Exception as Error:

            # Deleting sticker
            await sticker.delete()

            buttons = keymakers(["Retry"],
                                [f"ipQ-{postdata}"], True)
            await response.reply(f"An error has ocurred! | {Error}", reply_markup=buttons)
        