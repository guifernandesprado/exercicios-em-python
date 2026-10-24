numeros = [1, 23, 8, -4, 9, 12, -13, 22]

num_par = 0
num_neg = 0
total = 0

for num in numeros:
    if num % 2 == 0:
        num_par += num
    if num < 0 :
        num_neg += num
    total += num

print(f'Todos os números pares: {num_par}')
print(f'Todos os números negativos: {num_neg}')
print(f'A soma de todos os números é {total}')