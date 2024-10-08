# Sistema de Autenticação de Usuários : 


usuarios = ["Creuza","Daniele","Julio","Valquiria","João"]
senhas = ["1234","0000","2209","0203","0304"]
usuario = input("Informe o nome de acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios[i] == usuario:
        senha = input("Informe a senha de acesso:")
        if senhas[i] == senha:
          resp = "Senha Confere - Acesso Liberado"
        else:
            resp = ("Senha não confere - Aceeso Negado")
        break
    else:
        resp = "Usuário não Encontrado"
print(resp)