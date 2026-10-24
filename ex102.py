# Vídeo-aula 64 CeV
num = 0
cont = -1
total = -999

while num != 999:
    num = int(input('digite um número [999 para parar]: '))
    cont += 1 
    total += num


print(f'Você digitou {cont} números e a soma entre ele foi {total}.')