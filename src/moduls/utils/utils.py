import os, json, pickle, random, sys, time

# VAR
DIRPOSTSAVED = "moduls/postdata/postdataSaved.pkl"

def getX(): 
    if os.path.exists(DIRPOSTSAVED):
        file = open(DIRPOSTSAVED, "rb")
        content = pickle.load(file)
        return content
    return {}

def saveVAR(var):
    code = genCode()
    diccionario = getX()
    diccionario[code] = var
    file = open(DIRPOSTSAVED, "wb")
    pickle.dump(diccionario, file)
    return code

def getVAR(code, delete=True):
    try:
        diccionario = getX()
        data = diccionario.get(code, None)
        if delete:
            del diccionario[code]
            file = open(DIRPOSTSAVED, "wb")
            pickle.dump(diccionario, file)
        return data
    except KeyError:
        return None

def genCode(length=7):
    return "VAR:"+''.join(random.choices('0123456789ABCDEF', k=length))

    
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

def load_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dir_principal = os.path.abspath(os.path.join(current_dir, '..', '..'))
    route = os.path.join(dir_principal, 'config', 'config.json')
    with open(route) as archivo_config:
        config = json.load(archivo_config)    
    return config

def save_api_key(api_key):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")
    with open(config_path, "w") as config_file:
        json.dump({"api_key": api_key}, config_file)    

async def save_img_fromTG(client, message):
    file_path = await client.download_media(message)
    return file_path

async def loading_message(message, sticker_id=0):
    """Stickers pack for the loading effect
* 0: Loading focus -> default
* 1: Whell
* 2: Cloud uploading
* 3: Files
* 4: Cocodrile
* 5: Linear"""
    LISTA_STICKERS = [
        "CAACAgUAAxkBAAIH6GTnnz50bOkZeI6bg0-Y31I1behoAAKcAAPIlGQUc48AAfPaxYX8MAQ",
        "CAACAgUAAxkBAAEK7VNlc6q3USwPWTu3e6V4JJliYesHzQACmgADyJRkFCxl4eFc7yVqMwQ",
        "CAACAgUAAxkBAAEK7VVlc6uex00WmBRBkOwatwjCOuG-VAACpQADyJRkFHhDhV4BRbZGMwQ",
        "CAACAgUAAxkBAAEK7Vdlc6vebcbOXztVGwyVtPG8rOFjZwACpwADyJRkFGCmdrVn5RydMwQ", 
        "CAACAgIAAxkBAAN2ZdKS5UetFdo704o6sHi5_daCDGQAAjgLAAJO5JlLMrFH0tlPjNAeBA",
        "CAACAgUAAxkBAAPfZdKvwArlZE4TkkymoGmuQ9lK3wQAAqEAA8iUZBTlOvHR3aRelx4E"
    ]
    message_f = await message.reply_sticker(LISTA_STICKERS[sticker_id])
    return message_f

# -- TEXT OUTPUTS --

# --- ANIMATION
def animINFO(s):
    """An function for animate INFO DATA in the console
* s: The text that will be animated"""
    s = f"{colors.BLUE}[{colors.WHITE}INFO{colors.BLUE}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def animDONE(s):
    """An function for animate SUCCESS DATA in the console
* s: The text that will be animated"""
    s = f"{colors.GREEN}[{colors.WHITE}DONE{colors.GREEN}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)


def animERROR(s):
    """An function for animate ERROR DATA in the console
* s: The text that will be animated"""
    s = f"{colors.RED}[{colors.WHITE}ERROR{colors.RED}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def animDEBUG(s):
    """An function for animate DEBUG DATA in the console
* s: The text that will be animated"""
    s = f"{colors.MAGENTA}[{colors.WHITE}DEBUG{colors.MAGENTA}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def anim(s):
    """An function for animate text in the console
* s: The text that will be animated"""
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

# -- END TEXT OUTPUTS --



if __name__ == "__main__":
    import colors
    animINFO("System turn ON")
    animDONE("The message has been sent successfully")
    animERROR("An error has been occurred")
    animDEBUG("User registered - 972378")
    anim("Hello world")

else:
    from moduls.utils import colors