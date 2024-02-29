import re

def is_ip(data):
    return re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', data)

def consultar(tech):
    l = ["google.com", "google.com", "google.com"]
    return l


def consultarIP(ip):
    return {"ip": ip}
    return DATA_IP

if __name__ == "__main__":
    print (consultarIP("1.1.1.1"))