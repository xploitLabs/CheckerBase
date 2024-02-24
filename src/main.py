import sys, time
import argparse
from moduls.utils import utils
from pyrogram import Client

# Controlador de parámetros
parser = argparse.ArgumentParser(description="Una plantilla que permite interactuar con la API de Telegram para el desarrollo de bots de telegram.")
parser.add_argument("-d", help="Activar el modo debug.", action="store_true")
parser.add_argument("--name", help="Establecer el nombre al bot.")
parser.add_argument("--mention", help="Establecer un username de mención al bot.")
parser.add_argument("--url", help="Establecer una URL de contacto del bot.")
parser.add_argument("--api_id", help="Establecer el API ID del bot.")
parser.add_argument("--api_hash", help="Establecer el API HASH del bot.")
parser.add_argument("--bot_token", help="Establecer el token del bot.")
parser.add_argument("--dir_apps", help="Establecer el nombre de la carpeta que contiene todas las aplicaciones del bot. (default: apps)")
args = parser.parse_args()

if __name__ == "__main__":
    utils.clear_terminal()

    # Importing the config data for start the bot
    config = utils.load_json()

    # Establecer configuración del bot
    bot = Client(
        config["name"],
        api_id=config["api_id"],
        api_hash=config["api_hash"],
        bot_token=config["bot_token"],
        plugins=dict(root=config["dir_plugins"])
    )
    bot.run()

    # Starting the bot
#    try:
#    except AttributeError:
#        print ("Necesitas indicar una key válida.")