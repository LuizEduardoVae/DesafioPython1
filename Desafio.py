
# # # # # # # # # # # # # # Menus do Sistema  # # # # # # # # # # # # # #


menu_conta = """

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
[2] Acessar sua conta
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

def criar_conta():
    print("Ola")
     
def selecionar_conta():
    print("Ola")

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
                print( "\nDeseja acessar sua conta?")
                s_i = input(sim_nao_usuario)

                if s_i == "1":
                    if usuarios:
                        usuario_selecionado = selecionar_usuario()

                        if usuario_selecionado:
                            usuario_selecionado_nome = usuario_selecionado["Nome"]
                            print(f"\nBem-vindo(a), {usuario_selecionado_nome}!")
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

    