import requests

# GET
# requisicao = requests.get("https://teste-d52c9-default-rtdb.firebaseio.com/.json")
# print(requisicao) 
# print(requisicao.json())

# POST
# informacoes = '{"Nome": "Mateus"}'

# requisicao = requests.post("https://teste-d52c9-default-rtdb.firebaseio.com/.json", data=informacoes)
# print(requisicao) # se você não fornecer nenhum valor irá gerar o erro 400
# print(requisicao.json())

# PATCH
# informacoes = '{"Nome": "Mateus", "Sobrenome" : "Mateus", "Idade": "22"}'

# requisicao = requests.patch("https://teste-d52c9-default-rtdb.firebaseio.com/-NZTglKAvw7HlEgYrg_M.json", data=informacoes)
# print(requisicao) # se você não fornecer nenhum valor irá gerar o erro 400
# print(requisicao.json())


# Delete
# requisicao = requests.delete("https://teste-d52c9-default-rtdb.firebaseio.com/-NZTglKAvw7HlEgYrg_M.json")
# print(requisicao) 
# print(requisicao.json())