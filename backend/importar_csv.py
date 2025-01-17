import pandas as pd
import sqlite3

# Carregar o arquivo CSV
df = pd.read_csv('sat.csv')

# Conectar ao banco de dados SQLite (criar se não existir)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Importar o DataFrame para o SQLite
df.to_sql('sat_bd', conn, if_exists='replace', index=False)

# Fechar a conexão
conn.close()