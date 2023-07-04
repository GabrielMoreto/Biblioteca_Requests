import requests

# # get()
requisicao = requests.get("https://teste-d52c9-default-rtdb.firebaseio.com/.json")
print(requisicao) 
print(requisicao.json())

# post()
informacoes = '{"Nome": "Gabriel", "Sobrenome" : "Moreto", "Idade": "22"}'
requisicao = requests.post("https://teste-d52c9-default-rtdb.firebaseio.com/.json", data=informacoes)
print(requisicao) # se você não fornecer nenhum valor irá gerar o erro 400
print(requisicao.json())

# patch()
informacoes = '{"Nome": "Gabriel", "Sobrenome" : "Mozelli Moreto", "Idade": "22"}'
requisicao = requests.patch("https://teste-d52c9-default-rtdb.firebaseio.com/-NZTuRCwsBJb9bm67z91.json", data=informacoes)
print(requisicao) # se você não fornecer nenhum valor irá gerar o erro 400
print(requisicao.json())

# delete()
requisicao = requests.delete("https://teste-d52c9-default-rtdb.firebaseio.com/-NZTuRCwsBJb9bm67z91.json")
print(requisicao) 
print(requisicao.json())