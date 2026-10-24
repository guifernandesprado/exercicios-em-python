print('=-' * 30)
print('')
print('         LEITOR DE TEMPERATURA°')
print('')
print('=-' * 30)
print('')

resposta = 'S'

maior = menor = cont= total = media = 0

while resposta in 'Ss':
    temp = float(input('Digite a temperatura: '))
    cont += 1
    total += temp
    if cont == 1:
        maior = menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = total/cont

print(f'Ao todo, {cont} temperaturas foram registradas.')
print(f'A média das temperaturas é de {media:.1f}.')
print(f'A maior temperatura resgistrada foi {maior}° e a menor foi {menor}°.')