# Exercicio_04 versão do professor :

# forneca codigo com nome e idade de 5 pessoas ,depois soma as idades e de a média da quantidade:
# inclua soma das idades feminino e masculino separadamente:

soma_m = 0
soma_f = 0
cont_m = 0
cont_f = 0
maior = 0
for i in range(5):
    nome = input("Informe o nome:")
    sexo = input("Informe o sexo:")
    idade = int(input("Informe a idade:"))

    
    if idade > maior:
        maior = idade
     # Adiciona as idades às somas correspondentes e conta
    if sexo == 'M' or sexo == "m":
        soma_m += soma_m + idade
        cont_f += 1
    elif sexo == 'F' or sexo == "f":
        soma_f += soma_f + idade
        cont_m += 1
media_m = soma_m / cont_m
media_f = soma_f / cont_f
 
print(f"A soma das idades masculinas é: {soma_m}")
print(f"A soma das idades femininas é: {soma_f:.2f}")
print(f"A média das idades masculinas é: {media_m:.0f}")
print(f"A média das idades femininas é: {media_f:.0f}")
print(f"A maior idade é: {maior}")








