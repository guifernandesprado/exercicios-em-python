lanche = 'Hamburger','Suco','Pizza','Pudim'

print = (len(lanche)) # o len mostra o tamanho da string, tupla, lista ou dicionário

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}°')
# 1 - cria um contador com a tupla


for c in lanche:
    print(c)
# 2 -maneira mais simples de mostrar a tupla

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}°')
# 3 - faz o mesmo que o 1

print(sorted(lanche))
# 4 mostra a tupla em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# 5 - junta as tuplas, sem somar, apenas uma na frente da outra

print(c.count(5)) # o count mostra quantas vezes o número escolhido aparece

print(c.index(8)) # o index mostra em que posição o número escolhido aparece

pessoa = ('Gustavo', 39, 'M', 99.88) # nas tuplas, podemos colocar números e letras juntas
print(pessoa)