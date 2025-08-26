import variaveis

def deposito():
    valor1 = input('Digite o valor do depósito: ')
    try:
        valor1_float = float(valor1)
        print(f'Depósito de {valor1_float} realizado com sucesso!')
        variaveis.saldo += valor1_float
        variaveis.lista_depositos.append(valor1_float)
    except ValueError:
        print('Valor inválido. Por favor, digite um número válido.')