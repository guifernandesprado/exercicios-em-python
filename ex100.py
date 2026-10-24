# Vídeo-aula 62 CeV

print('')
print('     Rerador de Progressão Aritmética')
print('-=' *20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
print('')
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais 
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais= int(input('quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
print('')