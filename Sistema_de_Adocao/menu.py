from time import sleep
from limparterminal import limpar_terminal
from cadastraranimal import cadastrar_animal
from cadastrarcandidato import cadastrar_candidato
from consultaranimais import consultar_animais
from consultarcandidatos import consultar_candidatos
from combinarinteresses import combinar_interesses
from exibirsobre import exibir_sobre
from verificararquivos import verificar_arquivos

verificar_arquivos()

# Função principal
def main():
    limpar_terminal()
    while True:
        print("\tBEM VINDO AO SISTEMA DE ADOÇÃO DE ANIMAIS")
        print("\n\tEscolha uma Opção:\n")
        print("\t1 - Cadastrar Animais")
        print("\t2 - Cadastrar Candidatos")
        print("\t3 - Consultar Animais Cadastrados")
        print("\t4 - Consultar Candidatos Cadastrados")
        print("\t5 - Realizar Combinações")
        print("\t6 - Sobre")
        print("\t7 - Sair")
        opcao = input("\n\tDigite a opção desejada: ")
        if opcao == "1":
            limpar_terminal()
            print("\tAbrindo o Cadastro de Animais")
            sleep(1.5)
            cadastrar_animal()
        elif opcao == "2":
            limpar_terminal()
            print("\tAbrindo o Cadastro de Candidatos")
            sleep(1.5)
            cadastrar_candidato()
        elif opcao == "3":
            limpar_terminal()
            print("\tAbrindo a Consulta de Animais")
            sleep(1.5)
            consultar_animais()
        elif opcao == "4":
            limpar_terminal()
            print("\tAbrindo a Consulta dos Candidatos")
            sleep(1.5)
            consultar_candidatos()
        elif opcao == "5":
            limpar_terminal()
            print("\tAbrindo as Combinações")
            sleep(1.5)
            combinar_interesses()
        elif opcao == "6":
            limpar_terminal()
            print("\tAbrindo o Sobre")
            sleep(1.5)
            exibir_sobre()
        elif opcao == "7":
            limpar_terminal()
            print("\tSaindo do Sistema\n\tAguarde...")
            sleep(1.5)
            limpar_terminal()
            print("\tOBRIADO POR UTILIZAR O\n\tSISTEMA DE ADOÇÃO DE ANIMAIS")
            print("\n\t🐶😺🐮🐰")
            sleep(3)
            exit()
        else:
            limpar_terminal()
            print("\tOpção inválida!\n\tAgurade...")
            sleep(1.5)
            limpar_terminal()

if __name__ == "__main__":
    main()
