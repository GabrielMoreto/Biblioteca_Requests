# Biblioteca Requests
 
Requests é uma biblioteca da linguagem python muito utilizada para fazer iterações com API´s, e para fazer requisições, requisições nada mais são do que
trocas de informações entre um cliente e um servidor.
Normalmente a troca de informações feita de um site para o outro é feita no formato "json", e o formato json nada mais é do que um dicionário.

Para saber mais sobre os tipos de requisição acesse [Tipos de requisição].

[Tipos de requisição]: https://github.com/GabrielMoreto/Biblioteca_Requests/blob/702b882dc1e7b47b86211ac5c78a042da56b3e05/Metodos_http.md


# Importando biblioteca

Antes de qualquer coisa você deve importar a biblioteca requests utilizando o código abaixo:

```
import requests
```

`Observação`

Nestes exemplos eu utilizei o Firebase, que é um banco de dados do google, e o firebase exige que você utilize um ",json" ao final dos links.

> função get()

Serve para pegar informações.
Para utilizar o metódo GET em python siga o exemplo do código abaixo:

```
requisicao = requests.get("https://teste-d52c9-default-rtdb.firebaseio.com/.json")
print(requisicao) 
print(requisicao.json())
```

O resultado será:

```
<Response [200]>
None
```
O código de resposta "200" significa que está ok, que deu certo, porém ainda não tenho nenhum valor no meu banco de dados, por isso a 
saída para o comando "print(requisicao.json())" é igual a "None".

> função post()

Serve para criar informações.
Para utilizar o metódo POST em python siga o exemplo do código abaixo:

```
informacoes = '{"Nome": "Mateus"}'
requisicao = requests.post("https://teste-d52c9-default-rtdb.firebaseio.com/.json", data=informacoes)
print(requisicao) # se você não fornecer nenhum valor irá gerar o erro 400
print(requisicao.json())
```

O resultado será:

```
<Response [200]>
{'name': '-NZTuRCwsBJb9bm67z91'}
```
Novamente o código "200" significa que está ok, ao acessar o banco de dados eu posso ver que novas informações foram criadas.

> função patch()

Serve para editar informações.
Para utilizar o metódo PATCH em python siga o exemplo do código abaixo:

```
informacoes = '{"Nome": "Gabriel", "Sobrenome" : "Mozelli Moreto", "Idade": "22"}'
requisicao = requests.patch("https://teste-d52c9-default-rtdb.firebaseio.com/-NZTglKAvw7HlEgYrg_M.json", data=informacoes)
print(requisicao) # se você não fornecer nenhum valor irá gerar o erro 400
print(requisicao.json())
```
O resultado será: 

```
<Response [200]>
{'Nome': 'Gabriel', 'Sobrenome': 'Mozelli Moreto', 'Idade': '22'}
```
Ao acessar o banco de dados posso observar que o sobrenome foi alterado.

> função delete()

Serve para apagar informações.
Para utilizar o metódo DELETE em python siga o exemplo do código abaixo:

```
requisicao = requests.delete("https://teste-d52c9-default-rtdb.firebaseio.com/-NZTuRCwsBJb9bm67z91.json")
print(requisicao) 
print(requisicao.json())
```

O resultado será:

```
<Response [200]>
None
```

Ao acessar o banco de dados posso ver que não existe mais nenhuma informação.


# Códigos de resposta

Como resposta as requisições posso ter os seguintes códigos:

`200` 

Que significa que está tudo ok.

`400` 

Que significa que houve algum erro.