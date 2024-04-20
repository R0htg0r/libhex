# Python 3.8.7
# Desenvolvido: 18/08/2022

import re
import json
import requests

# libhex

NavPXR = requests.Session()
NavPXR.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"})
NavPXR.cookies.update({"PHPSESSID": memoria().token}) # Altere(Change)

class hacker:
    def __init__(sessao): sessao.Ox001 = []; sessao.Ox003 = NavPXR.post("https://hackerwars.io/ajax.php", data={"func": "getStatic"})
    def nome(sessao): return json.loads(re.search(r"\[(\S*)\]", sessao.Ox003.json()["msg"]).group(1))["user"] if("user" in sessao.Ox003.text) else "Nenhum"
    def ip(sessao): return json.loads(re.search(r"\[(\S*)\]", sessao.Ox003.json()["msg"]).group(1))["ip"] if("ip" in sessao.Ox003.text) else "Nenhum"
    def rp(sessao): return json.loads(re.search(r"\[(\S*)\]", sessao.Ox003.json()["msg"]).group(1))["reputation"] if("reputation" in sessao.Ox003.text) else "Nenhum"
    def rk(sessao): return json.loads(re.search(r"\[(\S*)\]", sessao.Ox003.json()["msg"]).group(1))["rank"] if("rank" in sessao.Ox003.text) else "Nenhum"

class bitcoins:
    def __init__(sessao):
        sessao.Ox001 = []
        sessao.Ox002 = 0
        sessao.Ox003 = NavPXR.post("https://hackerwars.io/internet?redirect=btc")
        sessao.Ox004 = NavPXR.post("https://hackerwars.io/finances")

    def publico(sessao):
        if("ip-data" in sessao.Ox003.cookies):
            for Ox005 in sessao.Ox003.text.split():
                if(sessao.Ox002 == 511 or sessao.Ox002 == 532):
                    sessao.Ox001.append(re.search(r"\"(\S*)\"", Ox005).group(1))
                sessao.Ox002 += 1
            sessao.Ox002 = 0
            return sessao.Ox001[0]
        else: return "Nenhum"

    def privado(sessao):
        if("ip-data" in sessao.Ox003.cookies):
            if(len(sessao.Ox001) >= 2): return sessao.Ox001[1]
            else:
                for Ox005 in sessao.Ox003.text.split():
                    if(sessao.Ox002 == 511 or sessao.Ox002 == 532):
                        sessao.Ox001.append(re.search(r"\"(\S*)\"", Ox005).group(1))
                    sessao.Ox002 += 1
                sessao.Ox002 = 0
                return sessao.Ox001[1]
        else: return "Nenhum"
    
    def satoshi(sessao):
        if("ip-data" in sessao.Ox003.cookies):
            if(re.search("Carteira Bitcoin", sessao.Ox004.text)):
                try:
                    return re.search(r"> (\S*) BTC<", sessao.Ox004.text).group(1)
                except Exception as e:
                    print("Ocorreu um erro", e)
        else: return "Nenhum"
