from time import sleep
from limparterminal import limpar_terminal

# Função para cadastrar animais
def cadastrar_animal():
    limpar_terminal()

    while True:
        print("\tCADASTRO DE ANIMAIS\n")
        print("\tDeseja Cadastrar Um Novo Animal?\n")

        opcao = input("\n\t1 - Sim\n\t2 - Não\n\n\tDigite a Opção Desejada: ")

        if opcao == "1":
            limpar_terminal()
            print("\tAbrindo Cadastro...")
            sleep(1.5)
            limpar_terminal()
            print("\tCADASTRAR NOVO ANIMAL")
            print("\n\tInforme os Dados do Animal:\n")
            sleep(1.5)
            especie = input("\tEspécie: ")
            raca = input("\tRaça: ")
            idade = input("\tIdade (meses): ")
            cor = input("\tCor: ")
            particularidades = input("\tParticularidades: ")
            sleep(1.5)

            with open("animais.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{especie},{raca},{idade},{cor},{particularidades}")

            print("\n\tCadastro Realizado com Sucesso!")
            sleep(1.5)
            limpar_terminal()

        elif opcao == "2":
            limpar_terminal()
            print("\tSaindo do Cadastro!\n\tAguarde...")
            sleep(1.5)
            limpar_terminal()
            return

        else:
            limpar_terminal()
            print("\tOpção Inválida!\n\tAguarde...")
            sleep(1.5)
            limpar_terminal()
