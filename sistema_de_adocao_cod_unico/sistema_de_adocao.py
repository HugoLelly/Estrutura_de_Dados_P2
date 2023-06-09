import os
from time import sleep


# Função para verificar se os arquivos txt existem. Se não existirem, serão criados.
def verificar_arquivos():
    if not os.path.exists("animais.txt"):
        with open("animais.txt", "w", encoding="utf-8"):
            pass

    if not os.path.exists("candidatos.txt"):
        with open("candidatos.txt", "w", encoding="utf-8"):
            pass

verificar_arquivos()

# Função para limpar o terminal
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

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
            nome = input("\tNome: ")
            telefone = input("\tTelefone: ")
            email = input("\tE-mail: ")
            bairro = input("\tBairro: ")
            especie_interesse = input("\tEspécie de interesse: ")
            particularidades_interesse = input("\tParticularidades de interesse: ")
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
            return

        else:
            limpar_terminal()
            print("\n\tOpção Inválida!\n\tAguarde...")
            sleep(1.5)
            limpar_terminal()

class Nodo_Animal:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEncadeada1:
    def __init__(self):
        self.head = None

    def adicionar_animais(self, data):
        animal_nodo = Nodo_Animal(data)
        if self.head is None:
            self.head = animal_nodo
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = animal_nodo

    def pesquisar_animais(self, campo_consulta):
        resultados_animal = []
        atual = self.head
        while atual:
            # Lógica de pesquisa aqui (por exemplo, pesquisa binária)
            if campo_consulta.lower() in atual.data[0].lower() or campo_consulta.lower() in atual.data[1].lower() or campo_consulta.lower() in atual.data[2].lower() or campo_consulta.lower() in atual.data[3].lower() or campo_consulta.lower() in atual.data[4].lower():
                resultados_animal.append(atual.data)
            atual = atual.next
        return resultados_animal

# Função para consultar animais cadastrados
def consultar_animais():
    limpar_terminal()
    print("\tCONSULTA DE ANIMAIS\n")

    campo_consulta = input("\tDigite a Consulta: ")
    campo_consulta = campo_consulta.lower()

    animais = ListaEncadeada1()

    with open("animais.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            especie, raca, idade, cor, particularidades = linha.strip().split(",")
            animais.adicionar_animais((especie, raca, idade, cor, particularidades))

    animais_encontrados = animais.pesquisar_animais(campo_consulta)

    limpar_terminal()
    print("\tCONSULTA DE ANIMAIS\n")
    print(f"\t{len(animais_encontrados)} Animais Encontrados:")
    print("\t----------------------------------\n")
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

class Nodo_Candidato:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEncadeada2:
    def __init__(self):
        self.head = None

    def adicionar_candidato(self, data):
        candidato_nodo = Nodo_Candidato(data)
        if self.head is None:
            self.head = candidato_nodo
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = candidato_nodo

    def pesquisar_candidato(self, campo_consulta):
        resultados = []
        atual = self.head
        while atual:
            # Lógica de pesquisa aqui (por exemplo, pesquisa binária)
            if campo_consulta.lower() in atual.data[0].lower() or campo_consulta.lower() in atual.data[1].lower() or campo_consulta.lower() in atual.data[2].lower() or campo_consulta.lower() in atual.data[3].lower() or campo_consulta.lower() in atual.data[4].lower() or campo_consulta.lower() in atual.data[5].lower():
                resultados.append(atual.data)
            atual = atual.next
        return resultados

# Função para consultar candidatos cadastrados
def consultar_candidatos():
    limpar_terminal()
    print("\tCONSULTA DE CANDIDATOS\n")

    campo_consulta = input("\tDigite a Consulta: ")
    campo_consulta = campo_consulta.lower()

    candidatos = ListaEncadeada2()

    with open("candidatos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, telefone, email, bairro, especie_interesse, particularidades_interesse = linha.strip().split(",")
            candidatos.adicionar_candidato((nome, telefone, email, bairro, especie_interesse, particularidades_interesse))

    candidatos_encontrados = candidatos.pesquisar_candidato(campo_consulta)

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

# Função para combinar interesses de candidatos e animais
def combinar_interesses():
    limpar_terminal()
    print("\tCOMBINAÇÕES\n")
    sleep(1.5)
    print("\tCombinações Encontradas")
    print("\t-----------------------\n")
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
    print(f"\n\t{len(candidatos_encontrados)} Candidatos Encontrados:\n")
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

# Função para exibir informações sobre o sistema
def exibir_sobre():
    limpar_terminal()
    print("\tSISTEMA DE ADOÇÃO DE ANIMAIS")
    print("\n\tDesenvolvido por:\n\tHUGO LELY DE LIMA MARINHO\n")
    sleep(5)
    limpar_terminal()
    print("\tUNIVERSIDADE DE VASSOURAS")
    print("\t  CAMPUS MARICÁ")
    sleep(1.5)
    print("\tCURSO:")
    print("\t  ENGENHARIA DE SOFTWARE")
    sleep(1.5)
    print("\tDISCIPLINA:")
    print("\t  ESTRUTURA DE DADOS")
    sleep(1.5)
    print("\tPROFESSOR:")
    print("\t  MÁRCIO GARRIDO")
    sleep(1.5)
    print("\tTÍTULO:")
    print("\t  P2 - SISTEMA DE ADOÇÃO DE ANIMAIS")
    sleep(1.5)
    print("\tTURMA:")
    print("\t  2022.1 – TURMA A")
    sleep(1.5)
    print("\tMATRÍCULA:")
    print("\t  202211182")
    sleep(1.5)
    print("\tALUNO:")
    print("\t  HUGO LELY DE LIMA MARINHO")
    sleep(10)
    print("\n\tSaindo do Sobre!\n\tAguarde...")
    sleep(1.5)
    limpar_terminal()

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
