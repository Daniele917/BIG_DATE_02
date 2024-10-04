# Faça um programa para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. Calcular ,
# e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total -desconto), sabendo que:

#- Se quantidade <= 5 o desconto será de 2%.
#- Se quantidade > 5 e quantidade <=10 o desconto será de 3%.
#- Se quantidade > 10 o desconto será de 5%.



try:
    nome = input("Informe o nome do produto: ")
    qtd = int(input("Informe a quantidade desejada: "))
    valor = float(input("Informe o valor unitário: "))
except ValueError:
    print("Verifique os valores informados")
else:
    total = valor * qtd
    print(f"O Valor total sem desconto é R$ {total:.2f}")
    if qtd <= 5:
        desc = total * 0.98
    elif qtd > 5 and qtd <= 10:
        desc = total * 0.97
    else:
        desc = total * 0.95
    print(f"O Valor total com desconto é R$ {desc:.2f}")