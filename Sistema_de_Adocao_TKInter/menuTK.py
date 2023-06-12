from tkinter import Button, Entry, Label, Tk, messagebox

from verificararquivosTK import verificar_arquivos

from cadastrarcandidato import cadastrar_candidato
from consultaranimais import consultar_animais
from consultarcandidatos import consultar_candidatos
from combinarinteresses import combinar_interesses
from exibirsobre import exibir_sobre


def abrir_cadastro_candidatos():
    messagebox.showinfo("Aguarde...", "Abrindo o Cadastro de Candidatos")
    cadastrar_candidato()

def abrir_consulta_animais():
    messagebox.showinfo("Aguarde...", "Abrindo a Consulta de Animais")
    consultar_animais()

def abrir_consulta_candidatos():
    messagebox.showinfo("Aguarde...", "Abrindo a Consulta de Candidatos")
    consultar_candidatos()

def abrir_combinacoes():
    messagebox.showinfo("Aguarde...", "Abrindo as Combinações")
    combinar_interesses()

def abrir_sobre():
    messagebox.showinfo("Aguarde...", "Abrindo o Sobre")
    exibir_sobre()

def sair():
    messagebox.showinfo("Saindo do Sistema", "Obrigado por utilizar o Sistema de Adoção de Animais")
    exit()

def voltar():
    menu()

def adastrar_candidato():
            nome = nome_entry.get()
            telefone = telefone_entry.get()
            email = email_entry.get()
            bairro = barrio_entry.get()
            especie_interesse = especie_interesse_entry.get()
            particularidades_interesse = particularidades_interesse_entry.get()
        
            with open("candidatos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{nome},{telefone},{email},{bairro},{especie_interesse},{particularidades_interesse}")

            print("\n\tCadastro Realizado com Sucesso!")
            
            messagebox.showinfo("Aguarde...", "Cadastro Realizado com Sucesso!")
            cadastro_window.destroy()
            cadastrar_candidato_window = Tk()
            cadastrar_candidato_window.title("Cadastro de Candidatos")
            cadastrar_candidato_window.geometry("960x500")
            cadastrar_candidato_window.resizable(False, False)

    label = Label(cadastrar_candidato_window, text="CADASTRAR NOVO CANDIDATO", font=("Helvetica", 16))
    label.pack(pady=10)

    nome_label = Label(cadastrar_candidato_window, text="Nome:")
    nome_label.pack()
    nome_entry = Entry(cadastrar_candidato_window)
    nome_entry.pack()

    telefone_label = Label(cadastrar_candidato_window, text="Telefone:")
    telefone_label.pack()
    telefone_entry = Entry(cadastrar_candidato_window)
    telefone_entry.pack()

    email_label = Label(cadastrar_candidato_window, text="E-mail:")
    email_label.pack()
    email_entry = Entry(cadastrar_candidato_window) 
    email_entry.pack()

    bairro_label = Label(cadastrar_candidato_window, text="Bairro:")
    bairro_label.pack()
    bairro_entry = Entry(cadastrar_candidato_window)
    bairro_entry.pack()

    especie_interesse_label = Label(cadastrar_candidato_window, text="Espécie de Interesse:")
    especie_interesse_label.pack()
    especie_interesse_entry = Entry(cadastrar_candidato_window)
    especie_interesse_entry.pack()

    particularidades_interesse_label = Label(cadastrar_candidato_window, text="Particularidades de Interesse:")
    particularidades_interesse_label.pack()
    particularidades_interesse_entry = Entry(cadastrar_candidato_window)
    particularidades_interesse_entry.pack()

    cadastrar_button = Button(cadastrar_candidato_window, text="Cadastrar", command=cadastrar)
    cadastrar_button.pack(pady=10)

    cadastrar_candidato_window.mainloop()


def cadastrar_animal():
    def cadastrar():
        especie = especie_entry.get()
        raca = raca_entry.get()
        idade = idade_entry.get()
        cor = cor_entry.get()
        particularidades = particularidades_entry.get()

        with open("animais.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{especie},{raca},{idade},{cor},{particularidades}\n")

        messagebox.showinfo("Aguarde...", "Cadastro Realizado com Sucesso!")
        cadastro_window.destroy()

    cadastro_window = Tk()
    cadastro_window.title("Cadastro de Animais")
    cadastro_window.geometry("960x500")
    cadastro_window.resizable(False, False)

    label = Label(cadastro_window, text="CADASTRAR NOVO ANIMAL", font=("Helvetica", 16))
    label.pack(pady=10)

    especie_label = Label(cadastro_window, text="Espécie:")
    especie_label.pack()
    especie_entry = Entry(cadastro_window)
    especie_entry.pack()

    raca_label = Label(cadastro_window, text="Raça:")
    raca_label.pack()
    raca_entry = Entry(cadastro_window)
    raca_entry.pack()

    idade_label = Label(cadastro_window, text="Idade (meses):")
    idade_label.pack()
    idade_entry = Entry(cadastro_window)
    idade_entry.pack()

    cor_label = Label(cadastro_window, text="Cor:")
    cor_label.pack()
    cor_entry = Entry(cadastro_window)
    cor_entry.pack()

    particularidades_label = Label(cadastro_window, text="Particularidades:")
    particularidades_label.pack()
    particularidades_entry = Entry(cadastro_window)
    particularidades_entry.pack()

    cadastrar_button = Button(cadastro_window, text="Cadastrar", command=cadastrar)
    cadastrar_button.pack(pady=10)

    sair_button = Button(cadastro_window, text="Voltar", command=voltar)
    sair_button.pack(pady=5)

    cadastro_window.mainloop()



verificar_arquivos()

def menu():
    main = Tk()
    main.title("Sistema de Adoção de Animais")
    main.geometry("960x500")
    main.resizable(False, False)

    texto1 = Label(main, text="BEM VINDO AO SISTEMA DE ADOÇÃO DE ANIMAIS", font=("Helvetica", 16))
    texto1.pack(pady=20, padx=20)

    button1 = Button(main, text="Cadastrar Animais", command=cadastrar_animal)
    button1.pack(pady=5, padx=5)

    button2 = Button(main, text="Cadastrar Candidatos", command=abrir_cadastro_candidatos)
    button2.pack(pady=5, padx=5)

    button3 = Button(main, text="Consultar Animais Cadastrados", command=abrir_consulta_animais)
    button3.pack(pady=5, padx=5)

    button4 = Button(main, text="Consultar Candidatos Cadastrados", command=abrir_consulta_candidatos)
    button4.pack(pady=5, padx=5)

    button5 = Button(main, text="Realizar Combinações", command=abrir_combinacoes)
    button5.pack(pady=5, padx=5)

    button6 = Button(main, text="Sobre", command=abrir_sobre)
    button6.pack(pady=5, padx=5)

    button7 = Button(main, text="Sair", command=sair)
    button7.pack(pady=5, padx=5)

    main.mainloop()

menu()
