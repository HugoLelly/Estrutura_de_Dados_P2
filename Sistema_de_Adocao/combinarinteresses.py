from time import sleep
from limparterminal import limpar_terminal

def combinar_interesses():
    limpar_terminal()
    print("\tBEM VINDO AS COMBINAÇÕES DE INTERESSES\n")
    sleep(1.5)
    print("\tCombinações Encontradas")
    sleep(1.5)

    animais = []
    candidatos = []

    with open("animais.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            especie, raca, idade, cor, particularidades = linha.strip().split(",")
            animais.append((especie, raca, idade, cor, particularidades))

    with open("candidatos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, telefone, email, bairro, especie_interesse, particularidades_interesse = linha.strip().split(",")
            candidatos.append((nome, telefone, email, bairro, especie_interesse, particularidades_interesse))

    animais_encontrados = []
    candidatos_encontrados = []

    for animal in animais:
        for candidato in candidatos:
            if animal[0].lower() == candidato[4].lower() and animal[4].lower() == candidato[5].lower():
                animais_encontrados.append(animal)
                candidatos_encontrados.append(candidato)

    print(f"\n\t{len(animais_encontrados)} Animais Encontrados:\n")
    print("\t----------------------------------")
    for animal in animais_encontrados:
        sleep(0.5)
        print(f"\tEspécie: {animal[0]}")
        print(f"\tRaça: {animal[1]}")
        print(f"\tIdade: {animal[2]}")
        print(f"\tCor: {animal[3]}")
        print(f"\tParticularidades: {animal[4]}")
        sleep(0.5)
        print("\t----------------------------------")


    sleep(1.5)

    print("\n\t{len(candidatos_encontrados)} Candidatos Encontrados:\n")
    print("\t----------------------------------")
    for candidato in candidatos_encontrados:
        sleep(0.5)
        print(f"\tNome: {candidato[0]}")
        print(f"\tTelefone: {candidato[1]}")
        print(f"\tE-mail: {candidato[2]}")
        print(f"\tBairro: {candidato[3]}")
        print(f"\tEspécie de Interesse: {candidato[4]}")
        print(f"\tParticularidades de Interesse: {candidato[5]}")
        sleep(0.5)
        print("\t----------------------------------")

    sleep(1.5)
    input("\n\tPressione Enter para voltar ao menu principal.")
    limpar_terminal()
    return
