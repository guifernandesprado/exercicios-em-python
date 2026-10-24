lista = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break

lista.sort(reverse=True)

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não está na lista')