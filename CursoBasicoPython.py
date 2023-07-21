# Logica de programacao

# Passo 0- Entender o desafio que voce quer resolver
# Passo 1- Percorrer todos os arquivos da pasta base de dados 
import os
import pandas as pd

lista_arquivos = os.listdir("python/Vendas")

tabela_total = pd.DataFrame()

# Passo 2- Importar as bases dados de vendas

for arquivo in lista_arquivos:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"python/Vendas/{arquivo}")
        tabela_total = tabela_total._append(tabela)
        #Importar o arquivo
    
# Passo 3- Tratar / Compilar a base de dados
print(tabela_total)


# Passo 4- Calcular o produto mais vendido em quantidade
tabela_produto = tabela_total.groupby("Produto").sum()[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produto)

# Passo 5- Calcular o produto que mais faturou
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby("Produto").sum()[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_faturamento)

# Passo 6- Calcular a loja/cidade que mais vendeu - criar um grafco/dashboard
tabela_lojas = tabela_total.groupby("Loja").sum()[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(tabela_lojas)