import deposito, extrato, saque, variaveis, sair

while True:
    entrada = input('Digite o que deseja fazer: 1- Extrato, 2-Deposito,3-Saque ou sair: ')

    if entrada == '1':
        extrato.extrato()
    elif entrada == '2':
        deposito.deposito()
    elif entrada == '3':
        saque.saque()
    elif entrada.lower() == 'sair':
        sair.sair()
    else:
        print('Operação inválida, tente novamente')
        continue
