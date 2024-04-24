saldo = 0.00
LIMITE = 500.00
NUMERO_MAXIMO_SAQUES = 3
contador_saques = 0
extrato = 11*"=" + " EXTRATO " + 11*"=" + "\n"

menu = """
Digite [s] para Saque
Digite [d] para Depósito
Digite [e] para Extrato
Digite [q] para Encerrar o atendimento

"""

while True:
    operacao = input(menu)

    if operacao == "s":

        if contador_saques < NUMERO_MAXIMO_SAQUES:

            valor_saque = float(input("Insira o valor a ser sacado: R$ "))

            limite_excedido = valor_saque > LIMITE

            saldo_excedido = valor_saque > saldo

            saque_negativo = valor_saque < 0
            
            if limite_excedido:
                print(f"Operação recusada. Seu limite de saque é de R$ {LIMITE:.2f} por operação.")
            elif saldo_excedido:
                print("Operação recusada. Você não pode sacar uma quantia superior ao seu saldo.")
            elif saque_negativo:
                print(f"Operação recusada. Valor sacado deve ser positivo.")
            else:
                saldo -= valor_saque
                extrato += f"\nSaque: R$ {valor_saque:.2f}"
                contador_saques += 1
        
        else:
            print(f"Operação recusada. Número máximo de {NUMERO_MAXIMO_SAQUES} saques diários foi atingido.")

    # Depósito
    elif operacao == "d":
        valor_deposito = float(input("Insira valor a ser depositado: R$ "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\nDepósito: R$ {valor_deposito:.2f}"
        else:
            print("Operação recusada. Valor depositado deve ser positivo.")

    # Extrato
    elif operacao == "e":
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n" + 31*"=" + "\n")

    # Encerrar o atendimento
    elif operacao == "q":
        print("Agradecemos pela sua preferência. Tenha um ótimo dia!")
        break

    # Mensagem de comando inválido
    else:
        print("Comando inválido. Por favor, leia as opções novamente e escolha uma operação.")
