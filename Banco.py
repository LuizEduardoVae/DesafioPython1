from validate_docbr import CPF


# Variaveis Globais

usuarios = []

# Funcoes de validacao 

def validacao_numero(numero_casa):
    if not numero_casa.isdigit():
        return False
    return True

# Funcoes Usuario 

def cadastrar_endereco():
    rua = input("Rua: ")
    numero_casa = input("Número: ")
    bairro_casa = input("Bairro: ")
    cidade_casa = input("Cidade: ")

    numero_valido = validacao_numero(numero_casa)

    if numero_valido:
        endereco = {
            "Rua": rua,
            "Numero da Residencia": numero_casa,
            "Bairro": bairro_casa,
            "Cidade": cidade_casa
        }

        return endereco
    
    else:
        print("\nNúmero da casa inválido")
        return None
    
def criar_usuario(usuarios):
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")

    cpf_validator = CPF()
    if cpf_validator.validate(cpf):
        print("\nCPF válido.")

        for usuario in usuarios.values():
            if usuario["CPF"] == cpf:
                print("\nCPF já cadastrado.")
                return None


        print("\nVamos Cadastrar o seu endereco: ")
        endereco = cadastrar_endereco()

        if endereco is not None:
            dados_usuarios = {
                "CPF": cpf,
                "Nome": nome,
                "Data de Nascimento": data_nascimento,
                "Endereco": endereco
            }

            usuarios[cpf] = dados_usuarios
            
            usuarios.update({cpf: dados_usuarios})

            return usuarios
        else:
            print("\nNao foi possivel cadastrar endereco")
    else:
        print("CPF inválido.")
        return None
    

def login_usuario(usuarios):
    login_usuario = input("Digite o CPF da sua conta: ")

    for usuario in usuarios.values():
        if usuario["CPF"] == login_usuario:
            print("\nLogin feito com sucesso! ")
            return usuario

    print("CPF não encontrado no nosso banco de dados! ")
    return None



# Funcoes da Conta
contas = {}
def criar_conta(usuario, agencia):
    saldo = 0

    numero_da_conta = str(len(contas) + 1)

    conta_dados = {
        "Agencia": agencia,
        "Conta": numero_da_conta,
        "Saldo": saldo,
        "Extrato": [],
        "Usuario": usuario["CPF"],
        "NumeroSaquesDiarios": 0, # Adicionando o contador de saques diários
        "LimiteSaquesDiarios": 3,
        "LimiteValor": 500
    }


    contas.update({numero_da_conta: conta_dados})
    
    return contas




def login_contas(usuario, contas, numero_conta, saldo, agencia):
    print("Veja suas contas: ")

    for numero_conta, dados_conta in contas.items():
        if dados_conta["Usuario"] == usuario["CPF"]:
            print(f"Conta: {agencia}{numero_conta}")
            print(f"Saldo: R$ {dados_conta['Saldo']}")
            print("----\n")

    numero_conta = input("Digite o número da sua conta: ")

    for conta in contas.values():
        if conta["Conta"] == numero_conta and conta["Usuario"] == usuario["CPF"]:
            print(f"\nLogin na conta {agencia}{numero_conta} feito com sucesso! ")
            return conta

    print("\nConta não encontrada.")
    return None
   


#  Funcoes de movimentacao

def depositar(deposito,saldo,extrato,/):

    saldo += deposito
    extrato.append(f"Depósito: {deposito}")

    return saldo


    
def sacar(*, saldo, valor, extrato, conta):
    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato

    elif valor > conta["LimiteValor"]:
        print("Limite de saque excedido.")
        return saldo, extrato

    elif conta["NumeroSaquesDiarios"] >= conta["LimiteSaquesDiarios"]:
        print("Limite de saques diários atingido.")
        return saldo, extrato

    else:
        saldo -= valor
        conta["NumeroSaquesDiarios"] += 1  # Atualizando o contador de saques diários
        extrato.append(f"Saque: {valor}")
        return saldo, extrato



        
def extrato_bancario(saldo,/,*,extrato):
    print("Extrato:")
    for movimentacao in extrato:
        print(movimentacao)

    print("\nSaldo Final:")
    print(saldo)

    

def main():
    

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    contas = {}
    numero_conta = 0
    agencia = "0001/"

    usuarios = {}

    senha_adm = "Senha123"

    while True:
        print("\n# # # # # # # # # # # # # # Menus do Sistema  # # # # # # # # # # # # # #")
        print("[1] Criar Usuario")
        print("[2] Acessar Usuario")
        print("[3] Sair")

        opcao = input("=> ")

        if opcao == "1":
            criar_usuario(usuarios=usuarios)
        elif opcao == "2":
            usuario_selecionado = login_usuario(usuarios=usuarios)
            if usuario_selecionado:
                print(f"\nBem-vindo(a), {usuario_selecionado['Nome']}!")
                conta_selecionada = {}

                while True:
                    print(f"\n# # # # # # # # # # # # # # Bem Vindo(a), {usuario_selecionado['Nome']}  # # # # # # # # # # # # # #")
                    print("[1] Criar conta")
                    print("[2] Acessar conta")
                    print("[3] Sair")

                    opcao1 = input("=> ")

                    if opcao1 == "1":
                        contas = criar_conta(usuario_selecionado,agencia)

                    elif opcao1 == "2":
                        if usuario_selecionado is None:
                            print("Faça login primeiro.")
                        else:
                            conta_selecionada = login_contas(usuario_selecionado, contas, numero_conta, saldo, agencia)
                            if conta_selecionada is None:
                                print("teste2")
                            else:
                                while True:
                                    print(f"\n# # # # # # # # # # # # # # {agencia}{conta_selecionada['Conta']}  # # # # # # # # # # # # # #")
                                    print("[1] Depositar")
                                    print("[2] Sacar")
                                    print("[3] Ver Extrato")
                                    print("[4] Voltar")

                                    opcao2 = input("=> ")

                                    if opcao2 == "1":
                                        valor_deposito = float(input("Digite o valor do depósito: "))
                                        conta_selecionada['Saldo'] = depositar(valor_deposito, conta_selecionada['Saldo'], conta_selecionada['Extrato'])
                                        print("Depósito realizado com sucesso!")

                                    elif opcao2 == "2":
                                        valor_saque = float(input("Digite o valor do saque: ")) 
                                        conta_selecionada['Saldo'], conta_selecionada['Extrato'] = sacar(saldo=conta_selecionada['Saldo'], valor=valor_saque, extrato=conta_selecionada['Extrato'], conta=conta_selecionada)

                                    elif opcao2 == "3":
                                        extrato_bancario(conta_selecionada['Saldo'], extrato =conta_selecionada['Extrato'])


                                    elif opcao2 == "4":
                                        print(f"Voltando para o menu principal, {usuario_selecionado['Nome']}!")
                                        break

                                    else:
                                        print("Opção inválida. Selecione uma das opções abaixo:")
                                
                    elif opcao1 == "3":
                        print(f"Até logo, {usuario_selecionado['Nome']}!")
                        break

                    else:
                        print("Opção inválida. Selecione uma das opções abaixo:")

                
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Selecione uma das opções abaixo:")


main()