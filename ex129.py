lista = []
for c in range(5):
    num = int(input('Digite um valor: ' ))
    if c == 0 or num > lista[-1]:                        #se o contador for igual a 0, ele adicona normalmente na lista
        lista.append(num)               #e se o numero foi maior que o último numero da lista, ele vai para o final dela
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):                           #essa é a parte mais complicada e vale a pena estudar sobre ela
            if num <= lista[pos]:                         # colocamos a variável 0 na posição iinicial
                lista.insert(pos, num)                    # percorro toda a lista comparando os números
                print(f'Adicionado na posição {pos}...')  # adiciono ela de acordo com a posição e valor numérico
                break
            pos += 1

print(f'Os valores digitados em ordem foram: {lista}')