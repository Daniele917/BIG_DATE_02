# Faça um programa que pergunte quanto um funcionário recebe por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) salário bruto.
# b) quanto pagou ao IRRF.
# c) quanto pagou ao INSS.
# d) quanto pagou ao sindicato.
# e) o salário líquido.


salario_por_hora = float(input("Quanto você ganha por hora? "))  # Entrada de dados
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))


salario_bruto = salario_por_hora * horas_trabalhadas  # Cálculos
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato


print(f"a) Salário Bruto: R$ {salario_bruto:.2f}")  # Resultados
print(f"b) Imposto de Renda (11%): R$ {imposto_renda:.2f}")
print(f"c) INSS (8%): R$ {inss:.2f}")
print(f"d) Sindicato (5%): R$ {sindicato:.2f}")
print(f"e) Salário Líquido: R$ {salario_liquido:.2f}")
