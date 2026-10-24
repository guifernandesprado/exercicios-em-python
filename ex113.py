# Exercício 71 CeV

print('=' * 30)
print('{:^30}'.format('BANCO CeV'))
print('=' * 30)
valor = int(input('Quanto dinheiro você quer sacar? R$'))
total = valor
nota = 50
cont_nota = 0
while True:
    if total >= nota:
        total -= nota
        cont_nota += 1
    else:
        if cont_nota > 0:
            print(f'Total de {cont_nota} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
           nota = 10
        elif nota == 10:
            nota = 1
        cont_nota = 0
        if total == 0:
            break
print('=' * 30)
print('OBRIGADO, VOLTE SEMPRE!')
