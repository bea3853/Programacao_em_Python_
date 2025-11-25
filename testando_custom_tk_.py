import sqlite3 
import tkinter as tk 
from tkinter import messagebox 
from tkinter import ttk 
import customtkinter


def conectar():
    return sqlite3.connect('teste.db')


def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
              
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL              
        )       
    ''')
    conn.commit()
    conn.close()
  

# CREATE
def inserir_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    cpf =  entry_cpf.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id,nome, email) VALUES(?,?,?)', (cpf,nome, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 

# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2]))
    conn.close()    


# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()

    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  

# UPDATE    
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_email = entry_email.get()

         if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , email = ? WHERE id = ? ',(novo_nome,novo_email,user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')


janela = customtkinter.CTk()
janela.title('CRUD')
janela.geometry('800x630')
janela.configure(bg =  'gray')
customtkinter.set_appearance_mode("dark")

# inserindo icones com o tkinter 

caminho_icone = "meu.ico"
janela.iconbitmap(caminho_icone)

label_nome = customtkinter.CTkLabel(janela, text='Nome:', font=('arial', 15))
label_nome.grid(row=0, column=0, padx=10, pady=10)

entry_nome = customtkinter.CTkEntry(janela, placeholder_text="Nome")
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_email = customtkinter.CTkLabel(janela, text = 'E-mail:', font=('arial', 15))
label_email.grid(row=1, column=0, padx=10, pady=10)

entry_email = customtkinter.CTkEntry(janela, placeholder_text='E-mail')
entry_email.grid(row=1, column=1, padx=10, pady=10)



label_CPF = customtkinter.CTkLabel(janela, text = 'CPF:', font=('arial', 15))
label_CPF.grid(row=2, column=0, padx=10, pady=10)

entry_cpf = customtkinter.CTkEntry(janela,placeholder_text="CPF")
entry_cpf.grid(row=2, column=1, padx=10, pady=10)


fr =  customtkinter.CTkFrame(janela)
fr.grid(columnspan=2)


btn_salvar = customtkinter.CTkButton(fr, text='Salvar', command=inserir_usuario, fg_color='green')
btn_salvar.grid(row=3, column=0, padx=10, pady=10)

btn_deletar = customtkinter.CTkButton(fr, text='deletar', command=delete_usuario, fg_color='green' )
btn_deletar.grid(row=3, column=2, padx=10, pady=10)

btn_atualizar = customtkinter.CTkButton(fr, text='atualizar', command=editar, fg_color='green')
btn_atualizar.grid(row=3, column=3, padx=10, pady=10)

# frame da treeview
fr2 = ttk.Frame(janela)
fr2.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew') 


scrollbar = ttk.Scrollbar(fr2, orient='vertical')

# Treeview: Ligada à Scrollbar. Mestra é o fr2.
columns = ('ID', 'NOME', 'E-MAIL')
tree = ttk.Treeview(fr2, columns=columns, show='headings', yscrollcommand=scrollbar.set, height=40)


scrollbar.config(command=tree.yview)


tree.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

# Scrollbar na Coluna 1 (ao lado), grudada N-S
scrollbar.grid(row=0, column=1, sticky='ns')


#  coluna 0 do FRAME (Treeview) se expandi
fr2.grid_columnconfigure(0, weight=1) 

# Faz a linha 0 do FRAME se expandir
fr2.grid_rowconfigure(0, weight=1)     

# Faz a coluna/linha da JANELA principal se expandir
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1) # Permite a expansão dos inputs/botões
janela.grid_rowconfigure(4, weight=1) # Faz a linha da Treeview se expandir verticalmente


for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER) # Centraliza o texto nas colunas


criar_tabela()
mostrar_usuario()

janela.mainloop()