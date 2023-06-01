import os
from time import sleep

cad_especie = []
cad_raca = []
cad_idade = []
cad_cor = []
cad_porte = []
cad_particularidades = []

def cadastro_animal():
    print("\n\tCADASTRO ANIMAL")
    sair = True
    while sair:
        cad_an = str(input(f"\n\tDeseja Cadastrar um Animal?\n\t[S] Sim \n\t[N] Não: "))
        if cad_an == "S" or cad_an == "s":
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
            sleep(3)
            os.system('clear') or None
            print(f"\n\tEspécie: {cad_especie} \n\tRaça: {cad_raca} \n\tIdade: {cad_idade} \n\tCor: {cad_cor} \n\tPorte: {cad_porte} \n\tParticularidades: {cad_particularidades}")
            sleep(3)
            os.system('clear') or None
        elif cad_an == "N" or cad_an == "n":
            print(f"\n\tSaindo do Cadastro!\n\taguarde...")
            sleep(3)
            os.system('clear') or None
            menu()
        else:
            print(f"\n\tOpção Inválida!\n\taguarde...")
            sleep(3)
            os.system('clear') or None

def cadastro_candidatos():
    print("\n\tCADASTRO DOS CANDIDATOS PARA ADOÇÃO")
    sleep(3)
    os.system('clear') or None
    menu()

def consulta():
    print("\n\tCONSULTA DOS ANIMAIS PARA ADOÇÃO")
    sleep(3)
    os.system('clear') or None
    menu()

def menu():
    print(f"\n\tBEM VINDO AO SISTEMA DE ADOÇÃO DE ANIMAIS\n\tEscolha uma das opções abaixo:\n\t[1] Cadastrar Animal\n\t[2] Cadastrar Candidatos\n\t[3] Consultar Animais para Adoção\n\t[4] Sair do Sistema")
    opcao = int(input(f"\n\tInforme a opção desejada: "))
    if opcao == 1:
        cadastro_animal()
    elif opcao == 2:
        cadastro_candidatos()
    elif opcao == 3:
        consulta()
    elif opcao == 4:
        print(f"\n\tSaindo do Sistema!\n\taguarde...")
        sleep(3)
        os.system('clear') or None
    else:
        print(f"\n\tOpção Inválida!\n\taguarde...")
        sleep(3)
        os.system('clear') or None

menu()
