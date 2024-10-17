# O Gerente de uma loja pediu o seu auxílio para que a cada 7 dias, calculasse a média do valor vendido, o maior
# valor vendido e o menor valor vendido de seus 3 vendedores/as. Pediu para que fosse algo automatizado, pois como ele está em
# fase de expansão, nos próximos meses mais 4 vendedores serão contratados e sua análise deve estar pronta para isso.

# Ele te passou a venda dos últimos 7 dias, dos/as vendedores/as atuais:
# • Maria: 800,700,1000,900,1200,600,600
# • João: 900,500,1100,1000,900,500,700
# • Manuel: 700,600,900,1200,900,700,400

# Como resultado, ele gostaria de visualizar o Nome do/a vendedor/a e a média de venda, o maior valor vendido e o
# menor valor vendido, dos últimos 7 dias.

###
import pandas as pd

# Dados fornecidos
vendas = {
    "Maria": pd.Series([800, 700, 1000, 900, 1200, 600, 600]),
    "João": pd.Series([900, 500, 1100, 1000, 900, 500, 700]),
    "Manuel": pd.Series([700, 600, 900, 1200, 900, 700, 400])
}

# Cálculo das estatísticas para cada vendedor
resultados = {}
for vendedor, valores in vendas.items():
    media_venda = valores.mean()
    maior_venda = valores.max()
    menor_venda = valores.min()
    media_venda_diaria = media_venda / len(valores)
    
    resultados[vendedor] = {
        "Média de Venda": media_venda,
        "Maior Venda": maior_venda,
        "Menor Venda": menor_venda,
        "Média de Venda Diária": media_venda_diaria
    }

# Exibindo os resultados
for vendedor, resultado in resultados.items():
    print(f"Vendedor(a): {vendedor}")
    print(f"  Média de Venda: {resultado['Média de Venda']:.2f}")
    print(f"  Média de Venda Diária: {resultado['Média de Venda Diária']:.2f}")
    print(f"  Maior Venda: {resultado['Maior Venda']}")
    print(f"  Menor Venda: {resultado['Menor Venda']}")
    print()
