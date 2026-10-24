galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]  #exemplo 1
for p in galera:                                             # como montar uma tabela com vários dados
    print(f'{p[0]} tem {p[1]} anos de idade')

galera = []     # exemplo 2
dado = []       #coloca todos os dados na lista dado, dentro da lista galera
maior = menor = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:    #aqui dá pra descobrir quem é maior de idade
    if p[1]> 21:
        print(f'{p[0]} é maior de idade. ')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        menor += 1
print(f'No total, temos {maior} pessoas maiores e {menor} menores de idade.')
