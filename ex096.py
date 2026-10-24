from random import randint
from time import sleep

print('=-'*15 , 'JOGO DA ADIVINHAÇÃO', '=-'*15)
print()
pc = randint(1,10)
tent = 1
jogador = int(input('Vou pensar em um número de 1 a 10, tente adivinhar!  '))
sleep(1)
print()
while jogador != pc:
    jogador = int(input('Você errou, tente outra vez! '))
    tent += 1
print(f'Você acertou na {tent}° tentativa, O número que eu pensei foi {pc}.')