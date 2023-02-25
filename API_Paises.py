import requests
import json
import sys

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

def contagem_de_paises():
    resposta = requisicao(URL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def lista_pais(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_name, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        for pais in lista_de_paises:
            print("{}:{} habitantes".format(pais["name"], pais["population"]))
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
        print("País nao encontrado")

def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("é preciso passar o nome do país.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('   ____          __  __ _      \n  / __ \___  ___/ /_/ /(_)___ _\n / /_/ / _ \/ _  / __/ / / __ `/\n/ _, _/  __/  __/ /_/ / / /_/ / \n\/ |_|\___/\___/\__/_/_/\__, /  \n                        /_/   \n                       \n  Bem-vindo ao sistema!\n\n')
        print("uso: python API_Paises <acao> <nome do pais>")
        print("acoes disponiveis: contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            print(contagem_de_paises())

        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)

        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("argumento invalido")
