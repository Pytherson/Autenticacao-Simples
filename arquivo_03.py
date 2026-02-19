from rich import print
from rich import inspect
import os

class ValidadorCadastro:
    """Autenticação Simples"""
    def __init__(self, email, senha):
        self.__email_correto = email
        self.__senha_correta = senha


    def validar_usuario(self):
        try:
            email = input("Digite seu email: ")
            senha = int(input("Digite sua senha: "))

            if email.lower().strip() == self.__email_correto and senha == self.__senha_correta:
                os.system("cls")
                print(":white_check_mark:[green] Email e Senha Correta![/]")

            else:
                os.system("cls")
                print(":x:[red] Email ou Senha incorreto![/]")
        except:
            os.system("cls")
            print(":thumbs_down:[yellow] Erro: A senha deve conter apenas números![/]")



v1 = ValidadorCadastro("pyther@gmail.com", 123456)
v1.validar_usuario()
inspect(v1)

