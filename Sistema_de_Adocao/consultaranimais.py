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
            if campo_consulta.lower() in atual.data[0].lower() or campo_consulta.lower() in atual.data[1].lower() or campo_consulta.lower() in atual.data[2].lower() or campo_consulta.lower() in atual.data[3].lower() or campo_consulta.lower() in atual.data[4].lower():
                resultados.append(atual.data)
            atual = atual.next
        return resultados

# Função para consultar animais cadastrados
def consultar_animais():
    limpar_terminal()
    print("\tCONSULTA DE ANIMAIS\n")

    campo_consulta = input("\tDigite a Consulta: ")
    campo_consulta = campo_consulta.lower()

    animais = ListaEncadeada()

    with open("animais.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            especie, raca, idade, cor, particularidades = linha.strip().split(",")
            animais.adicionar_elemento((especie, raca, idade, cor, particularidades))

    animais_encontrados = animais.pesquisar_elemento(campo_consulta)

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
