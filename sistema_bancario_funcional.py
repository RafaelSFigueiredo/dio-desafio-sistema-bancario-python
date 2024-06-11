lista_usuarios = {}
lista_contas = {}

saldo_conta = 0.00
LIMITE = 500.00
NUMERO_MAXIMO_SAQUES = 3
contador_saques = 0
extrato_conta = 11 * "=" + " EXTRATO " + 11 * "=" + "\n"

menu = """
[u]\tCadastrar Usuário
[c]\tCriar Conta Corrente
[s]\tSaque
[d]\tDepósito
[e]\tExtrato
[q]\tEncerrar o atendimento

"""


# FUNÇÃO SAQUE
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if numero_saques < limite_saques:

        limite_excedido = valor > limite

        saldo_excedido = valor > saldo

        saque_negativo = valor < 0

        if limite_excedido:
            print(f"Operação recusada. Seu limite de saque é de R$ {LIMITE:.2f} por operação.")
        elif saldo_excedido:
            print("Operação recusada. Você não pode sacar uma quantia superior ao seu saldo.")
        elif saque_negativo:
            print(f"Operação recusada. Valor sacado deve ser positivo.")
        else:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}"
            numero_saques += 1

    else:
        print(f"Operação recusada. Número máximo de {limite_saques} saques diários foi atingido.")

    return saldo, extrato


# FUNÇÃO DEPÓSITO
def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}"
    else:
        print("Operação recusada. Valor depositado deve ser positivo.")

    return saldo, extrato


# FUNÇÃO EXTRATO
def exibe_extrato(saldo, /, *, extrato):

    print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n" + 31 * "=" + "\n")


# FUNÇÃO CADASTRAR
def cadastrar_usuario(registro):
    cpf = input("CPF: ")

    if cpf not in registro.keys():
        nome = input("Nome: ")
        nascimento = input("Data de Nascimento: ")
        endereco = input("Endereço Completo: ")

        registro.update({cpf: {"nome_usuario": nome, "nascimento_usuario": nascimento, "endereco_usuario": endereco}})

    else:
        print("Operação recusada. CPF já cadastrado.")


# FUNÇÃO CRIAR CONTA CORRENTE
def criar_conta(registro_usuarios, registro_contas):

    if len(registro_usuarios.keys()) == 0:
        print("Operação recusada. Não há usuários cadastrados.")

    else:
        cpf_usuario = input("Informe o CPF do usuário: ")

        if cpf_usuario not in registro_usuarios.keys():
            print("Operação recusada. CPF não cadastrado no sistema.")

        else:
            nome_do_usuario = registro_usuarios[cpf_usuario]["nome_usuario"]

            numero_de_contas = len(registro_contas.values())
            numero_da_conta = str(numero_de_contas + 1)
            registro_contas.update({numero_da_conta: {"agencia": "0001", "usuario": nome_do_usuario}})


# LOOP DE FUNCIONAMENTO DO SISTEMA
while True:
    operacao = input(menu)

    # Cadastro de usuário
    if operacao == "u":
        cadastrar_usuario(lista_usuarios)

    # Criar uma conta
    elif operacao == "c":
        criar_conta(lista_usuarios, lista_contas)

    # Saque
    elif operacao == "s":
        valor_saque = float(input("Insira o valor a ser sacado: R$ "))

        saldo_conta, extrato_conta = saque(saldo=saldo_conta, valor=valor_saque, extrato=extrato_conta, limite=LIMITE,
                                           numero_saques=contador_saques, limite_saques=NUMERO_MAXIMO_SAQUES)

    # Depósito
    elif operacao == "d":
        valor_deposito = float(input("Insira valor a ser depositado: R$ "))

        saldo_conta, extrato_conta = deposito(saldo_conta, valor_deposito, extrato_conta)

    # Extrato
    elif operacao == "e":
        exibe_extrato(saldo_conta, extrato=extrato_conta)

    # Encerrar o atendimento
    elif operacao == "q":
        print("Agradecemos pela sua preferência. Tenha um ótimo dia!")
        break

    # Mensagem de comando inválido
    else:
        print("Comando inválido. Por favor, leia as opções novamente e escolha uma operação.")
