import argparse
from moduls.utils import utils
from pyrogram import Client
import base64, sys

if __name__ == "__main__":
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

    # Clear the terminal
    utils.clear_terminal()

    # PRINT THE BANNER
    utils.anim(base64.b64decode(f"""CiBfX19fXyBfX19fXyBfICAgICAgICAgICAgICAgCnxfICAgX3wgICBfX3wgfF8gX19fIF9fXyBfX18gCiAgfCB8IHwgIHwgIHwgLiB8IC4nfF8gLXwgLV98CiAgfF98IHxfX19fX3xfX198X18sfF9fX3xfX198CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB4cGxvaXRMYWJz""").decode("utf-8"))

    print ()

    # LOADING JSON CONFIG
    utils.animINFO("Loading the json config.")

    try:
        # Importing the config data for start the bot
        config = utils.load_json()

    except Exception as Error:
        utils.animERROR("An error has been occurred!")
        print (Error)
        sys.exit()
    else:
        utils.animDONE("Config loaded successfully.")

    # LOADING JSON CONFIG
    utils.animINFO("Setting the config data.")

    try:
        # Set the config data
        bot = Client(
            config["name"],
            api_id=config["api_id"],
            api_hash=config["api_hash"],
            bot_token=config["bot_token"],
            plugins=dict(root=config["dir_plugins"])
        )

    except Exception as Error:
        utils.animERROR("An error has been occurred!")
        print (Error)
        sys.exit()
    else:
        utils.animDONE("Config data has been set successfully.")

    # TURNING ON THE BOT
    utils.animINFO("Turning on the bot.")

    try:
        utils.animINFO(f"THE BOT IS ON!, You can use in: {config['url']}")
        bot.run()
    except Exception as Error:
        utils.animERROR("An error has been occurred!")
        print (Error)
        sys.exit()