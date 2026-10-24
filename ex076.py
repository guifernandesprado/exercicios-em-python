from datetime import date

nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print(f'O atleta tem {idade} anos. Classificação: MIRIM')
elif idade <=14:
    print(f'O atleta tem {idade} anos. Classificação: INFANTIL')
elif idade <=19:
    print(f'O atleta tem {idade} anos. Classificação: JUNIOR')
elif idade <=25:
    print(f'O atleta tem {idade} anos. Classificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos. Classificação: MASTER')