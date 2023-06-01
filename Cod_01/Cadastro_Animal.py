import os
from time import sleep

cad_especie = []
cad_raca = []
cad_idade = []
cad_cor = []
cad_porte = []
cad_particularidades = []

cad_can_nome = []
cad_can_telefone = []
cad_can_email = []
cad_can_bairro = []
cad_can_especie = []
cad_can_particularidades = []

def cadastro_animal():
    os.system('cls') or None
    print("\n\tCADASTRO ANIMAL")
    sair = True
    while sair:
        os.system('cls') or None
        cad_an = str(input(f"\n\tDeseja Cadastrar um Animal?\n\t[S] Sim \n\t[N] Não: "))
        if cad_an == "S" or cad_an == "s":
            os.system('cls') or None
            tipo = str(input(f"\n\tInforme a espécie do animal: "))
            cad_especie.append(tipo)
            raca = str(input(f"\n\tInforme a raça do animal: "))
            cad_raca.append(raca)
            idade = str(input(f"\n\tInforme a idade aproximada do animal: "))
            cad_idade.append(idade)
            cor = str(input(f"\n\tInforme a cor do animal: "))
            cad_cor.append(cor)
            porte = str(input(f"\n\tInforme o porte do animal: "))
            cad_porte.append(porte)
            particularidades = str(input(f"\n\tInforme as particularidades do animal: "))
            cad_particularidades.append(particularidades)
            os.system('cls') or None
            sleep(2)
            print(f"\n\tANIMAL CADASTRADO")
            print(f"\n\tEspécie: {cad_especie} \n\tRaça: {cad_raca} \n\tIdade: {cad_idade} \n\tCor: {cad_cor} \n\tPorte: {cad_porte} \n\tParticularidades: {cad_particularidades}")
            sleep(5)
        elif cad_an == "N" or cad_an == "n":
            os.system('cls') or None
            print(f"\n\tSaindo do Cadastro!\n\tAguarde...")
            sleep(3)
            menu()
        else:
            os.system('cls') or None
            print(f"\n\tOpção Inválida!\n\tAguarde...")
            sleep(3)

def cadastro_candidatos():
    os.system('cls') or None
    print("\n\tCADASTRO DOS CANDIDATOS PARA ADOÇÃO")
    sair = True
    while sair:
        os.system('cls') or None
        cad_cand = str(input(f"\n\tDeseja Cadastrar um Candidato?\n\t[S] Sim \n\t[N] Não: "))
        if cad_cand == "S" or cad_cand == "s":
            os.system('cls') or None
            nome = str(input(f"\n\tInforme o nome do candidato: "))
            cad_can_nome.append(nome)
            telefone = str(input(f"\n\tInforme o telefone do candidato: "))
            cad_can_telefone.append(telefone)
            email = str(input(f"\n\tInforme o email do candidato: "))
            cad_can_email.append(email)
            bairro = str(input(f"\n\tInforme o bairro do candidato: "))
            cad_can_bairro.append(bairro)
            especie = str(input(f"\n\tInforme a espécie do animal desejado: "))
            cad_can_especie.append(especie)
            particularidades = str(input(f"\n\tInforme as particularidades do animal desejado: "))
            cad_can_particularidades.append(particularidades)
            os.system('cls') or None
            sleep(2)
            print(f"\n\tCANDIDATO CADASTRADO")
            print(f"\n\tNome: {cad_can_nome} \n\tTelefone: {cad_can_telefone} \n\tEmail: {cad_can_email} \n\tBairro: {cad_can_bairro} \n\tEspécie: {cad_can_especie} \n\tParticularidades: {cad_can_particularidades}")
            sleep(5)
        elif cad_cand == "N" or cad_cand == "n":
            os.system('cls') or None
            print(f"\n\tSaindo do Cadastro!\n\tAguarde...")
            sleep(3)
            menu()
        else:
            os.system('cls') or None
            print(f"\n\tOpção Inválida!\n\tAguarde...")
            sleep(3)

def consulta():
    os.system('cls') or None
    print("\n\tCONSULTA DOS ANIMAIS PARA ADOÇÃO")
    sleep(3)
    menu()

def sobre():
    os.system('cls') or None
    print("\n\tSISTEMA DE ADOÇÃO DE ANIMAIS")
    sleep(1)
    print("\n\tDesenvolvido por:\n\tHUGO LELY DE LIMA MARINHO")
    sleep(1.5)
    os.system('cls') or None
    print("\n\tUNIVERSIDADE DE VASSOURAS")
    sleep(1)
    print("\t  CAMPUS MARICÁ")
    sleep(1.5)
    print("\n\tCURSO:")
    sleep(1)
    print("\t  ENGENHARIA DE SOFTWARE")
    sleep(1.5)
    print("\n\tDISCIPLINA:")
    sleep(1)
    print("\t  ESTRUTURA DE DADOS")
    sleep(1.5)
    print("\n\tPROFESSOR:")
    sleep(1)
    print("\t  MÁRCIO GARRIDO")
    sleep(1.5)
    print("\n\tTÍTULO:")
    sleep(1)
    print("\t  P2 - SISTEMA DE ADOÇÃO DE ANIMAIS")
    sleep(1.5)
    print("\n\tTURMA:")
    sleep(1)
    print("\t  2022.1 – TURMA A")
    sleep(1.5)
    print("\n\tMATRÍCULA:")
    sleep(1)
    print("\t  202211182")
    sleep(1.5)
    print("\n\tALUNO:")
    sleep(1)
    print("\t  HUGO LELY DE LIMA MARINHO")
    sleep(10)
    print("\n\tSaindo do Sobre!\n\tAguarde...")
    sleep(3)
    menu()

def menu():
    os.system('cls') or None
    print(f"\n\tBEM VINDO AO SISTEMA DE ADOÇÃO DE ANIMAIS\n\tEscolha uma das opções abaixo:\n\t[1] Cadastrar Animal\n\t[2] Cadastrar Candidatos\n\t[3] Consultar Animais para Adoção\n\t[4] Sobre\n\t[5] Sair")
    opcao = int(input(f"\n\tInforme a opção desejada: "))
    if opcao == 1:
        os.system('cls') or None
        print("\n\tAbrindo o Cadastro Animal!\n\tAguarde...")
        sleep(2)
        cadastro_animal()
    elif opcao == 2:
        os.system('cls') or None
        print("\n\tAbrindo o Cadastro de Candidatos!\n\tAguarde...")
        sleep(2)
        cadastro_candidatos()
    elif opcao == 3:
        os.system('cls') or None
        print("\n\tAbrindo a Consulta dos Animais para Adoção!\n\tAguarde...")
        sleep(2)
        consulta()
    elif opcao == 4:
        os.system('cls') or None
        print(f"\n\tAbrindo Sobre\n\tAguarde...")
        sleep(2)
        sobre()
    elif opcao == 5:
        os.system('cls') or None
        print(f"\n\tSaindo do Sistema!\n\tAguarde...")
        sleep(2)
        os.system('cls') or None
        print(f"\n\tOBRIADO POR UTILIZAR O\n\tSISTEMA DE ADOÇÃO DE ANIMAIS")
        print(f"\n\t🐶😺🐮🐰")
        sleep(4)
        exit()
    else:
        os.system('cls') or None
        print(f"\n\tOpção Inválida!\n\tAguarde...")
        sleep(2)

menu()
