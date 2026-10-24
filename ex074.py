from datetime import date

atual = date.today().year
nascimento = int(input('Em que ano você nasceu: '))
idade = atual - nascimento

if idade <= 17:
    saldo = 18-idade
    print(f'Você tem {idade} anos, e deverá se alistar daqui {saldo} anos.')
    print(f'Seu alistamento será em {atual + saldo}.')
elif idade == 18:
    print(f'Você tem {idade} anos. Você deve se alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    print(f'Você tem {idade} anos. Você deveria ter se alistado á {idade - 18} anos atrás.')
    print(f'Seu alistamento foi em {atual - saldo}.')



