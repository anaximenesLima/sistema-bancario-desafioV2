import textwrap

def menu():
    menu = """\n
    ################ MENU ###########################
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo Usuario
    [q] Sair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
     if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:0.2f}\n"
        print("\nDeposito realizado com ssucesso!!")
     else:
        print("\nOpçao falhou! valor informado é invalido.")

     return saldo, extrato   

def sacar(*, saldo, valor, extrato, limite, numero_saques ,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("\nOperacao falhou! saldo insulficiente.")
    elif excedeu_limite:
        print("\nOperacao falhou: Limite para saque exedido.")
    elif excedeu_saques:
        print("\nOperacao falhou: Número máximo de saque exedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:0.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!!!")
    else:
        print("\nOperação falhou valor informado é inválido.")

def exibir_extrato(saldo, *, extrato):
     print("\n############### EXTRATO ################")
     print("Não foram realizadas movimentação." if not extrato else extrato)
     print(f"\nSando: {saldo:0.2f}")
     print("###########################################")


    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500.00
    extrato = ""
    numero_saques = 0
    usuaros = []
    contas = []
    


    while(True):
        opcao = menu()
        if opcao == "d":
            valor = float(input("Ddigite o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
           
        elif opcao == "s":
            valor = float(input("Ddigite o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES, 
            )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
           
        elif opcao == "q":
            break
        else:
            print("Operacao invalida, por favor selecione uma opçao")

main()