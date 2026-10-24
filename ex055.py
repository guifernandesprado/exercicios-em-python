cadastro = int(input('Quantas pessoas serão cadastradas: '))
lista = []
maiores = []

for pessoa in range(cadastro):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    lista.append(f'{nome} - {idade} anos')
    if idade >= 18:
        maiores.append(nome)

print(lista)
print(f'Maiores de idade: {len(maiores)}')
print(f'Nomes: {maiores}')
