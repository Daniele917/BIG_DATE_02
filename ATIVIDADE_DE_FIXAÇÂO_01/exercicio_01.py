# Faça um programa que obtenha o valor para a variável HT (horas trabalhadas no mês), obtenha o valor
# para a variável VH (valor hora trabalhada), obtenha o valor para a variável PD (percentual de desconto) e calcule o
# salário bruto => SB = HT * VH, mais o total de desconto => TD = (PD/100)*SB e o salário líquido => SL = SB – TD.
# Apresentando ao final o Salário Liquido.


# Solicitar entradas do usuário
HT = float(input("Informe as horas trabalhadas no mês: "))
VH = float(input("Informe o valor da hora trabalhada: "))
PD = float(input("Informe o percentual de desconto: "))

# Calcular o salário bruto
SB = HT * VH

# Calcular o total de desconto
TD = (PD / 100) * SB

# Calcular o salário líquido
SL = SB - TD

# Exibir o resultado
print(f"\nSalário Bruto: R$ {SB:.2f}")
print(f"Total de Desconto: R$ {TD:.2f}")
print(f"Salário Líquido: R$ {SL:.2f}")
