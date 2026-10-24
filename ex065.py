from random import randint
from time import sleep

pc = randint(0,5)
num = int(input('Pensei em um número de 0 a 5, tente adivinhar: '))

sleep(3)

if pc == num:
    print(f'PARABÉNS!Você acertou o número {num}!!!')
else:
    print(f'VOCÊ PERDEU! Eu escolhi o número {pc}.')
