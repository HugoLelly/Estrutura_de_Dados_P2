import os

# Função para limpar o terminal
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    return
