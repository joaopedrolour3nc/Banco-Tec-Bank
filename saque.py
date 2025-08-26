import variaveis

def saque():
    valor_saque = input('Digite o valor do saque: ')
    try:
        valor_saque_float = float(valor_saque)
        if valor_saque_float > variaveis.saldo:
            print('Saldo insuficiente para saque.')
        else:
            print(f'Saque de {valor_saque_float} realizado com sucesso!')
            variaveis.saldo -= valor_saque_float
            variaveis.lista_saques.append(valor_saque_float)
    except ValueError:
        print('Valor inválido. Por favor, digite um número válido.')