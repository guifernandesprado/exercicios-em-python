from datetime import date
maior = 0
menor = 0

for c in range(1,8):
    ano = int(input(f'Em que ano nasceu a {c}° pessoa? '))
    hoje = date.today().year
    idade = hoje - ano
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo, {maior} pessoas são maiores de idade.')
print(f'E também, {menor} pessoas são menores de idade.')

