def menu():
	print("MENU DE OPÇÕES")
	print("1. Submenu de Médicos")
	print("2. Submenu de Pacientes")
	print("3. Submenu de Consultas")
	print("4. Submenu dos Relatórios")
	print("5. Sair")

	opc = int(input("Qual opção você deseja? "))

	return opc

# DICIONÁRIO DOS MÉDICOS
def inserirMedicos(medicos, emails, telefones):
    crm = str(input("Digite o CRM: ")).lower()
    nome = str(input("Digite o seu nome: ")).lower()
    data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
    sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
    especialidade = str(input("Digite a sua especialidade: ")).lower()
    universidade = str(input("Digite a universidade em que se formou: ")).lower()

    emails = inserirEmail(emails)
    telefones = inserirTelefones(telefones)

    medicos [crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]

    return medicos

# DICIONÁRIO DOS PACIENTES
# Paciente = (CPF, Nome, Data de Nascimento, Sexo, Plano de Saúde, E-mails, Telefones)
def inserirPacientes(pacientes, emails, telefones):
    cpf = str(input("Digite o CPF: ")).lower()
    nome = str(input("Digite o seu nome: ")).lower()
    data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
    sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
    plano_saude = str(input("Digite o seu plano de saúde: ")).lower()
    
    emails = inserirEmail(emails)
    telefones = inserirTelefones(telefones)

    pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]

    return pacientes


# DICIONÁRIO DA CONSULTA
# Consulta = (CRM, CPF, Data, Hora, Diagnostico, Medicamentos)
def inserirConsultas(consultas):

    return consultas

# SUBFUNÇÕES
def inserirEmail(emails):
    email = str(input("Digite o e-mail: ")).lower()
    
    while email != "":
        emails.append(email)
        email = str(input("Digite o e-mail ou [ENTER] para sair: ")).lower()
    
    return emails
        

def inserirTelefones(telefones):
    telefone = str(input("Digite o telefone ou [ENTER] para sair: ")).lower()

    while telefone != "":
        telefones.append(telefone)
        telefone = str(input("Digite o telefone ou [ENTER] para sair: ")).lower()
    
    return telefones

# FUNÇÕES PRINCIPAIS
def subMenu(opcao, medicos, pacientes, consultas):
    while opcao <= 4:
        emails = []
        telefones = []
        print("="*100)
        print("SUBMENU DE OPÇÕES")
        if opcao == 1:
            print("1. Incluir Médico")
            print("2. Alterar Médico")
            print("3. Excluir Médico")
            print("4. Listar Médico")
            print("5. Listar Todos")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                inserirMedicos(medicos, emails, telefones)

        elif opcao == 2:
            print("1. Incluir Paciente")
            print("2. Alterar Paciente")
            print("3. Excluir Paciente")
            print("4. Listar Paciente")
            print("5. Listar Todos")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                inserirPacientes(pacientes, emails, telefones)

        elif opcao == 3:
            print("1. Incluir Consulta")
            print("2. Alterar Consulta")
            print("3. Excluir Consulta")
            print("4. Listar Consulta")
            print("5. Listar Todas")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                inserirConsultas(consultas)

        elif opcao == 4:
            print("1. Mostrar medicos com a especialização X")
            print("2. Mostrar pacientes menores de X idade")
            print("3. Mostrar o CRM, o nome do médico, o CPF do paciente, o nome do paciente, data, hora, diagnostico e medicamentos para todas as consultas realizadasnos últimos X dias")
            opc = int(input("Qual opção você deseja? "))   
                
        print("="*100)
        opcao = menu()
        
    print("Encerrando...")    

def main():
    medicos = dict()
    pacientes = dict()
    consultas = dict()

    subMenu(menu(), medicos, pacientes, consultas)

    print(medicos)
    print(pacientes)
    print(consultas)
    
    
main()