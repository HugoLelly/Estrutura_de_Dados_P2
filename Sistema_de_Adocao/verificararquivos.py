import os

# Função para verificar se os arquivos txt existem. Se não existirem, serão criados.
def verificar_arquivos():
    if not os.path.exists("animais.txt"):
        with open("animais.txt", "w", encoding="utf-8"):
            pass

    if not os.path.exists("candidatos.txt"):
        with open("candidatos.txt", "w", encoding="utf-8"):
            pass
