from rich import print
import os
import stdiomask

class ValidadorCadastro:
    """Autenticação Simples"""
    def __init__(self):
        self.__email_correto = "pyther@gmail.com"
        self.__senha_correta = 123456
        self.__tentativas = 1


    def validar_usuario(self):
        while self.__tentativas <= 3:
            try:
                email = input("Digite seu email: ")
                senha_input =stdiomask.getpass("Digite sua senha: ", mask="*")
                senha = int(senha_input)


                if email.lower().strip() == self.__email_correto and senha == self.__senha_correta:
                    os.system("cls")
                    print(":white_check_mark:[green] Email e Senha Correta![/]")
                    break

                elif self.__tentativas == 3:
                    os.system("cls")
                    print(f":no_entry_sign:[red] Conta bloqueada![/]")
                    break

                else:
                    os.system("cls")
                    print(f":x:[red] Email ou Senha incorreto![/]\n[yellow]Você tem 3 chances, caso erra na terceira tentativa sua conta será bloqueada. Tentativas:{self.__tentativas}[/]")
            except:
                os.system("cls")
                print(":thumbs_down:[yellow] Erro: A senha deve conter apenas números![/]")

            self.__tentativas += 1

v1 = ValidadorCadastro()
v1.validar_usuario()

