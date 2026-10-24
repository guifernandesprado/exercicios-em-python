num = cont = total = 0

while True:
    num = int(input('Digite um número: [999 PARA PARAR] '))
    if num == 999:
        break
    cont += 1
    total += num

print(f'Foram didgitados {cont} números e a soma dele é {total}.')