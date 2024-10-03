# 2- Uma revendedora de carros paga a seus vendedores três salários mínimos fixos por mês, mais uma comissão de
# acordo com as informações a seguir. Escrever um programa que informe o nome do vendedor, a quantidade de carros por ele
# vendidos no mês e o valor total das vendas mensais. Calcule e escreva o salário final do vendedor.

#• Se a quantidade vendida for menor que 10 – Comissão de 5%.
#• Se a quantidade vendida for maior igual a 10 e menor igual a 20 – Comissão de 10%.
#• Se a quantidade vendida for maior que 20 – Comissão de 20%.


# Constantes
salario_minimo = 1212  # Salário mínimo em reais

# Entrada de dados
nome = input("Informe o nome do vendedor: ")
quantidade_vendida = int(input("Informe a quantidade de carros vendidos: "))
valor_total_vendas = float(input("Informe o valor total das vendas mensais: "))

# Cálculo do salário fixo e da comissão
salario_fixo = 3 * salario_minimo

if quantidade_vendida < 10:
    comissao = valor_total_vendas * 0.05
elif 10 <= quantidade_vendida <= 20:
    comissao = valor_total_vendas * 0.10
else:
    comissao = valor_total_vendas * 0.20

# Cálculo do salário final
salario_final = salario_fixo + comissao

# Exibição dos resultados
print(f"\nNome do vendedor: {nome}")
print(f"Quantidade de carros vendidos: {quantidade_vendida}")
print(f"Valor total das vendas: R$ {valor_total_vendas:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
