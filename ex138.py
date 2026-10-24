# Sorteando Mega-Sena - aula 88 CeV
from time import sleep
from random import randint
lista = []
jogos = []
print('-=' *30)
print('                     JOGO DA MEGA-SENA')
print('-=' *30)
print()
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print()
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('=-'*3, f'SORTEANDO {quantidade} JOGOS', '=-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('=-' * 6, '< BOA SORTE >', '=-' * 6)

