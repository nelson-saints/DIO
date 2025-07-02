import textwrap

def menu():
    menu = """\n
    =========================== MENU ===========================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato):
    if valor> 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\nOperação falhou! O valor informado é inválido!!!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n### Operação falhou! Você não tem saldo suficiente. ###")

    elif excedeu_limite:
        print("\n### Operação falhou! O valor do saque excede o limite. ###")

    elif excedeu_saques:
        print("\n### Operação falhou! Número máximo de saques excedido. ###")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

while True:
    
    opcao = menu()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 's':
        valor  = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
    elif opcao == 'e':
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'q':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")