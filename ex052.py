idade = int(input('Idade: '))

if idade < 12:
   classificacao = 'Criança'
elif idade < 18:
   classificacao = 'Adolescente'
elif idade < 60:
   classificacao = 'Adulto'
else:
   classificacao = 'Idoso'

print(f'Classificação: {classificacao}')

if idade >= 16:
   print('Pode votar: Sim')
else:
   print('Pode votar: Não')

if idade >= 65:
   print('Pode se aposentar: Sim')
else:
   print('Pode se aposentar: Não')