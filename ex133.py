from random import randint

times = ('Corinthians','Palmeiras','São Paulo','Flamengo','Grêmio','Cruzeiro')

pos1 = randint(0, 5)
pos2 = randint(0, 5)

while pos1 == pos2:
    pos1 = randint(0, 5)
    pos2 = randint(0, 5)

print(f'Jogo: {times[pos1]} x {times[pos2]}')
print(f'Três primeiros: {times[0:3]}')
print(f'Dois últimos: {times[-2:]}')


