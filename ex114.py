# exercício 72 CeV
from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1,10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e a máquina {computador}. Total de {total}.', end='')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1 :
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break

    print('Vamos jogar novamente...')
    print('')
print(f'Você venceu {vitoria} vezes.')