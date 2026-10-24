todos = []
pares = []
impares = []

for c in range(7):
    num = int(input(f'Digite o {c+1}º número: '))
    todos.append(num)
    if num % 2 ==0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Lista de todos os números digitados: {todos}')
print(f'Lista dos números pares digitados: {pares}')
print(f'Lista dos números ímpares digitados: {impares}')