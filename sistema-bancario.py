menu = '''
    Seja Bem vindo ao TecBank
    [D] para Depositar
    [S] para Sacar
    [E] para Estrato da Conta
    [Q] para Sair
'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:
   
    opcao = input(menu)

    if opcao == 'D' or opcao == 'd':
        valor = int(input('Digite o valor para Depósito: '))
        if valor > 0:
            saldo += valor
            print(f'Seu saldo atual é de R${saldo:.2f}')
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Valor inválido')
    elif opcao == "S" or opcao == "s":
        saque = int(input('Digite o valor que deseja sacar:'))
        if saque <= saldo and numero_saques < LIMITE_SAQUES and saque < limite:
            print ('Saque realizado com sucesso')
            print(f'\nSaque: R${valor:.2f}')
            saldo -= saque
            numero_saques += 1
            print(f'Você fez {numero_saques} saques')
            extrato += f'Saque: R$ {saque:.2f}\n'
            print(f'Segue seu saldo atualiado: R${saldo:.2f}')
        elif saldo < saque:
            print('Saldo insuficiente')
        elif numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingido')
        else:
            print('Valor de saque inválido')
    elif opcao == 'E' or opcao == 'e':
        print('================ EXTRATO ==============')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        # print(f'Seu saldo é de R${saldo:.2f}')
        print(f'Sua quantidade de Saques é de {numero_saques}')
        print(f'Seu limite de saque é de R${limite:.2f}')
        print('======================================')
    elif opcao == 'Q' or opcao == 'q':
        break
    else:
        print('Opção inválida, por favor, selecione uma das opções listadas no menu')