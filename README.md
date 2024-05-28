def deposito(saldo, valor):
    if valor > 0:
        saldo += valor
        print("Depósito de R$%.2f realizado com sucesso." % valor)
    else:
        print("Valor de depósito inválido.")
    return saldo

def saque(saldo, saques_totais, valor):
    if saques_totais > 0:
        if valor > 0 and valor <= 500:
            if saldo >= valor:
                saldo -= valor
                saques_totais -= 1
                print("Saque de R$%.2f realizado com sucesso." % valor)
            else:
                print("Saldo insuficiente para realizar a operação saque.")
        else:
            print("Valor de saque inválido, seu limite é R$ 500,00/dia.")
    else:
        print("Limite diário de saques atingido.")
    return saldo, saques_totais

def extrato(saldo):
    print("Saldo atual: R$%.2f" % saldo)


def main():
    saldo = 0
    saques_totais = 3

    while True:
        operacao = input("Digite a operação desejada (Depósito / Saque / Extrato / Sair): ").capitalize()

        if operacao == "Depósito":
            valor = float(input("Digite o valor do depósito: "))
            saldo = deposito(saldo, valor)
        elif operacao == "Saque":
            valor = float(input("Digite o valor do saque: "))
            saldo, saques_totais = saque(saldo, saques_totais, valor)
        elif operacao == "Extrato":
            extrato(saldo)
        elif operacao == "Sair":
            print("Obrigado por utilizar nossos serviços, o banco agradece ;)")
            break
        else:
            print("Operação inválida.")

if __name__ == "__main__":
    main()
