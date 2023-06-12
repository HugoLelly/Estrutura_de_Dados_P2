from time import sleep
from limparterminal import limpar_terminal

# Função para consultar candidatos cadastrados
def consultar_candidatos():
    limpar_terminal()
    print("\tCONSULTA DE CANDIDATOS\n")

    campo_consulta = input("\tDigite a Consulta: ")
    campo_consulta = campo_consulta.lower()

    candidatos_encontrados = []

    with open("candidatos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, telefone, email, bairro, especie_interesse, particularidades_interesse = linha.strip().split(",")
            if campo_consulta == "" or campo_consulta in nome.lower() or campo_consulta in telefone.lower() or campo_consulta in email.lower() or campo_consulta in bairro.lower() or campo_consulta in especie_interesse.lower() or campo_consulta in particularidades_interesse.lower():
                candidatos_encontrados.append(
                    (nome, telefone, email, bairro, especie_interesse, particularidades_interesse))

    limpar_terminal()
    print("\tCONSULTA DE CANDIDATOS\n")
    print(f"\t{len(candidatos_encontrados)} Candidatos Encontrados:")
    print("\t----------------------------------\n")
    sleep(1.5)

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
