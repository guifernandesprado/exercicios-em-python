velocidade = int(input('Qual a velocidade do seu carro? '))
multa = (velocidade - 80) * 7
if velocidade < 80:
    print('Velocidade permitida, tenha um bom dia!')
else:
    print(f'Velocidade excedida! Você será multado em R${multa:.2f}.')