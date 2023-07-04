# Importando a biblioteca requests
import requests

# Método GET, requisição para pegar informações

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print(requisicao) # Se a resposta "response" for 200 significa que deu tudo certo, mas se for 404, significa que não deu certo.

# Normalmente a troca de informações feita de um site para o outro é feita no formato "json", e o formato jason nada mais é do que um dicionário

print(requisicao.json())
