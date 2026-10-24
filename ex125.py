lista_a = []
lista_b = []
comuns = []
print('Primeira lista')
for c in range(5):
    num = int(input('Digite um número: '))
    lista_a.append(num)
print('Segunda lista')
for c in range(5):
    num = int(input('Digite um número: '))
    lista_b.append(num)
for num in lista_a:
    if num in lista_b and num not in comuns:
        comuns.append(num)

print(f'Números digitados na primeira lista: {lista_a}')
print(f'Números digitados na segunda lista: {lista_b}')
if len(comuns) > 0:
    print(f'Números que aparecem nas duas listas: {comuns}')
else:
    print('Nenhum valor em comum encontrado.')