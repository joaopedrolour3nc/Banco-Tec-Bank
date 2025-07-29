saldo = 0
lista_depositos = []
def extrato():
    global saldo
    print('Exibindo extrato...')
    print(f"Saldo atual: {saldo}")
    print("Depósitos realizados:")
    for deposito in lista_depositos:
        print(f" - {deposito}")
    if not lista_depositos:
        print("Nenhum depósito realizado ainda.")
def deposito():
    global saldo
    valor1 = input('Digite o valor do depósito: ')
    try:
        valor1_float = float(valor1)
        print(f'Depósito de {valor1_float} realizado com sucesso!')
        saldo += valor1_float
        lista_depositos.append(valor1_float)
    except ValueError:
        print('Valor inválido. Por favor, digite um número válido.')
def saque():
    global saldo
    valor_saque = input('Digite o valor do saque: ')
    try:
        valor_saque_float = float(valor_saque)
        if valor_saque_float > saldo:
            print('Saldo insuficiente para saque.')
        else:
            print(f'Saque de {valor_saque_float} realizado com sucesso!')
            saldo -= valor_saque_float
    except ValueError:
        print('Valor inválido. Por favor, digite um número válido.')
while True:
    entrada = input('Digite o que deseja fazer: 1- Extrato, 2-Deposito e 3-Saque: ')

    if entrada == '1':
        extrato()
    elif entrada == '2':
        deposito()
    elif entrada == '3':
        saque()
    else:
        print('Operação inválida, tente novamente')
        continue
