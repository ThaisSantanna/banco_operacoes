saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def deposito(valor):
    global saldo

    saldo += valor
    print(f'Depósito de R${valor:.2f} realizado com sucesso.')
    print(f'Seu saldo atual é R${saldo:.2f}')


def saque(valor):
    global saldo, numero_saques, LIMITE_SAQUES

    if numero_saques < LIMITE_SAQUES:

        if valor <= limite and valor <= saldo:
            saldo -= valor
            numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            print(f"Seu Saldo atual é R${saldo:.2f}")

        elif valor > limite:
            print(f"Seu limite de saque é R${limite:.2f} por saque.")

        else:
            print("Saldo insuficiente.")
    else:
        print("Limite de saques mensais atingido")


def extrato():
    global saldo

    print(f"Seu Saldo atual é R${saldo:.2f}")
    print(f"Você realizou {numero_saques} de {LIMITE_SAQUES} esse mês")
    print(f"Seu limite de Saque é de R${limite:.2f}")


def main():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>"""

    while True:

        opcao = input(menu)

        if opcao == "d":

            print("Depósito")
            valor = float(input("Digite o valor do depósito: "))
            deposito(valor)

        elif opcao == "s":
            print("Sacar")
            valor = float(input("Digite o valor do saque: "))
            saque(valor)

        elif opcao == "e":

            print("Extrato")
            extrato()

        elif opcao == "q":

            print("Obrigado por utilizar nossos serviços.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")


if __name__ == "__main__":
    main()
