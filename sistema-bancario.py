menu = '''
    Seja Bem vindo ao TecBanc
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
        valor_int = valor
        if valor_int > 0:
            saldo += valor_int
            print(f'Seu saldo atual é de R${saldo:.2f}')
        else:
            print('Valor inválido')
    elif opcao == "S" or opcao == "s":
        saque = int(input('Digite o valor que deseja sacar:'))
        if saque <= saldo and numero_saques < LIMITE_SAQUES and saque < limite:
            print ('Saque realizado com sucesso')
            saldo -= saque
            numero_saques += 1
            print(f'Segue seu saldo atualiado: R${saldo:.2f}')
            print(f'Você fez {numero_saques} saques')
        elif saldo < saque:
            print('Saldo insuficiente')
        elif numero_saques == LIMITE_SAQUES:
            print('Limite de saques diários atingido')
        else:
            print('Valor de saque inválido')
    elif opcao == 'E' or opcao == 'e':
        extrato = saldo
        print(f'Seu saldo é de R${extrato:.2f}')
        print(f'Sua quantidade de Saques é de {numero_saques}')
        print(f'Seu limite de saque é de R${limite:.2f}')
    elif opcao == 'Q' or opcao == 'q':
        break
    else:
        print('Opção inválida, por favor, selecione uma das opções listadas no menu')