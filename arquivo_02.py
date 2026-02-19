from rich import print
import os

email_correto = "pyther@gmail.com"
senha_correto = 123456

try:
    email = input("Digite seu email: ")
    senha = int(input("Digite sua senha: "))

    if email_correto == email.strip().lower() and senha_correto == senha:
        os.system("cls")
        print(f":white_heavy_check_mark: [green]Acesso Liberado!")

    else:
        os.system("cls")
        print(":x: [red]Senha ou email incorreto![/]")

except:
    print(":thumbs_down:[yellow] Erro: A senha deve conter apenas números![/]")



