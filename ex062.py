nome = input('Digite seu nome: ') .strip()
lista = nome.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {lista[0]}.')
print(f'Seu ultimo nome é {lista[len(lista)-1]}')
