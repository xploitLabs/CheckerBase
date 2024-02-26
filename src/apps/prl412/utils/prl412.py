import requests
from bs4 import BeautifulSoup
import random

def consultar(tech):
    DICTY = []
    limit = 200
    
    URL = f"https://www.shodan.io/search/facet?query=http.component:{tech}&facet=domain"

    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": '"gzip", "deflate", "br"',
        "Accept-Language": "es-US,es-419;q=0.9,es;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Referer": URL,
        "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    data = f"query=http.component:{tech}&facet=domain"
    response = requests.get(URL, headers=header, data=data)

    soup = BeautifulSoup(response.text, "lxml")
    caja = soup.find_all("div", class_="four columns name", limit=limit)
    conteo = soup.find_all("div", class_="one column value", limit=limit)
    for counter, (container_data, container_amount) in enumerate(zip(caja, conteo)):
        counter += 1
        data = container_data.find("strong").get_text()
        amount = container_amount.get_text()
        DICTY.append(data)
    
    l = random.sample(DICTY, 3)
    return l


def consultarIP(ip):
    def eliminar_claves_test(diccionario):
        if isinstance(diccionario, dict):
            return {k: eliminar_claves_test(v) for k, v in diccionario.items() if "shodan" not in k}
        elif isinstance(diccionario, list):
            return [eliminar_claves_test(item) for item in diccionario]
        else:
            return diccionario

    import shodan
    API = shodan.Shodan("7gxwzNcslcrcMcZQvjiV67LlR45fViiV")
    DATA_IP = eliminar_claves_test(API.host(ip))
    return DATA_IP

if __name__ == "__main__":
    print (consultarIP("1.1.1.1"))