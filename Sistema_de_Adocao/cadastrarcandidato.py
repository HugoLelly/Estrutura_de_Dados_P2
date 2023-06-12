from time import sleep
from limparterminal import limpar_terminal

# Função para cadastrar candidatos
def cadastrar_candidato():
    limpar_terminal()

    while True:
        print("\tCADASTRO DE CANDIDATOS\n")
        print("\tDeseja Cadastrar Um Novo Candidato?\n")

        opcao = input("\n\t1 - Sim\n\t2 - Não\n\n\tDigite a Opção Desejada: ")

        if opcao == "1":
            limpar_terminal()
            print("\tAbrindo Cadastro...")
            sleep(1.5)
            limpar_terminal()
            print("\tCADASTRO DE CANDIDATOS")
            print("\n\tInforme os Dados do Candidato:\n")
            sleep(1.5)
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            bairro = input("Bairro: ")
            especie_interesse = input("Espécie de interesse: ")
            particularidades_interesse = input("Particularidades de interesse: ")
            sleep(1.5)

            with open("candidatos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{nome},{telefone},{email},{bairro},{especie_interesse},{particularidades_interesse}")

            print("\n\tCadastro Realizado com Sucesso!")
            sleep(1.5)
            limpar_terminal()

        elif opcao == "2":
            limpar_terminal()
            print("\n\tSaindo do Cadastro!\n\tAguarde...")
            sleep(1.5)
            limpar_terminal()

        else:
            limpar_terminal()
            print("\n\tOpção Inválida!\n\tAguarde...")
            sleep(1.5)
            limpar_terminal()
