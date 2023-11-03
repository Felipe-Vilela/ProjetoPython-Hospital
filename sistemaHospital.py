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
    if verificarInclusao(medicos, crm):
        nome = str(input("Digite o seu nome: ")).lower()
        data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
        sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
        especialidade = str(input("Digite a sua especialidade: ")).lower()
        universidade = str(input("Digite a universidade em que se formou: ")).lower()

        emails = inserirEmail(emails)
        telefones = inserirTelefones(telefones)

        medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]

        return True
    else:
        return False

def alterarMedico(medicos):
    print("Informe o CRM do médico que deseja alterar: ")
    crm = str(input("Digite o CRM: ")).lower()
    
    emails = []
    telefones = []
    lista_geral = []

    if crm in medicos.keys():
        for k in medicos.keys():
            if crm == k:
                for v in medicos.get(k):
                    lista_geral.append(v)
                
        nome = lista_geral[0]
        data_nascimento = lista_geral[1]
        sexo = lista_geral[2]
        especialidade = lista_geral[3]
        universidade = lista_geral[4]
        emails = lista_geral[5]
        telefones = lista_geral[6]
        
        opcaoAlterar = str(input("Qual dado você deseja alterar (nome, data de nascimento, sexo, especialidade, universidade, emails, telefones)? ")).lower()
        
        if opcaoAlterar == "nome":
            nome = str(input("Digite o nome: ")).lower()
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
            return True 
        elif opcaoAlterar == "data de nascimento":
            data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
            return True 
        elif opcaoAlterar == "sexo":
            sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
            return True
        elif opcaoAlterar == "especialidade":
            especialidade = str(input("Digite a sua especialidade: ")).lower()
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
            return True
        elif opcaoAlterar == "universidade":
            universidade = str(input("Digite a universidade em que se formou: ")).lower()
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
            return True
        elif opcaoAlterar == "emails":
            emailAlterar = str(input("Digite o e-mail que deseja alterar: "))
            emailNovo = str(input("Digite o e-mail novo: "))

            emails.remove(emailAlterar)
            emails.append(emailNovo) 
    
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
        
            return True
        elif opcaoAlterar == "telefones":
            telefoneAlterar = str(input("Digite o telefone que deseja alterar: "))
            telefoneNovo = str(input("Digite o telefone novo: "))

            telefones.remove(telefoneAlterar)
            telefones.append(telefoneNovo) 

            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
        
            return True
        else:
            return False
    else:
        return False
    
def excluirMedico(medicos):
    crm = str(input("Infome o CRM do médico que deseja excluir: "))
    if crm in medicos.keys():
        del medicos[crm]
        return True
    else:
        return False

def listarMedico(medicos):
    crm = str(input("Digite o CRM: ")).lower()
    
    if crm in medicos.keys():
        for chave in medicos.keys():
            if chave == crm:
                print(f"Nome: {medicos.get(chave)[0].capitalize()}")
                print(f"Data de nascimento: {medicos.get(chave)[1]}")
                print(f"Sexo: {medicos.get(chave)[2].capitalize()}")
                print(f"Especialidade: {medicos.get(chave)[3].capitalize()}")
                print(f"Universidade: {medicos.get(chave)[4].capitalize()}")

                for email in medicos.get(chave)[5]:
                    print(f"Email: {email}")

                for telefone in medicos.get(chave)[6]:
                    print(f"Telefone: {telefone}")
    else:
        print("Médico inválido.")

def gravar_medicos(nome_arquivo, medicos):
    ref_arq = open(nome_arquivo, "w")

    for chave in medicos.keys():
        linha = ""
        linha += chave + ";"
        
        for i in range(len(medicos.get(chave)) - 2):
            linha += medicos.get(chave)[i] + ";"

        for emails in medicos.get(chave)[5]:
            linha += emails + ";"

        for telefones in medicos.get(chave)[6]:
            linha += telefones + ";"
            
        linha += "\n"

        ref_arq.write(linha)
    ref_arq.close()

def ler_medicos(nome_arquivo, medicos):
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo, "r")
        
        for linha in ref_arq:
            if linha != "\n":
                linha = linha.split(";")

                chave = linha[0]
                medicos[chave] = []
                medicos.get(chave).append(linha[1])
                medicos.get(chave).append(linha[2])
                medicos.get(chave).append(linha[3])
                medicos.get(chave).append(linha[4])
                medicos.get(chave).append(linha[5])

                medicos.get(chave).append([])
                medicos.get(chave).append([])

                for i in range(6, len(linha)):
                    if linha[i] != "\n":
                        if "@" in linha[i]:
                            medicos.get(chave)[5].append(linha[i])
                        elif verificarTel(linha[i]):
                            medicos.get(chave)[6].append(linha[i])
    print(medicos)
    return medicos

# DICIONÁRIO DOS PACIENTES

def inserirPacientes(pacientes, emails, telefones):
    cpf = str(input("Digite o CPF: ")).lower()
    if verificarInclusao(pacientes, cpf):
        nome = str(input("Digite o seu nome: ")).lower()
        data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
        sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
        plano_saude = str(input("Digite o seu plano de saúde: ")).lower()
        emails = inserirEmail(emails)
        telefones = inserirTelefones(telefones)

        pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
        return True
    else:
        print("Paciente já está na lista")

        return False

def alterarPaciente(pacientes):
    print("Informe o CPF do paciente que deseja alterar: ")

    cpf = str(input("Digite o CPF: ")).lower()

    emails = []
    telefones = []
    lista_geral = []

    if cpf in pacientes.keys():
        for k in pacientes.keys():
            if cpf == k:
                for v in pacientes.get(k):
                    lista_geral.append(v)
        
        nome = lista_geral[0]
        data_nascimento = lista_geral[1]
        sexo = lista_geral[2]
        plano_saude = lista_geral[3]
        emails = lista_geral[4]
        telefones = lista_geral[5]

        opcaoAlterar = str(input("Qual dado você deseja alterar (nome, data de nascimento, sexo, plano de saúde, emails, telefones)? ")).lower()

        if opcaoAlterar == "nome":
            nome = str(input("Digite o nome: ")).lower()
            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
            return True 

        elif opcaoAlterar == "data de nascimento":
            data_nascimento =  str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
            return True 

        elif opcaoAlterar == "sexo":
            sexo =  str(input("Digite o sexo: ")).lower()
            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
            return True 
        
        elif opcaoAlterar == "plano de saúde":
            plano_saude =  str(input("Digite o plano de saúde: ")).lower()
            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
            return True 
        elif opcaoAlterar == "emails":
            emailAlterar = str(input("Digite o e-mail que deseja alterar: "))
            emailNovo = str(input("Digite o e-mail novo: "))

            emails.remove(emailAlterar)
            emails.append(emailNovo) 

            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
        
            return True
        elif opcaoAlterar == "telefones":
            telefoneAlterar = str(input("Digite o telefone que deseja alterar: "))
            telefoneNovo = str(input("Digite o telefone novo: "))

            telefones.remove(telefoneAlterar)
            telefones.append(telefoneNovo) 

            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
        
            return True
        else:
            return False
    else:
        return False

def excluirPaciente(pacientes):
    cpf = str(input("Infome o CPF do paciente que deseja excluir: "))
    if cpf in pacientes.keys():
        del pacientes[cpf]
        return True
    else:
        return False

def listarPaciente(pacientes):
    return True

def listarTodos(dicionario): #Utilizado para pacientes, medicos e consultas
    return True

def gravar_pacientes(nome_arquivo, pacientes):
    ref_arq = open(nome_arquivo, "w")

    for chave in pacientes.keys():
        linha = ""
        linha += chave + ";"
        
        for i in range(len(pacientes.get(chave)) - 2):
            linha += pacientes.get(chave)[i] + ";"

        for emails in pacientes.get(chave)[4]:
            linha += emails + ";"

        for telefones in pacientes.get(chave)[5]:
            linha += telefones + ";"
            
        linha += "\n"

        ref_arq.write(linha)
    ref_arq.close()

def ler_pacientes(nome_arquivo, pacientes):
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo, "r")
    
    for linha in ref_arq:
        if linha != "\n":
            linha = linha.split(";")

            chave = linha[0]
            pacientes[chave] = []
            pacientes.get(chave).append(linha[1])
            pacientes.get(chave).append(linha[2])
            pacientes.get(chave).append(linha[3])
            pacientes.get(chave).append(linha[4])

            pacientes.get(chave).append([])
            pacientes.get(chave).append([])

            for i in range(4, len(linha)):
                if linha[i] != "\n":
                    if "@" in linha[i]:
                        pacientes.get(chave)[4].append(linha[i])
                    elif verificarTel(linha[i]):
                        pacientes.get(chave)[5].append(linha[i])
    print(pacientes)
    return pacientes


# DICIONÁRIO DA CONSULTA
def inserirConsultas(consultas):
    crm = str(input("Digite o CRM: ")).lower()
    cpf = str(input("Digite o CPF: ")).lower()
    data = str(input("Digite a data (xx/xx/xxxx): ")).lower()
    hora = str(input("Digite o horario (xx:xx): ")).lower()
    chaves = (crm, cpf, data, hora)

    if consultas != {} :
        for k in consultas.keys():
            if k[0] == crm and k[2] == data and k[3] == hora or k[1] == cpf and k[2] == data and k[3] == hora:            
                return False
            
            else:
                diagnostico = str(input("Digite o diagnóstico: ")).lower()
                medicamentos = []
                medicamentos = inserirMedicamentos(medicamentos)
                consultas[chaves] = [diagnostico, medicamentos]
                return True
    else:
        diagnostico = str(input("Digite o diagnóstico: ")).lower()
        medicamentos = []
        medicamentos = inserirMedicamentos(medicamentos)
        consultas[chaves] = [diagnostico, medicamentos]

        return True

def alterarConsulta(consultas):
    print("Informe os dados da consulta que deseja alterar: ")
    crm = str(input("Digite o CRM: ")).lower()
    cpf = str(input("Digite o CPF: ")).lower()
    data = str(input("Digite a data (xx/xx/xxxx): ")).lower()
    hora = str(input("Digite o horario (xx:xx): ")).lower()

    consultaAlterar = (crm, cpf, data, hora)

    medicamentos = []
    lista_geral = []

    if consultaAlterar in consultas.keys():
        for k in consultas.keys():
            if consultaAlterar == k:
                for v in consultas.get(k):
                    lista_geral.append(v)
        
        diagnostico = lista_geral[0]
        medicamentos = lista_geral[1]

        opcaoAlterar = str(input("Qual dado você deseja alterar (diagnostico ou medicamentos)? ")).lower()

        if opcaoAlterar == "diagnostico":
            diagnostico = str(input("Digite o diagnóstico: ")).lower()
            consultas[consultaAlterar] = [diagnostico, medicamentos]

            return True 
        elif opcaoAlterar == "medicamentos":
            medicamentoAlterar = str(input("Digite o medicamento que deseja alterar: "))
            medicamentoNovo = str(input("Digite o medicamento novo: "))

            medicamentos.remove(medicamentoAlterar)
            medicamentos.append(medicamentoNovo) 

            consultas[consultaAlterar] = [diagnostico, medicamentos]

            return True
        else:
            return False
    else:
        return False
    
def excluirConsulta(consultas):
    print("Informe os dados da consulta que deseja excluir: ")
    crm = str(input("Digite o CRM: ")).lower()
    cpf = str(input("Digite o CPF: ")).lower()
    data = str(input("Digite a data (xx/xx/xxxx): ")).lower()
    hora = str(input("Digite o horario (xx:xx): ")).lower()

    consultaExcluir = (crm, cpf, data, hora)

    if consultaExcluir in consultas.keys():
        del consultas[consultaExcluir]
        return True
    else:
        return False
    
def listarConsulta(consultas):  
    crm = str(input("Digite o CRM: ")).lower()
    cpf = str(input("Digite o CPF: ")).lower()
    data = str(input("Digite a data (xx/xx/xxxx): ")).lower()
    hora = str(input("Digite o horario (xx:xx): ")).lower()
    chaves = (crm, cpf, data, hora)

    if chaves in consultas.keys():
        for chave in consultas.keys():
            if chaves == chave:
                print(f"Diagnóstico: {consultas.get(chave)[0].capitalize()}")
                
                for medicamentos in consultas.get(chave)[1]:
                    print(f"Medicamento: {medicamentos.capitalize()}")
    else:
        print("Consulta inválida.")
    
def gravar_consultas(nome_arquivo, consultas):
    ref_arq = open(nome_arquivo, "w")
    for chave in consultas.keys():
        linha = ""
        linha += chave[0] + ";"
        linha += chave[1] + ";"
        linha += chave[2] + ";"
        linha += chave[3] + ";"
      
        linha += consultas.get(chave)[0] + ";"
        for medicamentos in consultas.get(chave)[1]:
            linha += medicamentos + ";"
        
        linha += "\n"

        ref_arq.write(linha)

    ref_arq.close()

def ler_consultas(nome_arquivo, consultas):
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo, "r")

        for linha in ref_arq:
            if linha != "\n":
                linha = linha.split(";")
                chaves = (linha[0], linha[1], linha[2], linha[3])
                consultas[chaves] = []
                consultas.get(chaves).append(linha[4])
                consultas.get(chaves).append([])

                for i in range(5, len(linha) - 1):
                    if linha[i] != "\n":
                        consultas.get(chaves)[1].append(linha[i])

        ref_arq.close()
    return consultas
    
# FUNÇÕES RELATÓRIOS
def medicosEspecilizacaoX(medicos,especializacao):
    return True

def pacientesMenoresXIdade(pacientes,idade):
    return True

def mostrarConsultasNosUltimosXDias(medicos, pacientes, consultas, diasAtras):
    return True

# SUBFUNÇÕES
def verificarTel(posicao_lista):
    if  "0" in posicao_lista or "0" in posicao_lista or "1" in posicao_lista or "2" in posicao_lista or "3" in posicao_lista or "4" in posicao_lista or "5" in posicao_lista or "6" in posicao_lista or "7" in posicao_lista or "8" in posicao_lista or "9" in posicao_lista or "-" in posicao_lista:   
        return True
    else:
        return False

def existe_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False
    
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

def inserirMedicamentos(medicamentos):
    medicamento = str(input("Digite o medicamento: ")).lower()
    
    while medicamento != "":
        medicamentos.append(medicamento)
        medicamento = str(input("Digite o medicamento ou [ENTER] para sair: ")).lower()

    return medicamentos

def verificarInclusao(dicionario, chave):
    if chave not in dicionario.keys():
        return True
    else:
        return False

# FUNÇÕES PRINCIPAIS
def subMenu(medicos, pacientes, consultas):
    consultas = ler_consultas("Consultas.txt", consultas)
    medicos = ler_medicos("Medicos.txt", medicos)
    pacientes = ler_pacientes("Pacientes.txt", pacientes)
    opcao = 1
    while opcao != 5:
        opcao = menu()
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
                if inserirMedicos(medicos, emails, telefones):
                    print("Médico adicionado com sucesso!")
                else:
                    print("Médico já está cadastrado.")
            elif opc == 2:
                if alterarMedico(medicos):
                    print("Médico alterado com sucesso!")
                else:
                    print("Médico inválido.")
            elif opc == 3:
                if excluirMedico(medicos):
                    print("Médico excluido com sucesso!")
                else:
                    print("Médico inválido.")
            elif opc == 4:
                listarMedico(medicos)

        elif opcao == 2:
            print("1. Incluir Paciente")
            print("2. Alterar Paciente")
            print("3. Excluir Paciente")
            print("4. Listar Paciente")
            print("5. Listar Todos")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirPacientes(pacientes, emails, telefones):
                    print("Paciente adicionado com sucesso!")
                else:
                    print("Paciente já esta cadastrado.")
            if opc == 2:
                if alterarPaciente(pacientes):
                    print("Paciente alterado com sucesso!")
                else:
                    print("Paciente inválido.")
            
            elif opc ==3:
                if excluirPaciente(pacientes):
                    print("Paciente excluido com sucesso!")
                else:
                    print("Paciente inválido.")

        elif opcao == 3:
            print("1. Incluir Consulta")
            print("2. Alterar Consulta")
            print("3. Excluir Consulta")
            print("4. Listar Consulta")
            print("5. Listar Todas")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirConsultas(consultas):
                    print("Consulta marcada com sucesso!")
                else:
                    print("Consulta inválida.")  
            if opc == 2:         
                if alterarConsulta(consultas):
                    print("Consulta alterada com sucesso!")                
                else:
                    print("Consulta inválida.")           
            elif opc == 3:
                if excluirConsulta(consultas):
                    print("Consulta excluida com sucesso!")
                else:
                    print("Consulta inválida.")
            elif opc == 4:
                listarConsulta(consultas)

        elif opcao == 4:
            print("1. Mostrar medicos com a especialização X")
            print("2. Mostrar pacientes menores de X idade")
            print("3. Mostrar o CRM, o nome do médico, o CPF do paciente, o nome do paciente, data, hora, diagnostico e medicamentos para todas as consultas realizadasnos últimos X dias")
            opc = int(input("Qual opção você deseja? "))   

            if opc == 1:
                especializacao = str(input("Informe a especialização desejada: "))
                if medicosEspecilizacaoX(medicos,especializacao):
                    print(f"Esses são os médicos com a especialização {especializacao} !")
                else:
                    print(f"Não temos médicos com a especialização informada: {especializacao}")
            elif opc == 2:
                idade = int(input("Informe a idade máxima dos pacientes que deseja ver: "))
                if pacientesMenoresXIdade(pacientes, idade):
                    print(f"Esses são os pacientes menores de {idade} anos!")
                else:
                    print(f"Não temos pacientes menores de {idade} anos!")
            elif opc == 3:
                ultimosDias = int(input("Informe de quantos dias atrás deseja ver consultas: "))
                if mostrarConsultasNosUltimosXDias(medicos, pacientes, consultas):
                    print(f"Essas são as consultas dos ultimos {ultimosDias} dias ")
        elif opcao == 5:
            gravar_medicos("Medicos.txt", medicos)
            gravar_consultas("Consultas.txt", consultas)
            gravar_pacientes("Pacientes.txt", pacientes)
            print("Encerrando o programa...")
                
        print("="*100)     

def main():
    medicos = dict()
    pacientes = dict()
    consultas = dict()

    subMenu( medicos, pacientes, consultas)

    print(medicos)
    print(pacientes)
    print(consultas)
    
    
main()