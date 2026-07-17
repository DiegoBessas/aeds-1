while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha.lower() == usuario.lower():
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Usuário e senha cadastrados com sucesso!")
        break