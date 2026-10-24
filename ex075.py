nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua média foi de {media:.1f}. PARABÉNS, VOCÊ FOI APROVADO!')
elif media >= 5:
    print(f'Sua média foi de {media:.1f}. VOCÊ ESTÁ DE RECUPERAÇÃO!')
else:
    print(f'Sua média foi de {media:.1f}. VOCÊ FOI REPROVADO!')