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
        while verificarData(data_nascimento) == False:
            print("Formato inválido.")
            data_nascimento = str(input("Digite a data de nascimento novamente (xx/xx/xxxx): ")).lower()
            verificarData(data_nascimento)

            
        sexo = str(input("Digite o seu sexo (M/F): ")).lower()
        sexo = verificaSexo(sexo)

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
            while verificarData(data_nascimento) == False:
                print("Formato inválido")
                data_nascimento = str(input("Digite a data de nascimento novamente (xx/xx/xxxx): ")).lower()
                verificarData(data_nascimento)
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
            return True 
        elif opcaoAlterar == "sexo":
            sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
            sexo = verificaSexo(sexo)
            
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
            while verificarEmail(emailNovo) == False:
                print("Formato inválido.")
                emailNovo = str(input("Digite o e-mail novo novamente: "))

            emails.remove(emailAlterar)
            emails.append(emailNovo) 
    
            medicos[crm] = [nome, data_nascimento, sexo, especialidade, universidade, emails, telefones]
        
            return True
        elif opcaoAlterar == "telefones":
            telefoneAlterar = str(input("Digite o telefone que deseja alterar: "))
            telefoneNovo = str(input("Digite o telefone novo: "))
            while verificarTel(telefoneNovo) == False:
                print("Formato inválido.")
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
        deseja_excluir = str(input("Médico encontrado. Deseja mesmo excluir (S ou N)? ")).lower()
        if deseja_excluir == "s":
            del medicos[crm]
            print("Médico excluído com sucesso!")
        else:
            print("Médico não excluído.")
    else:
        print("Médico inválido.")

def listarMedico(medicos, crm):    
    if crm in medicos.keys():
        for chave in medicos.keys():
            if chave == crm:
                print(f"Nome: {medicos.get(chave)[0].title()}")
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

def listarTodosMedicos(medicos): # Utilizado para listar todos médicos
    for chave in medicos.keys():
        print("_"*100)

        print(f"CRM: {chave}")
        print(f"Nome: {medicos.get(chave)[0].title()}")
        print(f"Data de nascimento: {medicos.get(chave)[1]}")
        print(f"Sexo: {medicos.get(chave)[2].capitalize()}")
        print(f"Especialidade: {medicos.get(chave)[3].capitalize()}")
        print(f"Universidade: {medicos.get(chave)[4].capitalize()}")

        for email in medicos.get(chave)[5]:
                print(f"Email: {email}")

        for telefone in medicos.get(chave)[6]:
            print(f"Telefone: {telefone}")
      
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
    return medicos

# DICIONÁRIO DOS PACIENTES
def inserirPacientes(pacientes, emails, telefones):
    cpf = str(input("Digite o CPF: ")).lower()
    if verificarInclusao(pacientes, cpf):
        nome = str(input("Digite o seu nome: ")).lower()
        data_nascimento = str(input("Digite a data de nascimento (xx/xx/xxxx): ")).lower()
        while verificarData(data_nascimento) == False:
            print("Formato inválido.")
            data_nascimento = str(input("Digite a data de nascimento novamente (xx/xx/xxxx): ")).lower()
            verificarData(data_nascimento)

        sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
        sexo = verificaSexo(sexo)

        plano_saude = str(input("Digite o seu plano de saúde: ")).lower()
        emails = inserirEmail(emails)
        telefones = inserirTelefones(telefones)

        pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
        return True
        
    else:
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
            while verificarData(data_nascimento) == False:
                print("Formato inválido.")
                data_nascimento =  str(input("Digite a data de nascimento novamente (xx/xx/xxxx): ")).lower()
                verificarData(data_nascimento)

            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
            return True 

        elif opcaoAlterar == "sexo":
            sexo = str(input("Digite o seu sexo (M/F) : ")).lower()
            sexo = verificaSexo(sexo)

            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
            return True 
        
        elif opcaoAlterar == "plano de saúde":
            plano_saude =  str(input("Digite o plano de saúde: ")).lower()
            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
            return True 
        elif opcaoAlterar == "emails":
            emailAlterar = str(input("Digite o e-mail que deseja alterar: "))
            emailNovo = str(input("Digite o e-mail novo: "))
            while verificarEmail(emailNovo) == False:
                print("Formato inválido.")
                emailNovo = str(input("Digite o e-mail novo novamente: "))

            emails.remove(emailAlterar)
            emails.append(emailNovo) 

            pacientes[cpf] = [nome, data_nascimento, sexo, plano_saude, emails, telefones]
        
            return True
        elif opcaoAlterar == "telefones":
            telefoneAlterar = str(input("Digite o telefone que deseja alterar: "))
            telefoneNovo = str(input("Digite o telefone novo: "))
            while verificarTel(telefoneNovo) == False:
                print("Formato inválido.")
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
        deseja_excluir = str(input("Paciente encontrado. Deseja mesmo excluir (S ou N)? ")).lower()
        if deseja_excluir == "s":
            del pacientes[cpf]
            print("Paciente excluído com sucesso!")
        else:
            print("Paciente não excluído.")
    else:
        print("Paciente inválido.")

def listarPaciente(pacientes):
    cpf = str(input("Digite o CPF: ")).lower()
    
    if cpf in pacientes.keys():
        for chave in pacientes.keys():
            if chave == cpf:
                print(f"Nome: {pacientes.get(chave)[0].title()}")
                print(f"Data de nascimento: {pacientes.get(chave)[1]}")
                print(f"Sexo: {pacientes.get(chave)[2].capitalize()}")
                print(f"Plano de saúde: {pacientes.get(chave)[3].capitalize()}")

                for email in pacientes.get(chave)[4]:
                    print(f"Email: {email}")

                for telefone in pacientes.get(chave)[5]:
                    print(f"Telefone: {telefone}")
            
    else:
        print("Paciente inválido.")

def listarTodosPacientes(pacientes): #Utilizado para listar todos os pacientes
    for chave in pacientes.keys():
        print("_"*100)

        print(f"CPF: {chave}")
        print(f"Nome: {pacientes.get(chave)[0].title()}")
        print(f"Data de nascimento: {pacientes.get(chave)[1]}")
        print(f"Sexo: {pacientes.get(chave)[2].capitalize()}")
        print(f"Plano de saúde: {pacientes.get(chave)[3].capitalize()}")
        
        for email in pacientes.get(chave)[4]:
                print(f"Email: {email}")

        for telefone in pacientes.get(chave)[5]:
            print(f"Telefone: {telefone}")
    
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
    return pacientes

# DICIONÁRIO DA CONSULTA

def inserirConsultas(consultas, medicos, pacientes):
    crm = str(input("Digite o CRM: ")).lower()
    if pessoa_existe(medicos, crm) == False:
        print("Médico não cadastrado.")
        return False
    cpf = str(input("Digite o CPF: ")).lower()
    if pessoa_existe(pacientes, cpf) == False:
        print("Paciente não cadastrado.")
        return False
    data = str(input("Digite a data (xx/xx/xxxx): ")).lower()
    if verificarData(data) == False:
        print("Formato da data inválido.")
        return False
    
    hora = str(input("Digite o horario (xx:xx): ")).lower()
    if verificarHora(hora) == False:
        print("Formato do horário inválido.")
        return False
    
    chaves = (crm, cpf, data, hora)
    

    if consultas != {} :

        for k in consultas.keys():
            if (k[0] == crm or k[1] == cpf) and k[2] == data and k[3] == hora:
                print("Horário não disponível")
                return False

        if (crm, cpf, data, hora) not in consultas:
            diagnostico = str(input("Digite o diagnóstico: ")).lower()
            medicamentos = inserirMedicamentos([])
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

    chaves = (crm, cpf, data, hora)

    if chaves in consultas.keys(): 
        deseja_excluir = str(input("Consulta encontrada. Deseja mesmo excluir (S ou N)? ")).lower()
        if deseja_excluir == "s":
            del consultas[chaves]
            print("Consulta excluída com sucesso!")
        else:
            print("Consulta não excluída.")
    else:
        print("Consulta inválida.")
  
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

def listarTodasConsultas(consultas):
    for chave in consultas.keys():
        print("_"*100)
        print(f"CRM: {chave[0]}")
        print(f"CPF: {chave[1]}")
        print(f"Data: {chave[2]}")
        print(f"Hora: {chave[3]}")
        print(f"Diagnóstico: {consultas.get(chave)[0].capitalize()}")
        
        for medicamentos in consultas.get(chave)[1]:
            print(f"Medicamento: {medicamentos.capitalize()}")
        
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
def medicosEspecilizacaoX(medicos, especializacao):
    cont = 0
    for chave in medicos.keys():
        if medicos.get(chave)[3] == especializacao:
            cont += 1
            print("-" * 100)
            listarMedico(medicos, chave)
    if cont == 0:
        print(f"Não há nenhum médico com a especialização: {especializacao}.")

def pacientesMenoresXIdade(pacientes, idade):
    from datetime import date
    data_atual = str(date.today())
    lista_data_atual = data_atual.split("-")

    lista_data_atual_invertida = []

    for c in range(len(lista_data_atual) -1, -1, -1):
        lista_data_atual_invertida.append(int(lista_data_atual[c]))  

    cont = 0
    for chave in pacientes.keys():
        lista_data_paciente = pacientes.get(chave)[1].split("/")
        
        lista_data_paciente_formatada = []
        for i in lista_data_paciente:
            lista_data_paciente_formatada.append(int(i))
        
        idade_paciente = lista_data_atual_invertida[2] - lista_data_paciente_formatada[2]
        
        if idade_paciente < idade: 
            print("-"*100)
            cont += 1
            print(f"Nome: {pacientes.get(chave)[0].title()}")
            print(f"Data de nascimento: {pacientes.get(chave)[1]}")
            print(f"Sexo: {pacientes.get(chave)[2].capitalize()}")
            print(f"Plano de saúde: {pacientes.get(chave)[3].capitalize()}")

            for email in pacientes.get(chave)[4]:
                print(f"Email: {email}")

            for telefone in pacientes.get(chave)[5]:
                print(f"Telefone: {telefone}")
            
    if cont == 0:
        print(f"Não há pacientes menores de {idade} anos.")

def mostrarConsultasNosUltimosXDias(medicos, pacientes, consultas, ultimosDias):
    import datetime

    cont = 0
    data_atual = datetime.date.today()
    data_consulta = []
    for chave in consultas.keys():
        data_consulta = chave[2].split("/")
    
        data_consulta_int = []
        for i in data_consulta:
            data_consulta_int.append(int(i))

        data_consulta_formatada = datetime.date(day=data_consulta_int[0], month=data_consulta_int[1], year=data_consulta_int[2])
        qtd_ultimos_dias = data_atual - data_consulta_formatada
        qtd_ultimos_dias = qtd_ultimos_dias.days
  
        if qtd_ultimos_dias <= ultimosDias:
            print("-"*100)
            print(f"CRM: {chave[0]}")
            print(f"Nome do médico: {medicos.get(chave[0])[0].title()}")
            print(f"CPF: {chave[1]}")
            print(f"Nome do paciente: {pacientes.get(chave[1])[0].title()}")
            print(f"Data: {chave[2]}")
            print(f"Hora: {chave[3]}")
            print(f"Diagnóstico: {consultas.get(chave)[0].capitalize()}")
            
            for medicamentos in consultas.get(chave)[1]:
                print(f"Medicamento: {medicamentos.capitalize()}")
            cont += 1

    if cont == 0:
        print(f"Não há consultas nos ultimos {ultimosDias} dias.")
        
# SUBFUNÇÕES
def pessoa_existe(dicionario, pessoa):
    if pessoa in dicionario.keys():
        return True
    else:
        return False

def verificarNumeros(string):
    if  "0" in string or "0" in string or "1" in string or "2" in string or "3" in string or "4" in string or "5" in string or "6" in string or "7" in string or "8" in string or "9" in string:   
        return True
    else:
        return False

def verificarHora(hora):
    verificacoes = 0

    if len(hora) != 5:
        return False
    else:
        for i in range(len(hora)):
            if hora[0] ==  verificarNumeros(hora):
                verificacoes += 1
            elif hora[1] == verificarNumeros(hora):
                verificacoes += 1
            elif hora[2] == ":" :
                verificacoes += 1
            elif hora[3] == verificarNumeros(hora):
                verificacoes += 1
            elif hora[4] == verificarNumeros(hora):
                verificacoes += 1
    
        if verificacoes == 5:
            return True
        else:
            return False

def verificarData(data):
    verificacoes = 0

    if len(data) != 10:
        return False
    else:
        for i in range(len(data)):
            if data[0] ==  verificarNumeros(data):
                verificacoes += 1
            elif data[1] == verificarNumeros(data):
                verificacoes += 1
            elif data[2] == "/" :
                verificacoes += 1
            elif data[3] == verificarNumeros(data):
                verificacoes += 1
            elif data[4] == verificarNumeros(data):
                verificacoes += 1
            elif data[5] ==  "/" :
                verificacoes += 1
            elif data[6] == verificarNumeros(data):
                verificacoes += 1
            elif data[7] == ":" :
                verificacoes += 1
            elif data[8] == verificarNumeros(data):
                verificacoes += 1
            elif data[9] == verificarNumeros(data):
                verificacoes += 1
        if verificacoes == 10:
            return True
        else:
            return False

def verificarEmail(email):
    lista_elemento = []
    achou = False
    
    for i in range(len(email)):
        lista_elemento.append(email[i])

    for i in lista_elemento:
        if i == "@":
            achou = True
    
    if achou == True:
        return True
    else:
        return False

def verificarTel(elemento):
    lista_elemento = []
    
    for i in range(len(elemento)):
        lista_elemento.append(elemento[i])

    elemento_verificado = ""

    for i in lista_elemento:
        if  "0" == i or "1" == i or "2" == i or "3" == i or "4" == i or "5" == i or "6" == i or "7" == i or "8" == i or "9" == i or "-" == i:   
            elemento_verificado += i
        else:
            return False

    if elemento_verificado == elemento:
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
        if verificarEmail(email):
            emails.append(email)
        else:
            print("Formato inválido.")
        email = str(input("Digite o e-mail ou [ENTER] para sair: ")).lower()

    return emails
        
def inserirTelefones(telefones):
    telefone = str(input("Digite o telefone: ")).lower()

    while telefone != "":
        if verificarTel(telefone):
            telefones.append(telefone)
        else:
            print("Formato inválido.")
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

def verificaSexo(sexo):
    if sexo == "m":
        sexo = "Masculino"
    else:
        sexo = "Feminino"
    
    return sexo

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
            print("6. Voltar")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirMedicos(medicos, emails, telefones):
                    print("Médico adicionado com sucesso!")
                else:
                    print("Médico já cadastrado.")

            elif opc == 2:
                if alterarMedico(medicos):
                    print("Médico alterado com sucesso!")
                else:
                    print("Médico inválido.")
            elif opc == 3:
                excluirMedico(medicos)
            elif opc == 4:
                crm = str(input("Digite o CRM: ")).lower()
                listarMedico(medicos, crm)
            elif opc == 5:
                listarTodosMedicos(medicos)
            elif opc == 6:
                print("Voltando para o menu principal...")


        elif opcao == 2:
            print("1. Incluir Paciente")
            print("2. Alterar Paciente")
            print("3. Excluir Paciente")
            print("4. Listar Paciente")
            print("5. Listar Todos")
            print("6. Voltar")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirPacientes(pacientes, emails, telefones):
                    print("Paciente adicionado com sucesso!")
                else:
                    print("Paciente já cadastrado.")
            if opc == 2:
                if alterarPaciente(pacientes):
                    print("Paciente alterado com sucesso!")
                else:
                    print("Paciente inválido.")
            elif opc == 3:
                excluirPaciente(pacientes) 
            elif opc == 4:
                listarPaciente(pacientes)
            elif opc == 5:
                listarTodosPacientes(pacientes)
            elif opc == 6:
                print("Voltando para o menu principal...")


        elif opcao == 3:
            print("1. Incluir Consulta")
            print("2. Alterar Consulta")
            print("3. Excluir Consulta")
            print("4. Listar Consulta")
            print("5. Listar Todas")
            print("6. Voltar")
            opc = int(input("Qual opção você deseja? "))

            if opc == 1:
                if inserirConsultas(consultas, medicos, pacientes):
                    print("Consulta marcada com sucesso!")
                else:
                    print("Consulta não marcada.")  
            if opc == 2:         
                if alterarConsulta(consultas):
                    print("Consulta alterada com sucesso!")                
                else:
                    print("Consulta inválida.")           
            elif opc == 3:
                excluirConsulta(consultas)    
            elif opc == 4:
                listarConsulta(consultas)
            elif opc == 5:
                listarTodasConsultas(consultas)
            elif opc == 6:
                print("Voltando para o menu principal...")

        elif opcao == 4:
            print("1. Mostrar medicos com a especialização X")
            print("2. Mostrar pacientes menores de X idade")
            print("3. Mostrar o CRM, o nome do médico, o CPF do paciente, o nome do paciente, data, hora, diagnostico e medicamentos para todas as consultas realizadasnos últimos X dias")
            print("4. Voltar")
            opc = int(input("Qual opção você deseja? "))   

            if opc == 1:
                especializacao = str(input("Informe a especialização desejada: ")).lower()
                medicosEspecilizacaoX(medicos, especializacao)

            elif opc == 2:
                idade = int(input("Informe a idade máxima dos pacientes que deseja ver: "))
                pacientesMenoresXIdade(pacientes, idade)
            elif opc == 3:
                ultimosDias = int(input("Informe de quantos dias atrás deseja ver consultas: "))
                mostrarConsultasNosUltimosXDias(medicos, pacientes, consultas, ultimosDias)
            elif opc == 4:
                print("Voltando para o menu principal...")

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

main()