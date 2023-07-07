import httpx
from bs4 import BeautifulSoup

# get

requisicao = httpx.get("https://mundoeducacao.uol.com.br/geografia/estados-brasil.htm")
texto = requisicao.content
soup = BeautifulSoup(texto, "html.parser")
link_estados = []

for link in soup.find_all('a'):
    get_link = link.get('href')
    link_estados.append(get_link)

# print(link_estados[100])

lista_teste = []

for c in range(100, 127):
    link_2 = link_estados[c]
    lista_teste.append(link_2)
# print(lista_teste)

for estados in lista_teste:
    teste = httpx.get("{}".format(estados))
    teste2 = teste.content
    soup2 = BeautifulSoup(teste2, "html.parser")
    print(soup2.title)
    teste3 = soup2.get_text()

    # Região
    regiao = teste3.find('Região:')
    regiao2 = regiao + 20
    regiao3 = teste3[regiao:regiao2]
    print(regiao3.strip())

    # Capital
    capital = teste3.find('Capital:')
    print(capital)
    capital2 = capital + 20
    capital3 = teste3[capital:capital2]
    print(capital3.strip())

    # População
    populacao = teste3.find('População:')
    populacao2 = populacao + 25
    populacao3 = teste3[populacao:populacao2]
    print(populacao3.strip())

