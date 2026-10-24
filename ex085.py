num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
if total == 2 :
    print(f'\n\033[mO número {num} é primo!')
else:
    print(f'\n\033[mO número {num} não é primo.')