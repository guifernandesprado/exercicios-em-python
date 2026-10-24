email = input('Digite seu email: ')

if '@' and '.' in email:
    print('Email válido.')
else:
    print('Email inválido.')