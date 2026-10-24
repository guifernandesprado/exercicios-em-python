geral = []
positivos = []
negativos = []
soma_positivo = quant_zero = 0

for c in range(6):
    num = int(input('Digite um número: '))
    geral.append(num)
    if num > 0:
        positivos.append(num)
        soma_positivo += num
    elif num < 0:
        negativos.append(num)
    else:
        quant_zero += 1

print(f'Números digitados: {geral}')
print(f'Números positivos digitados: {positivos}')
print(f'Números negativos digitados: {negativos}')
print(f'Soma do total de números positivos: {soma_positivo}')
print(f'Quantidade de vezes em que o número 0 foi digitado: {quant_zero}')