
# Variaveis Globais
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
usuarios_criar = []
rua = ''
numero_casa = ''
bairro_casa = ''
cidade_casa = ''

# 



usuarios = {}
usuarios_criar = []
rua = ''
numero_casa = ''
bairro_casa = ''
nome = ''
data_nascimento= ''
cpf = ''
cidade_casa = ''



def cadastrar_endereco(rua, numero_casa, bairro_casa, cidade_casa):
    rua = str(input("Rua: "))
    numero_casa = str(input("Numero: "))
    bairro_casa = str(input("Bairro: "))
    cidade_casa = str(input("Cidade: "))

    numero_casa_validado = validar_numero_casa(numero_casa)
    
    if numero_casa_validado[0]:
        print("\nEndereco validado")
        print("\nEndereco cadastrado!")

        endereco = {
            "logradouro": rua,
            "numero": numero_casa,
            "bairro": bairro_casa,
            "cidade": cidade_casa
        }

        return endereco, numero_casa


    else:
        print("Endereço inválido")
        print("Cadastre um endereço novamente")
        endereco = None

        return None
  


def validar_cpf(cpf):
    if not cpf.isdigit():
        return False, cpf
    return True, cpf

def validar_numero_casa(numero_casa):
    if not numero_casa.isdigit():
        return False, numero_casa
    return True, numero_casa


def criar_usuario(nome,data_nascimento,cpf):
    nome = str(input("Nome: "))
    data_nascimento = str(input("Data de Nascimento: "))
    cpf = str(input("CPF: "))

    
    cpf_validado = validar_cpf(cpf)

    if cpf_validado[0]:
        print("CPF validado")
        cpf = cpf_validado[1]
        endereco = cadastrar_endereco(rua, numero_casa, bairro_casa, cidade_casa)
        if endereco is not None:
            dados_usuario = {
                "Nome": nome,
                "Data de Nascimento": data_nascimento,
                "CPF": cpf,
                "Endereco": endereco
            }

            usuarios[nome] = dados_usuario
            return usuarios
        
        else:
            print("Não foi possível cadastrar o endereço.")
            return None
    else:
        print("CPF inválido")
        print("Crie uma conta Novamente")
        return None

    

usuarios = criar_usuario(nome, data_nascimento, cpf)


print(usuarios)




