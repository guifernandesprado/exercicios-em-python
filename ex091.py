par = 0
impar = 0
somapar = 0
somaimpar = 0
for c in range(5):
    num = int(input(f'Digite o {c+1}° número: '))
    if num % 2 == 0:
        par += 1
        somapar += num
    else:
        impar +=1
        somaimpar += num
if par > 0:
    mediapar =  somapar / par
else:
    mediapar = 0
if impar > 0:
    mediaimpar = somaimpar / impar
else:
    mediaimpar =  0


print(f'Você digitou {par} números pares e {impar} números ímpares.')
print(f'A soma de todos os números pares é de {somapar}.')
print(f'A soma de todos os números ímpares é de {somaimpar}.')
print(f'A média dos números pares é de {mediapar:.1f}.')
print(f'A média dos números ímpares é de {mediaimpar:.1f}.')