import variaveis

def extrato():
    
    print('Exibindo extrato...')
    print(f"Saldo atual: {variaveis.saldo}")
    print("Depósitos realizados:")
    for deposito in variaveis.lista_depositos:
        print(f" - {deposito}")
    for saque in variaveis.lista_saques:
        print(f" - {saque}")
    if not variaveis.lista_saques:
        print("Nenhum depósito realizado ainda.")