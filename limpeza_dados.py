import pandas as pd

# Carregar os dados
df = pd.read_csv('caminho/para/seu/arquivo.csv')

# Visualizar os dados iniciais
print(df.head())
print(df.info())

# Tratar valores ausentes
df = df.dropna()  # ou df['coluna'] = df['coluna'].fillna(valor)

# Remover duplicatas
df = df.drop_duplicates()

# Limpar strings
df['coluna'] = df['coluna'].str.lower().str.strip()

# Converter tipos de dados se necessário
df['coluna'] = df['coluna'].astype(int)

# Salvar os dados limpos em um novo arquivo CSV
df.to_csv('caminho/para/seu/arquivo_limpo.csv', index=False)