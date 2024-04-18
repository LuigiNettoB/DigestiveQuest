import customtkinter as ctk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import os

janela= ctk.CTk()

class Jogo():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()
        
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("900x600")
        janela.title("DigestiveQuest")
        
        janela.resizable(False, False)

    def tela_login(self):
    # Obter o caminho absoluto do diretório atual
        current_directory = os.path.dirname(os.path.abspath(__file__))
    # Combinar o caminho absoluto com o nome do arquivo da imagem
        image_path = os.path.join(current_directory, "9027760.png")
        img = PhotoImage(file=image_path)
        label_img = ctk.CTkLabel(master=janela, image=img, text='')
        label_img.place(x=75, y=150)

        label_tt = ctk.CTkLabel(master=janela, text="Entre já na sua conta", font=("Roboto ", 18), text_color="#00B0F0")

        # frame
        frame_login = ctk.CTkFrame(master=janela, width=450, height=700)
        frame_login.pack(side=RIGHT)

        label_login = ctk.CTkLabel(master=frame_login, text="Login", font=("Roboto", 30))
        label_login.place(x=25, y=120)

        login_username_input = ctk.CTkEntry(master=frame_login, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14)).place(x=25, y=205)
        label_login_username = ctk.CTkLabel(master=frame_login, text="O campo nome de usuário é obrigatório *", text_color="gray", font=("Roboto", 11)).place(x=25, y=235)

        login_password_input = ctk.CTkEntry(master=frame_login, placeholder_text="Senha", width=300, font=("Roboto", 14)).place(x=25, y=275)
        label_login_password = ctk.CTkLabel(master=frame_login, text="O campo senha é obrigatório *", text_color="gray", font=("Roboto", 11)).place(x=25, y=305)

        login_checkbox = ctk.CTkCheckBox(master=frame_login, text="Lembrar sempre").place(x=25, y=335)


        def login():
            frame_login.pack_forget()
            label_img.place_forget()
            pass
        login_button = ctk.CTkButton(master=frame_login, text="Login", width=300, fg_color='#7a5c3c', hover_color="#b08e6b", command=login).place(x=25, y=385)


        def tela_cadastro():
            #Remover o frame  de login de usuários
            frame_login.pack_forget()

            #Criando a tela de cadastro de usuários
            frame_cadastro = ctk.CTkFrame(master=janela, width=450, height=700)
            frame_cadastro.pack(side=RIGHT)

            label_login = ctk.CTkLabel(master=frame_cadastro, text="Faça o seu cadastro: ", font=("Roboto", 30))
            label_login.place(x=25, y=90)

            cadastro_nome_input = ctk.CTkEntry(master=frame_cadastro, placeholder_text="Nome Completo", width=300, font=("Roboto", 14)).place(x=25, y=155)
            label_cadastro_nome = ctk.CTkLabel(master=frame_cadastro, text="O campo Nome Completo é obrigatório *", text_color="gray", font=("Roboto", 11)).place(x=25, y=185)


            cadastro_email_input = ctk.CTkEntry(master=frame_cadastro, placeholder_text="Email", width=300, font=("Roboto", 14)).place(x=25, y=215)
            label_cadastro_email = ctk.CTkLabel(master=frame_cadastro, text="O campo Email é obrigatório *", text_color="gray", font=("Roboto", 11)).place(x=25, y=245)

            cadastro_ano_input = ctk.CTkEntry(master=frame_cadastro, placeholder_text="Série", width=300, font=("Roboto", 14)).place(x=25, y=275)
            label_cadastro_ano = ctk.CTkLabel(master=frame_cadastro, text="O campo Série é obrigatório *", text_color="gray", font=("Roboto", 11)).place(x=25, y=305)


            cadastro_turma_input = ctk.CTkEntry(master=frame_cadastro, placeholder_text="Turma", width=300, font=("Roboto", 14)).place(x=25, y=335)
            label_cadastro_turma = ctk.CTkLabel(master=frame_cadastro, text="O campo Turma é obrigatório *", text_color="gray", font=("Roboto", 11)).place(x=25, y=365)
            
            cadastro_senha_input = ctk.CTkEntry(master=frame_cadastro, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*").place(x=25, y=395)
            label_cadastro_senha = ctk.CTkLabel(master=frame_cadastro, text="O campo Senha é obrigatório *", text_color="gray", font=("Roboto", 11),).place(x=25, y=425)
            

            def back():
                #Removendo o frame de cadastro
                frame_cadastro.pack_forget()

                #Devolvendo o frame de login
                frame_login.pack(side=RIGHT)
                pass

            back_button=ctk.CTkButton(master=frame_cadastro, text="Voltar", width=140, fg_color="#b08e6b", command=back).place(x=25, y=455)
            

            def save_user():
                msg= messagebox.showinfo(title="Estado do Cadastro", message="Cadastro concluído com sucesso!")
                pass


            save_button=ctk.CTkButton(master=frame_cadastro, text="Cadastrar", width=140, fg_color='#7a5c3c', command=save_user).place(x=185, y=455)

            pass
        cadastro_button = ctk.CTkButton(master=frame_login, text="Cadastre-se", width=300, fg_color='#b08e6b' , hover_color="#7a5c3c", command=tela_cadastro).place(x=25, y=445)

Jogo()