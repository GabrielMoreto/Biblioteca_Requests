# Importa a biblioteca httpx para fazer requisições.
import httpx
# Importa a biblioteca BeautifulSoup para organizar as requisições feitas.
from bs4 import BeautifulSoup

# Realiza uma requisição do tipo GET no página principal para obter os Estados, suas siglas e o link de detalhes de cada estados.
requisicao = httpx.get("https://mundoeducacao.uol.com.br/geografia/estados-brasil.htm")
texto = requisicao.text
texto2 = texto[72968:79012]
soup = BeautifulSoup(texto2, "html.parser")
lista = []

# Realiza um loop for para colocar os estados e as siglas dentro de uma lista
for estado_sigla in soup.find_all('p'):
    nome_estado = estado_sigla.string
    lista.append(nome_estado)

# Cria duas novas listas para separar os estados e as siglas
lista_estados = []
lista_siglas = []

for estado in lista[2:55:2]:
    lista_estados.append(estado)

for sigla in lista[3:56:2]:
    lista_siglas.append(sigla)

# Cria uma lista para cada etsado para colocar os dados
lista_Acre = []
lista_Alagoas = []
lista_Amapa = []
lista_Amazonas = []
lista_Bahia = []
lista_Ceara = []
lista_Espirito_Santo = []
lista_Goias = []
lista_Maranhao = []
lista_Mato_Grosso = []
lista_Mato_Grosso_Sul = []
lista_Minas_Gerais = []
lista_Para = []
lista_Paraiba = []
lista_Parana = []
lista_Pernambuco = []
lista_Piaui = []
lista_Rio_Janeiro = []
lista_Rio_Grande_Norte = []
lista_Rio_Grande_Sul = []
lista_Rondonia = []
lista_Roraima = []
lista_Santa_Catarina = []
lista_Sao_Paulo = []
lista_Sergipe = []
lista_Tocantins = []
lista_Distrito_Federal = []
contador = 1

# Procura pelos links dos estados onde contém os detalhes
for link in soup.find_all('a'):
    link = link.get('href')
    requisicao_dados = httpx.get("{}".format(link))
    requisicao_dados = requisicao_dados.text
    find_dados = requisicao_dados.find("Dados gerais")
    requisicao_dados = requisicao_dados[find_dados:find_dados + 950]
    soup2 = BeautifulSoup(requisicao_dados, "html.parser")

    # Salva os detalhes na lista do respectivo estado
    for regiao in soup2.find_all('li'):
        if contador == 1:
            lista_Acre.append(regiao.get_text())
        elif contador == 2:
            lista_Alagoas.append(regiao.get_text())
        elif contador == 3:
            lista_Amapa.append(regiao.get_text())
        elif contador == 4:
            lista_Amazonas.append(regiao.get_text())
        elif contador == 5:
            lista_Bahia.append(regiao.get_text())
        elif contador == 6:
            lista_Ceara.append(regiao.get_text())
        elif contador == 7:
            lista_Espirito_Santo.append(regiao.get_text())
        elif contador == 8:
            lista_Goias.append(regiao.get_text())
        elif contador == 9:
            lista_Maranhao.append(regiao.get_text())
        elif contador == 10:
            lista_Mato_Grosso.append(regiao.get_text())
        elif contador == 11:
            lista_Mato_Grosso_Sul.append(regiao.get_text())
        elif contador == 12:
            lista_Minas_Gerais.append(regiao.get_text())
        elif contador == 13:
            lista_Para.append(regiao.get_text())
        elif contador == 14:
            lista_Paraiba.append(regiao.get_text())
        elif contador == 15:
            lista_Parana.append(regiao.get_text())
        elif contador == 16:
            lista_Pernambuco.append(regiao.get_text())
        elif contador == 17:
            lista_Piaui.append(regiao.get_text())
        elif contador == 18:
            lista_Rio_Janeiro.append(regiao.get_text())
        elif contador == 19:
            lista_Rio_Grande_Norte.append(regiao.get_text())
        elif contador == 20:
            lista_Rio_Grande_Sul.append(regiao.get_text())
        elif contador == 21:
            lista_Rondonia.append(regiao.get_text())
        elif contador == 22:
            lista_Roraima.append(regiao.get_text())
        elif contador == 23:
            lista_Santa_Catarina.append(regiao.get_text())
        elif contador == 24:
            lista_Sao_Paulo.append(regiao.get_text())
        elif contador == 25:
            lista_Sergipe.append(regiao.get_text())
        elif contador == 26:
            lista_Tocantins.append(regiao.get_text())
        elif contador == 27:
            lista_Distrito_Federal.append(regiao.get_text())
    contador += 1

# Cria um dicionario para cada estado
dic_Acre = {'Estado' : str(lista_estados[0]).strip(), 'Sigla' : str(lista_siglas[0]).strip(), 'Região' : str(lista_Acre[0])[8:-1].strip(), 'Capital' : str(lista_Acre[1])[9:-1].strip(), 'População' : str(lista_Acre[4])[11:-11].strip()}
dic_Alagoas = {'Estado' : str(lista_estados[1]).strip(), 'Sigla' : str(lista_siglas[1]).strip(), 'Região' : str(lista_Alagoas[0])[8:-1].strip(), 'Capital' : str(lista_Alagoas[1])[9:-1].strip(), 'População' : str(lista_Alagoas[3])[11:-46].strip()}
dic_Amapa = {'Estado' : str(lista_estados[2]).strip(), 'Sigla' : str(lista_siglas[2]).strip(), 'Região' : str(lista_Amapa[0])[8:-1].strip(), 'Capital' : str(lista_Amapa[1])[9:-1].strip(), 'População' : str(lista_Amapa[4])[11:-24].strip()}
dic_Amazonas = {'Estado' : str(lista_estados[3]).strip(), 'Sigla' : str(lista_siglas[3]).strip(), 'Região' : str(lista_Amazonas[0])[8:-1].strip(), 'Capital' : str(lista_Amazonas[1])[9:-1].strip(), 'População' : str(lista_Amazonas[4])[11:-25].strip()}
dic_Bahia = {'Estado' : str(lista_estados[4]).strip(), 'Sigla' : str(lista_siglas[4]).strip(), 'Região' : str(lista_Bahia[0])[8:-2].strip(), 'Capital' : str(lista_Bahia[1])[9:-2].strip(), 'População' : str(lista_Bahia[4])[11:-25].strip()}
dic_Ceara = {'Estado' : str(lista_estados[5]).strip(), 'Sigla' : str(lista_siglas[5]).strip(), 'Região' : str(lista_Ceara[0])[8:-1].strip(), 'Capital' : str(lista_Ceara[1])[9:-1].strip(), 'População' : str(lista_Ceara[4])[11:-25].strip()}
dic_Espirito_Santo = {'Estado' : str(lista_estados[6]).strip(), 'Sigla' : str(lista_siglas[6]).strip(), 'Região' : str(lista_Espirito_Santo[0])[8:-1].strip(), 'Capital' : str(lista_Espirito_Santo[1])[9:-1].strip(), 'População' : str(lista_Espirito_Santo[3])[11:-24].strip()}
dic_Goias = {'Estado' : str(lista_estados[7]).strip(), 'Sigla' : str(lista_siglas[7]).strip(), 'Região' : str(lista_Goias[0])[8:-1].strip(), 'Capital' : str(lista_Goias[1])[9:-1].strip(), 'População' : str(lista_Goias[3])[11:-24].strip()}
dic_Maranhao = {'Estado' : str(lista_estados[8]).strip(), 'Sigla' : str(lista_siglas[8]).strip(), 'Região' : str(lista_Maranhao[0])[8:-1].strip(), 'Capital' : str(lista_Maranhao[1])[9:-1].strip(), 'População' : str(lista_Maranhao[4])[11:-24].strip()}
dic_Mato_Grosso = {'Estado' : str(lista_estados[9]).strip(), 'Sigla' : str(lista_siglas[9]).strip(), 'Região' : str(lista_Mato_Grosso[0])[8:-1].strip(), 'Capital' : str(lista_Mato_Grosso[1])[9:-1].strip(), 'População' : str(lista_Mato_Grosso[4])[11:-24].strip()}
dic_Mato_Grosso_Sul = {'Estado' : str(lista_estados[10]).strip(), 'Sigla' : str(lista_siglas[10]).strip(), 'Região' : str(lista_Mato_Grosso_Sul[0])[8:].strip(), 'Capital' : str(lista_Mato_Grosso_Sul[1])[9:].strip(), 'População' : str(lista_Mato_Grosso_Sul[3])[11:-24].strip()}
dic_Minas_Gerais = {'Estado' : str(lista_estados[11]).strip(), 'Sigla' : str(lista_siglas[11]).strip(), 'Região' : str(lista_Minas_Gerais[0])[8:-2].strip(), 'Capital' : str(lista_Minas_Gerais[1])[9:-2].strip(), 'População' : str(lista_Minas_Gerais[4])[11:-25].strip()}
dic_Para = {'Estado' : str(lista_estados[12]).strip(), 'Sigla' : str(lista_siglas[12]).strip(), 'Região' : str(lista_Para[0])[8:].strip(), 'Capital' : str(lista_Para[1])[9:].strip(), 'População' : str(lista_Para[3])[11:-24].strip()}
dic_Paraiba = {'Estado' : str(lista_estados[13]).strip(), 'Sigla' : str(lista_siglas[13]).strip(), 'Região' : str(lista_Paraiba[0])[8:-1].strip(), 'Capital' : str(lista_Paraiba[1])[9:-1].strip(), 'População' : str(lista_Paraiba[3])[11:-25].strip()}
dic_Parana = {'Estado' : str(lista_estados[14]).strip(), 'Sigla' : str(lista_siglas[14]).strip(), 'Região' : str(lista_Parana[0])[8:-1].strip(), 'Capital' : str(lista_Parana[1])[9:-1].strip(), 'População' : str(lista_Parana[3])[10:-25].strip()}
dic_Pernambuco = {'Estado' : str(lista_estados[15]).strip(), 'Sigla' : str(lista_siglas[15]).strip(), 'Região' : str(lista_Pernambuco[0])[8:].strip(), 'Capital' : str(lista_Pernambuco[1])[9:].strip(), 'População' : str(lista_Pernambuco[4])[11:-23].strip()}
dic_Piaui = {'Estado' : str(lista_estados[16]).strip(), 'Sigla' : str(lista_siglas[16]).strip(), 'Região' : str(lista_Piaui[0])[8:-1].strip(), 'Capital' : str(lista_Piaui[1])[9:-1].strip(), 'População' : str(lista_Piaui[4])[11:-25].strip()}
dic_Rio_Janeiro = {'Estado' : str(lista_estados[17]).strip(), 'Sigla' : str(lista_siglas[17]).strip(), 'Região' : str(lista_Rio_Janeiro[0])[8:-1].strip(), 'Capital' : str(lista_Rio_Janeiro[1])[9:-1].strip(), 'População' : str(lista_Rio_Janeiro[4])[11:-25].strip()}
dic_Rio_Grande_Norte = {'Estado' : str(lista_estados[18]).strip(), 'Sigla' : str(lista_siglas[18]).strip(), 'Região' : str(lista_Rio_Grande_Norte[0])[8:].strip(), 'Capital' : str(lista_Rio_Grande_Norte[1])[9:].strip(), 'População' : str(lista_Rio_Grande_Norte[3])[11:-23].strip()}
dic_Rio_Grande_Sul = {'Estado' : str(lista_estados[19]).strip(), 'Sigla' : str(lista_siglas[19]).strip(), 'Região' : str(lista_Rio_Grande_Sul[0])[8:-1].strip(), 'Capital' : str(lista_Rio_Grande_Sul[1])[9:-1].strip(), 'População' : str(lista_Rio_Grande_Sul[3])[11:-35].strip()}
dic_Rondonia = {'Estado' : str(lista_estados[20]).strip(), 'Sigla' : str(lista_siglas[20]).strip(), 'Região' : str(lista_Rondonia[0])[8:].strip(), 'Capital' : str(lista_Rondonia[1])[9:].strip(), 'População' : str(lista_Rondonia[4])[11:-23].strip()}
dic_Roraima = {'Estado' : str(lista_estados[21]).strip(), 'Sigla' : str(lista_siglas[21]).strip(), 'Região' : str(lista_Roraima[0])[8:].strip(), 'Capital' : str(lista_Roraima[1])[9:].strip(), 'População' : str(lista_Roraima[4])[11:-23].strip()}
dic_Santa_Catarina = {'Estado' : str(lista_estados[22]).strip(), 'Sigla' : str(lista_siglas[22]).strip(), 'Região' : str(lista_Santa_Catarina[0])[8:-1].strip(), 'Capital' : str(lista_Santa_Catarina[1])[1:-1].strip(), 'População' : str(lista_Santa_Catarina[4])[11:-25].strip()}
dic_Sao_Paulo = {'Estado' : str(lista_estados[23]).strip(), 'Sigla' : str(lista_siglas[23]).strip(), 'Região' : str(lista_Sao_Paulo[0])[8:-1].strip(), 'Capital' : str(lista_Sao_Paulo[1])[9:-1].strip(), 'População' : str(lista_Sao_Paulo[3])[11:-25].strip()}
dic_Sergipe = {'Estado' : str(lista_estados[24]).strip(), 'Sigla' : str(lista_siglas[24]).strip(), 'Região' : str(lista_Sergipe[0])[8:-1].strip(), 'Capital' : str(lista_Sergipe[1])[9:-1].strip(), 'População' : str(lista_Sergipe[4])[11:-25].strip()}
dic_Tocantins = {'Estado' : str(lista_estados[25]).strip(), 'Sigla' : str(lista_siglas[25]).strip(), 'Região' : str(lista_Tocantins[0])[14:-1].strip(), 'Capital' : str(lista_Tocantins[1])[9:-1].strip(), 'População' : str(lista_Tocantins[4])[11:-34].strip()}
dic_Distrito_Federal = {'Estado' : str(lista_estados[26]).strip(), 'Sigla' : str(lista_siglas[26]).strip(), 'Região' : str(lista_Distrito_Federal[0])[8:-1].strip(), 'Capital' : str(lista_Distrito_Federal[1])[9:-1].strip(), 'População' : str(lista_Distrito_Federal[3])[11:-25].strip()}

lista_geral = []
lista_geral.append(dic_Acre)
lista_geral.append(dic_Alagoas)
lista_geral.append(dic_Amapa)
lista_geral.append(dic_Amazonas)
lista_geral.append(dic_Bahia)
lista_geral.append(dic_Ceara)
lista_geral.append(dic_Espirito_Santo)
lista_geral.append(dic_Goias)
lista_geral.append(dic_Maranhao)
lista_geral.append(dic_Mato_Grosso)
lista_geral.append(dic_Mato_Grosso_Sul)
lista_geral.append(dic_Minas_Gerais)
lista_geral.append(dic_Para)
lista_geral.append(dic_Paraiba)
lista_geral.append(dic_Parana)
lista_geral.append(dic_Pernambuco)
lista_geral.append(dic_Piaui)
lista_geral.append(dic_Rio_Janeiro)
lista_geral.append(dic_Rio_Grande_Norte)
lista_geral.append(dic_Rio_Grande_Sul)
lista_geral.append(dic_Rondonia)
lista_geral.append(dic_Roraima)
lista_geral.append(dic_Santa_Catarina)
lista_geral.append(dic_Sao_Paulo)
lista_geral.append(dic_Sergipe)
lista_geral.append(dic_Tocantins)
lista_geral.append(dic_Distrito_Federal)
print(lista_geral)