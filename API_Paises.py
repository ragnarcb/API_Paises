import requests
import json


URL = "https://restcountries.com/v2/all"
URL_name = "https://restcountries.com/v2/name/"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
            print("1")
    except:
        print("erro", url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print("erro pars")

def contagem_de_paises(lista_de_paises):
    return len(lista_de_paises)

def lista_pais(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_name, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        for pais in lista_de_paises:
            print("{}:{}".format(pais["name"], pais["population"]))
    else:
        print("Pais nao encontrado")

def mostrar_moedas(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_name, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        for pais in lista_de_paises:
            print("moedas do,", pais["name"])
            moedas = pais['currencies']
            for moeda in moedas:
                print("{} - {}".format(moeda["name"], moeda["code"]))

    else:
        print("Pais nao encontrado")
if __name__ == "__main__":
    print('   ____          __  __ _      \n  / __ \___  ___/ /_/ /(_)___ _\n / /_/ / _ \/ _  / __/ / / __ `/\n/ _, _/  __/  __/ /_/ / / /_/ / \n\/ |_|\___/\___/\__/_/_/\__, /  \n                        /_/   \n                       \n  Bem-vindo ao sistema!\n\n')

    #mostrar_populacao("unated states")
    mostrar_moedas("bra")