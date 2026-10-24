from time import sleep
peso = float(input('Digite seu peso: (Kg)'))
altura = float(input('Digite sua altura: (m)'))
alt = altura/100
imc = peso / (alt * alt)

print('-=' *15)
print('CALCULANDO SEU IMC ... ' )
print('-=' *15)
sleep(3)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} e você está ABAIXO do peso.')
elif imc < 25:
    print(f'Seu IMC é de {imc:.2f} e seu peso é IDEAL.')
elif imc < 30:
    print(f'Seu IMC é de {imc:.2f} e você está com SOBREPESO.')
elif imc < 40:
    print(f'Seu IMC é de {imc:.2f} e você está com OBESIDADE.')
else:
    print(f'Seu IMC é de {imc:.2f} e você está com OBESIDADE MÓRBIDA.')

