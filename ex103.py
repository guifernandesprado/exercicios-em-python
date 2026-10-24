# Vídeo-aula 65 CeV

total = cont = media = maior = menor = 0
resposta = 'S'
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    total += num
    cont += 1
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor:
            menor = num
media = total/cont
print(f'Você digitou {cont} números.')
print(f'A média entre eles foi de {media}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
print('FIM.')