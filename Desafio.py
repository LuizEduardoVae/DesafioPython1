menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

sim_nao = """

[y] Sim
[n] Nao

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        while True:
            print( " \n Deseja depositar?")
            yes_no = input(sim_nao)

            if yes_no == "y":
                deposito = int(input("Valor do deposito:  "))
                saldo += deposito
            else:
                break

    elif opcao == "s":
         while True:
            
    elif opcao == "e":
        print(saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")