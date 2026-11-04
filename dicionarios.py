pessoas = {'nome': 'Guilherme', 'idade': '34', 'sexo': 'M'}
print(pessoas)       #declarando um dicionário básico
print(pessoas['nome']) #para mostrar apenas um item

#se eu quiser montar um print formatado, tem que ser assim, com aspas duplas
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

#para mostar as chaves - vai mostar 'nome','idade','sexo'
print(pessoas.keys())
#para mostar os valores - vai mostrar 'Guilherme','34','M'
print(pessoas.values())

# ultilizando um laço for, mostrando uma chave em cada linha, serve também para os values
for k in pessoas.keys():
    print(k)

# para mostar em laço for nome = guilherme, não dá pra usar enumerate em dicionários
for k, v in pessoas.items():
    print(f'{k} = {v}')

#posso mudar os valores de forma simples
pessoas['nome'] = 'Leandro'

#para adicionar alguma chave ou valor basta declarar, não precisa do append
pessoas['peso'] = 98.5

# criando um dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

# para fazer uma lista com um dicionário e percorrer com o laço for, na hora do append, preciso escrever .copy()
estado = {}
brasil = []
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy())