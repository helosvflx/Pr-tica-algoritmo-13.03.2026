#tentem adivinhar o usuário e a senha, se for os certos, 
# vai aparecer a mensagem "Seja bem vindo!", se não, 
# "Usuário e senha não conferem" dica: futebol

usuario = input("Digite o seu login: ")
senha = input("Digite a senha: ")

if (usuario == "senac" and senha == "777"):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem.")