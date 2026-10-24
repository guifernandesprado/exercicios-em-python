# listas são mutáveis
lista = [1,2,3,4]
lista[2] = 5    #mudei o 3 pelo 5
print(lista)

# para adicionar um índice a lista, usar o .append
lista.append(6) # adicionei o número 6, que vai entrar em último lugar na lista
print(lista)

# se eu quiser adicionar alguma coisa e escolher o índice, usar o .insert
lista.insert(1,7) # adicionei o número 7 na posição 1, logo após o número 1
print(lista) 

# para apagar um item na lista, temos algumas opções:
del lista[1] #apaguei escolhendo o índice da lista
lista.pop(0) #outra forma de apagar escolhendo o índice
lista.remove(3) # dessa forma, você não escolhe o índice, mas sim o conteúdo de dentro da lista, nesse caso, o número 3
print(lista)

# para colocar a lista em ordem, usar o .sort
valores = [9,2,6,8,7,3,5]
valores.sort()
valores.sort(reverse=True) # aqui ele faz em ordem, mas de trás pra frente
print(valores)

# para ver o tamanho da lista, usar o len
len(lista)

lista_de_nomes = []  #para adicionar nomes ao uma lista.. nesse caso usei o laço for, mas o método é o mesmo para os outros
for c in range(5):
    nome = str(input('Digite seu nome: '))
    lista_de_nomes.append(nome)

# exercício do professor Guanabara

valores = []
valores.append(5)    # mostra os valores enumerados e separados por linha e por posição 
valores.append(9)
valores.append(4)
for c, v in enumerate (valores):
    print(f'Na posição {c} encontrei o número {v}')
print('Fim da lista!')

valores = []
for c in range(5):
    valores.append(int(input('Digite um valor: '))) #usa o laço range para adicionar valores na lista
for c, v in enumerate (valores):
    print(f'Na posição {c} encontrei o número {v}')
print('Fim da lista!')

# para copiar uma lista sem criar ligação entre elas
a = [1,2,3,4]
b = a[:]
b[2] = 8
print(f'Lista A = {a}') # alterei os números de cada lista, sem ligação entre elas
print(f'Lista B = {b}')