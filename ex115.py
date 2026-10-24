# Exercício 72 CeV
lista = ('zero', 'Um', 'Dois', 'Três','Quatro',
          'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
              'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número de 0 a 20: '))
while num < 0 or  num > 20 :
    num = int(input('Número inválido. Tente novamente de 0 a 20. '))

print(f'Você digitou o número {lista[num]}')