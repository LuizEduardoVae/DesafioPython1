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

menu_principal = """

[c] Criar Conta
[v] Ver contas
[q] Sair

=> """


# Variaveis Globais

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

rua = ''
numero_casa = ''
bairro_casa = ''
cidade_casa = ''

usuarios = {}

nome = ''
data_nascimento = ''
cpf = ''


# 


def cadastrar_endereco(rua, numero_casa, bairro_casa, cidade_casa):
    rua = str(input("Rua: "))
    numero_casa = str(input("Numero: "))
    bairro_casa = str(input("Bairro: "))
    cidade_casa = str(input("Cidade: "))

    endereco = {
        "logradouro": rua,
        "numero": numero_casa,
        "bairro": bairro_casa,
        "cidade": cidade_casa
    }
    
    return endereco

def string_so_numeros(cpf):
    for char in cpf:
        if not char.isdigit():
            return False, cpf
    return True, cpf

def criar_usuario(nome,data_nascimeneto,cpf):
    nome = str(input("Nome: "))
    data_nascimento = str(input("Data de Nascimento: "))
    cpf = str(input("CPF: "))

    endereco = cadastrar_endereco(rua, numero_casa, bairro_casa, cidade_casa)
    cpf_validado = string_so_numeros(cpf)

    if cpf_validado[0]:
        print("CPF validado")
        cpf = cpf_validado[1]

    else:
        print("CPF inválido")
        print("Crie uma conta Novamente")


criar_usuario()



def sacar(*, saque, numero_saques, saldo, extrato):
    
    if saque > saldo:
        print("\nSaldo Insuficiente")
    elif saque > limite:
        print("\nLimite Insuficiente")
    elif numero_saques >= LIMITE_SAQUES:
        print("""\nQuantidade de saques diários atingidos
                  \nSelecione outra opção!
             """)
    else:
        saldo -= saque
        numero_saques += 1
        extrato.append(f"Saque: {saque}")

    return saldo, numero_saques

def despositar(deposito,saldo,extrato,/):

    saldo += deposito
    extrato.append(f"Depósito: {deposito}")

    return saldo

        
def extrato_bancario(saldo,/,*,extrato):
    for movimentacao in extrato:
            print(movimentacao)

    print("\nSaldo Final:")
    print(saldo)






while True:

    opcao1 = input(menu_principal)

    if opcao1 == "c":
         while True:
                print( " \nDeseja criar uma conta?")
                yes_no = input(sim_nao)

                if yes_no == "y":
                    criar_usuario
                    
                else:
                    break

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