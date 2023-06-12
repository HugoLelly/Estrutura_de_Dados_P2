from time import sleep
from limparterminal import limpar_terminal

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def adicionar_elemento(self, data):
        novo_nodo = Nodo(data)
        if self.head is None:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = novo_nodo

    def pesquisar_elemento(self, campo_consulta):
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

    candidatos = ListaEncadeada()

    with open("candidatos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, telefone, email, bairro, especie_interesse, particularidades_interesse = linha.strip().split(",")
            candidatos.adicionar_elemento((nome, telefone, email, bairro, especie_interesse, particularidades_interesse))

    candidatos_encontrados = candidatos.pesquisar_elemento(campo_consulta)

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
