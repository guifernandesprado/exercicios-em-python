agenda = []
while True:
    print('')
    print('''[1] Adicionar contato 
[2] Ver contatos
[3] Remover contatos
[4] Sair''')
    print('')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        contato = str(input('Nome: ')).title().strip()
        if contato not in agenda:
            print('Contato adicionado')
            agenda.append(contato)
        else:
            print('Esse contato já existe!')
    elif opcao == 2:
        if len(agenda)< 1:
            print('Agenda vazia...')
        else:
            print('Contatos: ')
            for i in agenda:
                print(i)
    elif opcao == 3:
        remover = str(input('Nome: ')).title().strip()
        if remover not in agenda:
            print('Contato não encontrado.')
        else:
            agenda.remove(remover)
            print('Contato removido.')
    elif opcao == 4:
        print('Até logo...')
        break
    else:
        print('Opção inválida!')
