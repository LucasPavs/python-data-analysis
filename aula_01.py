import pandas as pd

# 1. Carga dos Dados
url = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
df = pd.read_csv(url)

# 2. Exploração Inicial (Visão Geral)
print("--- Primeiras 5 linhas do Dataset ---")
print(df.head())

print("\n--- Informações Estruturais (Tipos de Dados) ---")
df.info()  # Use info() com parênteses para um relatório completo

# 3. Análise Estatística e Dimensões
print("\n--- Resumo Estatístico ---")
print(df.describe())

linhas, colunas = df.shape
print(f"\nDimensões do DataFrame: {linhas} linhas e {colunas} colunas")

# 4. Detalhes das Colunas e Categorias
print("\n--- Nomes das Colunas ---")
print(df.columns.to_list())

print("\n--- Contagem por Nível de Experiência ---")
print(df["experience_level"].value_counts())