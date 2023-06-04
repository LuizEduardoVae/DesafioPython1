while True:

        opcao = input(menu)
        
        if opcao == "d":
            while True:
                print( " \nDeseja depositar?")
                yes_no = input(sim_nao)

                if yes_no == "y":
                    deposito = float(input("Valor do deposito:  "))
                    saldo = despositar(deposito,saldo,extrato)
                    
                else:
                    break

        elif opcao == "s":
                
                while True:
                    print( "\nDeseja Sacar?")
                    yes_no = input(sim_nao)
                    saque = 0
                    
                    if yes_no == "y":
                        saque = float(input("Valor do saque:  "))
                        saldo, numero_saques = sacar(saque=saque, numero_saques=numero_saques, saldo=saldo,extrato=extrato)
                    else:
                        break


        elif opcao == "e":
            while True:
                    print( "\n======== Deseja ver o Extrato? ========")
                    yes_no = input(sim_nao)
                    
                    if yes_no == "y":
                        print("\n======== Extrato ========")
                        extrato_bancario(saldo, extrato=extrato)
                    else:
                        break
        

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")