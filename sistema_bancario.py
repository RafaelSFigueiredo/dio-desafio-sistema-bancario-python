saldo = 0
contador_saques = 0

menu = """
Digite [s] para Saque
Digite [d] para Depósito
Digite [e] para Extrato
Digite [q] para Encerrar o atendimento

"""

while True:

    operacao = input(menu)

    if operacao == "s":

        if contador_saques < 3:

            valor_saque = float(input("Insira o valor a ser sacado: R$ "))

            if valor_saque <= 500.00:
                saldo -= valor_saque
                print(f"Seu novo saldo: R$ {saldo:.2f}")
                contador_saques += 1
            else:
                print(f"Operação recusada. Saques estão limitados a R$ 500.00 por operação.")

        else:
            print("Você atingiu o número máximo de 3 saques diários.")

    # Depósito
    elif operacao == "d":

        valor_deposito = float(input("Insira valor a ser depositado: R$ "))
        saldo += valor_deposito
        print(f"Seu novo saldo: R$ {saldo:.2f}")

    # Extrato
    elif operacao == "e":

        print(f"Seu saldo: R$ = {saldo:.2f}")

    # Encerrar o atendimento
    elif operacao == "q":
        break
