frutas = ['maçã' , 'banana' , 'pera' , 'uva' , 'manga']

for fruta in frutas:
    print(fruta)

print('=-'*30)

frutas.append('morango')
frutas.pop(0)

for fruta in frutas:
    print(fruta)