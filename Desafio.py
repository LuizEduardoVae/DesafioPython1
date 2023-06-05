
# # # # # # # # # # # # # # Menus do Sistema  # # # # # # # # # # # # # #
menu_conta = """

[1] Criar conta
[2] Acessar conta
[3] Sair

=> """

menu_conta_acoes = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

sim_nao_conta = """

[1] Sim
[2] Nao

=> """


sim_nao_usuario = """

[1] Sim
[2] Nao

=> """

menu_usuario = """

[1] Criar Usuario
[2] Acessar seu Usuario
[3] Sair

[s] Adm

=> """


# # # # # # # # # # # # # #  Variaveis Globais  # # # # # # # # # # # # # #

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

contas = {}
numero_conta = 0
agencia = "0001/"

senha_adm = "Senha123"


# # # # # # # # # # # # # # Funcoes de Usuario  # # # # # # # # # # # # # #

def cadastrar_endereco(rua, numero_casa, bairro_casa, cidade_casa):
    rua = str(input("Rua: "))
    numero_casa = str(input("Numero: "))
    bairro_casa = str(input("Bairro: "))
    cidade_casa = str(input("Cidade: "))

    numero_casa_validado = validar_numero_casa(numero_casa)

    if numero_casa_validado:
        print("\nEndereço validado")
        endereco = {
            "logradouro": rua,
            "numero": numero_casa,
            "bairro": bairro_casa,
            "cidade": cidade_casa
        }
        return endereco
    else:
        print("\nNúmero de casa inválido")
        return None

def validar_cpf(cpf):
    if not cpf.isdigit():
        return False
    return True

def validar_numero_casa(numero_casa):
    if not numero_casa.isdigit():
        return False
    return True

def criar_usuario(nome, data_nascimento, cpf):
    nome = str(input("Nome: "))
    data_nascimento = str(input("Data de Nascimento: "))
    cpf = str(input("CPF: "))

    cpf_valido = validar_cpf(cpf)
    
    if cpf_valido:

        for usario in usuarios.values():
            if usario["CPF"] == cpf:
                print("\nCPF já cadastrado.")
                return None

           
        print("CPF validado")
        endereco = cadastrar_endereco(rua, numero_casa, bairro_casa, cidade_casa)

        if endereco is not None:
                dados_usuario = {
                    "CPF": cpf,
                    "Data de Nascimento": data_nascimento,
                    "Nome": nome,
                    "Endereco": endereco
                }

                usuarios[cpf] = dados_usuario
                return usuarios
            
        else:
                print("\nNão foi possível cadastrar o endereço.")
                return None
    else:
        print("CPF inválido")
        return None

def selecionar_usuario():
    login_usuario = input("CPF do seu usuário: ")

    for usuario in usuarios.values():
        if usuario["CPF"] == login_usuario:
            print("\nLogado com sucesso")
            return usuario
    
    print("\nUsuário não encontrado.")
    return None     
      
# # # # # # # # # # # # # # Funcoes de Conta  # # # # # # # # # # # # # #

def criar_conta(cpf, contas, extrato):
    global agencia

    numero_conta = str(len(contas) + 1)

    conta_dados = {
        "Conta": numero_conta,
        "Saldo": saldo,
        "Extrato": extrato
    }

    contas[numero_conta] = conta_dados

    return contas

    


     
def selecionar_conta(contas):
    print("Selecione uma conta:")
    
    for numero_conta, dados_conta in contas.items():
        print(f"Conta: {numero_conta}")
        print(f"Saldo: R$ {dados_conta['Saldo']}")
        print("----")

    numero_conta_selecionada = input("Digite o número da conta desejada: ")
    

    for numero_conta in contas.values():
        if numero_conta["Conta"] == numero_conta_selecionada:
            print("\nLogado com sucesso")
            return numero_conta
    
    print("\nConta não encontrada.")
    return None     


    # if conta_selecionada:
    #     return conta_selecionada
    # else:
    #     print("Conta não encontrada.")
    #     return None

# # # # # # # # # # # # # # Funcoes dentro Conta  # # # # # # # # # # # # # #

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

# # # # # # # # # # # # # # Funcoes da Adm  # # # # # # # # # # # # # #

def digitar_senha_adm():
    senha = input("Digite a senha: ")

    if senha == senha_adm:
        print("\nLogado com sucesso")
        return senha
    
    print("\nLogin Invalido.")
    return None   

# # # # # # # # # # # # # # Main  # # # # # # # # # # # # # #

while True:

    opcao1 = input(menu_usuario)

    if opcao1 == "1":
         while True:
                print( " \nDeseja criar um usuario?")
                s_i = input(sim_nao_usuario)

                if s_i == "1":
                    usuarios = criar_usuario(nome,data_nascimento,cpf)
                    
                else:
                    break
    
    elif opcao1 == "2":
         while True:
                print( "\nDeseja acessar seu usuario?")
                s_i = input(sim_nao_usuario)

                if s_i == "1":
                    if usuarios:
                        usuario_selecionado = selecionar_usuario()

                        if usuario_selecionado:
                            usuario_selecionado_nome = usuario_selecionado["Nome"]
                            print(f"\nBem-vindo(a), {usuario_selecionado_nome}!")

                            while True:
                                opcao2 = input(menu_conta)

                                if opcao2 == "1":
                                    print( "\n\nDeseja cria uma conta?")
                                    y_n = input(sim_nao_conta)

                                    if y_n == "1":

                                        contas = criar_conta(usuario_selecionado["CPF"], contas, extrato)


                                    else:
                                        print("\nvoltando ao menu de opcoes da conta...")


                                if opcao2 == "2":
                                    conta_escolhida = selecionar_conta(contas)

                                    if conta_escolhida:
                                        while True:

                                            opcao3 = input(menu_conta_acoes)

                                            if opcao3 == "1":
                                                print("Ola")
                                            if opcao3 == "2":
                                                print("Ola")
                                            if opcao3 == "3":
                                                print("Ola")
                                            if opcao3 == "4":
                                                print("Ola")
                                                break
                                            else:
                                                print("Opcao Invalida")


                                if opcao2 == "3":
                                    break

                                else:
                                    ("Opcao invalida")
                                        

                        else:
                            print("Usuario nao encontrado")
                
                    else:
                        print("\nSem usuarios")
                else:
                    break

    
    elif opcao1 == "3":
        print("Saindo...")
        break
    elif opcao1 == "s":

        loginAprovado = digitar_senha_adm()

        if loginAprovado:
            for index,nome_usuario in enumerate(usuarios.keys(), start=1):
                print(f"{index}. {nome_usuario}")
        else:
            print("\nNao foi possivel completar o login!")
            print("Tente novamente em breve!")
            
        
    else:
        print("\n\nOpcao Invalida")
        print("Selecione uma das opções abaixo:")

    