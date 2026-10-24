# Vídeo-aula 61 CeV
print('')
print('     Rerador de Progreção Aritmética')
print('-=' *20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
print('')
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    cont += 1
print('FIM')
print('')