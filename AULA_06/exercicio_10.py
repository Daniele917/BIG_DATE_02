# verifica_usuario_senha.py - codigo melhorado para exercicio_09.py :

"""
Este script verifica se um nome de usuário e uma senha fornecidos
estão presentes nas listas de usuários e senhas correspondentes.
"""

# Listas de usuários e senhas
usuarios = ["alessandro", "Pedro", "Maria", "Lucas", "Ana"]
senhas = ["123", "abc", "456", "senha123", "pass123"]

# Função para conferir se o usuário e a senha existem
def conferir_usuario_senha(nome_usuario, senha):
    # Normaliza a entrada do usuário para comparar de forma case-insensitive
    nome_usuario = nome_usuario.lower()
    
    if nome_usuario in [u.lower() for u in usuarios]:  # Verifica se o usuário existe, ignorando maiúsculas
        index = [u.lower() for u in usuarios].index(nome_usuario)  # Obtém o índice do usuário
        if senhas[index] == senha:
            return "Usuário e senha corretos - Acesso Liberado!"
        else:
            return "Senha incorreta - Acesso Negado!"
    else:
        return "Usuário não encontrado!"

# Loop para permitir várias tentativas
while True:
    usuario_input = input("Digite seu nome de usuário (ou digite 'sair' para encerrar): ")
    
    if usuario_input.lower() == 'sair':
        print("Saindo do sistema.")
        break  # Sai do loop se o usuário digitar 'sair'
    
    senha_input = input("Digite sua senha: ")
    
    # Conferir o usuário e a senha
    resultado = conferir_usuario_senha(usuario_input, senha_input)
    print(resultado)
