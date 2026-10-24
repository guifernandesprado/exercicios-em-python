nome = input('Digite seu nome completo: ').strip()
print('Analizando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')

print(f'Seu nome ao todo tem {len(nome)- nome.count(' ')} letras. ')

print(f'Seu primeiro nome tem {nome.find(' ')} letras.')