# Listas de usuários e senhas:


usuarios = ["Alessandro", "Pedro", "Maria", "Lucas", "Ana"]
senhas = ["123", "abc", "456", "senha123", "pass123"]

# Função para conferir se o usuário e a senha existem
def conferir_usuario_senha(nome_usuario, senha):
    if nome_usuario in usuarios:
        index = usuarios.index(nome_usuario)
        if senhas[index] == senha:
            return "Usuário e senha corretos - Acesso Liberado!"
        else:
            return "Senha incorreta - Acesso Negado!"
    else:
        return "Usuário não encontrado!"

# Solicitar entrada do usuário
usuario_input = input("Digite seu nome de usuário: ")
senha_input = input("Digite sua senha: ")

# Conferir o usuário e a senha
resultado = conferir_usuario_senha(usuario_input, senha_input)
print(resultado)


# Listas de usuários e senhas
usuarios = ["Alessandro", "Pedro", "Maria", "Lucas", "Ana"]
senhas = ["123", "abc", "456", "senha123", "pass123"]

# Função para conferir se o usuário e a senha existem
def conferir_usuario_senha(nome_usuario, senha):
    if nome_usuario in usuarios:
        index = usuarios.index(nome_usuario)
        if senhas[index] == senha:
          return "Acesso Liberado!"
        else:
            return "Acesso Negado! Senha incorreta."
    else:
        return "Acesso Negado! Usuário não encontrado."

# Solicitar entrada do usuário
usuario_input = input("Digite seu nome de usuário: ")
senha_input = input("Digite sua senha: ")

# Conferir o usuário e a senha
resultado = conferir_usuario_senha(usuario_input, senha_input)
print(resultado)
