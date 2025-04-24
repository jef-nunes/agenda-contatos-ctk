#IMPORTS-----------------------------------------------------------------------------
import customtkinter as ctk
from tkinter import Listbox,END,messagebox

#-------------------------------------------------------------------------------------------------------------
#JANELA-------------------------------------------------------------------------------------------------------
janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.title("Lista de tarefas - 1.0")
janela.geometry("650x950")
janela.resizable(False,False)

#-------------------------------------------------------------------------------------------------------------
#COMANDOS BOTÃO-----------------------------------------------------------------------------------------------
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
        messagebox.showerror('Error ' ,'O campo nome esta vazio!!')
        

    if (t):
        telefone.delete(0,'end')
        salvar_contatos()
    else:
        campos_inseridos = False
        messagebox.showerror('Error ' ,'O campo telefone esta vazio!!')

    if (e):
        email.delete(0,'end')
        salvar_contatos()
    else:
        campos_inseridos = False
        messagebox.showerror('Error ' ,'O campo email esta vazio!!')

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
        messagebox.showerror('Error ' ,' Nenhum contato foi selecionada!!') 

#-------------------------------------------------------------------------------------------------------------
# LOCAL STORAGE ----------------------------------------------------------------------------------------------

def salvar_contatos():
    with open('dados.txt','w') as d:
        tarefas = listbox.get(0, END)
        for x in tarefas:
            d.write(x+'\n')

def carregar_contatos():
    with open('dados.txt', 'r') as d:
        tarefas = d.readlines()
        
        for x in tarefas:
            listbox.insert(0 , x.strip())
#---------------------------------------------------------------------------------------------------------------
#-TITULO-------------------------------------------------------------------------------------------------------
titulo = ctk.CTkLabel(janela,
                      text="Agenda",
                      font=("verdana", 40, "bold"),
                      text_color="white",
                      )
titulo.pack()

#-----------------------------------------------------------------------------------------------------------------
#INPUTS------------------------------------------------------------------------------------------------------------

nome = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='hotpink',
                      placeholder_text='Digite um nome',
                      )
nome.pack(pady=10)

telefone = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='hotpink',
                      placeholder_text='Digite um numero de telefone',
                      )
telefone.pack(pady=10)

email = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='hotpink',
                      placeholder_text='Digite um email',
                      )
email.pack(pady=10)

#-------------------------------------------------------------------------------------------------------------------------
#BOTÕES--------------------------------------------------------------------------------------------------------------------
btAdicionar = ctk.CTkButton(janela,
                             width=100,
                             height=40,
                             fg_color='lightgreen',
                             hover_color='darkgreen',
                             text='➕Adicionar tarefa',
                             font=('verdana',15,'bold'),
                             cursor='hand2',
                             text_color='black',
                             command=add_contato
                             )
btAdicionar.place(x=160,y=300)

btDeletar = ctk.CTkButton(janela,
                             width=100,
                             height=40,
                             fg_color='red',
                             hover_color='darkred',
                             text='Deletar tarefa',
                             font=('verdana',15,'bold'),
                             cursor='hand2',
                             text_color='white',
                             command=del_contato
                             )
btDeletar.place(x=360,y=300)

#--------------------------------------------------------------------------------
#LISTBOX-------------------------------------------------------------------------
listbox = Listbox(janela,
                        width=55,
                        height=29,
                        font=('verdana',12,'bold'),
                        fg='white',
                        background='#323232',
                        highlightbackground='hotpink',
                        highlightthickness=2,                        
                        )
listbox.place(x=21, y=370)

#-------------------------------------------------------------------------------
#INICIO-------------------------------------------------------------------------
if __name__ == "__main__":
    carregar_contatos()
    janela.mainloop()