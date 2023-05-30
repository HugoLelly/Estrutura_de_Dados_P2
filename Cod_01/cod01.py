cad_cand = str(print("\n\tCADASTRO DOS ANIMAIS\n"))
sair = True
candmat = []
candname = []
while sair:
    conf_cand = str(input("\n\tDeseja cadastrar um animal?\nDigite 'S' para cadastrar ou 'N' para sair:\n"))
    if conf_cand == "S" or conf_cand == "s":
        name = str(input("Nome do Candidato : \n"))
        candname.append (name)
        numero = int(input("Matricula do Candidato : \n"))
        candmat.append (numero)
        print(candname,"\n",candmat)
        print("Cadastro realizado: \n")
    elif conf_cand == "N" or conf_cand == "n":
        print("Fim do Cadastros.\n")
        sair = False
    else:
        print("Opção Invalida\n")

print("Candidatos Cadastrados.",candname,candmat)
