# Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não.

# Para estar em condições, um dos seguintes requisitos deve ser satisfeito:

# - Ter no mínimo 65 anos de idade.
# - Ter trabalhado no mínimo 30 anos.
# - Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
# Com base nas informações acima, faça um programa que leia: o nome do empregado, o ano de nascimento e o ano que entrou na empresa.
# O programa deverá escrever a idade e o tempo trabalhado do empregado acompanhado da seguinte mensagem: ‘Apto a Aposentadoria' ou ‘Inapto a Aposentadoria’.



from datetime import datetime


nome = input("Informe o nome do empregado: ")
ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_entrada = int(input("Informe o ano que entrou na empresa: "))


ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
tempo_trabalhado = ano_atual - ano_entrada


apto = (
    idade >= 65 or
    tempo_trabalhado >= 30 or
    (idade >= 60 and tempo_trabalhado >= 25)
)


if apto:
    status = "Apto a Aposentadoria"
else:
    status = "Inapto a Aposentadoria"

print(f"\n{nome}, Idade: {idade} anos, Tempo trabalhado: {tempo_trabalhado} anos.")
print(status)