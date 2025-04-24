#IMPORTS-----------------------------------------------------------------------------
from tkinter import Listbox,END,messagebox
from pathlib import Path

try:
    import customtkinter as ctk
except ImportError:
    print(f"Biblioteca customtkinter não encontrada.")
    exit(1)

try:
    from PIL import Image
    utilizar_imagem = True
except:
    print("Biblioteca PIL não encontrada.")
    utilizar_imagem = False

#-------------------------------------------------------------------------------------------------------------
# JANELA -------------------------------------------------------------------------------------------------------
janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.title("Lista de tarefas - 1.0")
janela.geometry("650x950")
janela.resizable(False,False)

        
#---------------------------------------------------------------------------------------------------------------
# TITULO -------------------------------------------------------------------------------------------------------
titulo = ctk.CTkLabel(janela,
                      text="Agenda de Contatos",
                      font=("verdana", 30, "bold"),
                      text_color="white",
                      )
titulo.pack(padx=20,pady=20)

#-------------------------------------------------------------------------------------------------------------
# IMAGEM ------------------------------------------------------------------------------------------------------
if utilizar_imagem:
    if Path("./logo.png").exists():
        imagem_01_pil = Image.open("logo.png")
        imagem_01_ctkimage = ctk.CTkImage(light_image=imagem_01_pil,dark_image=imagem_01_pil,size=(40,40))
        imagem_01_ctklabel = ctk.CTkLabel(master=janela,image=imagem_01_ctkimage,text="")
        imagem_01_ctklabel.place(x=100,y=17)


#-------------------------------------------------------------------------------------------------------------
# COMANDOS BOTÃO-----------------------------------------------------------------------------------------------
def add_contato():
    n = nome.get()
    t = telefone.get() 
    e = email.get()

    campos_inseridos = True

    if (n):
        nome.delete(0,'end')
        salvar_contatos()
    else:
        campos_inseridos = False
        messagebox.showerror('Erro ' ,'O campo nome esta vazio!')
        

    if (t):
        telefone.delete(0,'end')
        salvar_contatos()
    else:
        campos_inseridos = False
        messagebox.showerror('Erro ' ,'O campo telefone esta vazio!')

    if (e):
        email.delete(0,'end')
        salvar_contatos()
    else:
        campos_inseridos = False
        messagebox.showerror('Erro ' ,'O campo email esta vazio!')

    if campos_inseridos:
        concatenar = f"NOME: {n}, TELEFONE: {t}, EMAIL: {e}"
        listbox.insert(0,concatenar)
        salvar_contatos()

def del_contato():
    selecionada = listbox.curselection()
    if (selecionada):
        listbox.delete(selecionada)
        salvar_contatos()
    else:
        messagebox.showerror('Erro ' ,' Nenhum contato foi selecionado!') 

#-------------------------------------------------------------------------------------------------------------
# LOCAL STORAGE ----------------------------------------------------------------------------------------------

def salvar_contatos():
    with open('dados.txt','w') as d:
        contatos = listbox.get(0, END)
        for x in contatos:
            d.write(x+'\n')

def carregar_contatos():
    with open('dados.txt', 'r') as d:
        linhas = d.readlines()
        for x in linhas:
            listbox.insert(0 , x.strip())

#-----------------------------------------------------------------------------------------------------------------
# INPUTS ------------------------------------------------------------------------------------------------------------

nome = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='dimgrey',
                      placeholder_text='Digite um nome',
                      )
nome.pack(pady=10)

telefone = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='dimgrey',
                      placeholder_text='Digite um numero de telefone',
                      )
telefone.pack(pady=10)

email = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='dimgrey',
                      placeholder_text='Digite um email',
                      )
email.pack(pady=10)

#-------------------------------------------------------------------------------------------------------------------------
# BOTÕES--------------------------------------------------------------------------------------------------------------------
btAdicionar = ctk.CTkButton(janela,
                             width=100,
                             height=40,
                             fg_color='mediumseagreen',
                             hover_color='seagreen',
                             text='Adicionar',
                             font=('verdana',15,'bold'),
                             cursor='hand2',
                             text_color='black',
                             command=add_contato
                             )
btAdicionar.place(x=160,y=300)

btDeletar = ctk.CTkButton(janela,
                             width=100,
                             height=40,
                             fg_color='crimson',
                             hover_color='darkred',
                             text='Remover',
                             font=('verdana',15,'bold'),
                             cursor='hand2',
                             text_color='white',
                             command=del_contato
                             )
btDeletar.place(x=360,y=300)

#--------------------------------------------------------------------------------
# LISTBOX-------------------------------------------------------------------------
listbox = Listbox(janela,
                        width=55,
                        height=29,
                        font=('verdana',12,'bold'),
                        fg='white',
                        background='#323232',
                        highlightbackground='dimgrey',
                        highlightthickness=2,                        
                        )
listbox.place(x=21, y=370)

#-------------------------------------------------------------------------------
# INICIO-------------------------------------------------------------------------
if __name__ == "__main__":
    carregar_contatos()
    janela.mainloop()