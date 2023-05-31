import os
from time import sleep

cad_especie = []
cad_raca = []
cad_idade = []
cad_cor = []
cad_porte = []
cad_particularidades = []

def cadastro_animal():
    cad_animal = str(print("\n\tCADASTRO ANIMAL"))
    sair = True
    while sair:
        cad_an = str(input(f"\n\tDeseja Cadastrar um Animal?\n\t[S] Sim [N] Não: "))
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
        else:
            print(f"\n\tOpção Inválida!\n\taguarde...")
            sleep(3)
            os.system('clear') or None

def consulta():
    consulta_animal = str(print("\n\tCONSULTA ANIMAL"))
    sair = True
    while sair:
