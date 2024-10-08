# Versão do Professor do exercicio_09.py :

usuarios = ["pedro","maria","duda","dirceu","elvis"]
senhas = ["123","345","567","@@@$$$","8910"]
usuario = input("Informe o nome de acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios[i] == usuario:
        resp = "Usuário Encontrado"
        break
    else:
        resp = "Usuário não Encontrado"
print(resp)