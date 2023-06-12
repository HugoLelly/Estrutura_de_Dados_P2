from time import sleep
from limparterminal import limpar_terminal


def consultar_animais():
    limpar_terminal()
    print("\tCONSULTA DE ANIMAIS\n")

    campo_consulta = input("\tDigite a Consulta: ")
    campo_consulta = campo_consulta.lower()

    animais_encontrados = []

    with open("animais.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            especie, raca, idade, cor, particularidades = linha.strip().split(",")
            if campo_consulta == "" or campo_consulta in especie.lower() or campo_consulta in raca.lower() or campo_consulta in idade.lower() or campo_consulta in cor.lower() or campo_consulta in particularidades.lower():
                animais_encontrados.append(
                    (especie, raca, idade, cor, particularidades))

    limpar_terminal()
    print("\tCONSULTA DE ANIMAIS\n")
    print(f"\t{len(animais_encontrados)} Animais Encontrados:")
    sleep(1.5)
    for animal in animais_encontrados:
        sleep(0.5)
        print(f"\tEspécie: {animal[0]}")
        print(f"\tRaça: {animal[1]}")
        print(f"\tIdade (Meses): {animal[2]}")
        print(f"\tCor: {animal[3]}")
        print(f"\tParticularidades: {animal[4]}")
        sleep(0.5)
        print("\t----------------------------------")

    sleep(1.5)
    input("\n\tPressione Enter para voltar ao menu principal.")
    limpar_terminal()
    return
