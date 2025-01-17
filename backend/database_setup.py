import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criar a tabela (ajuste conforme a estrutura do seu CSV)
cursor.execute('''
CREATE TABLE IF NOT EXISTS nome_da_tabela (
    DBN TEXT PRIMARY KEY,
    School_Name TEXT,
    Num_of_SAT_Test_Takers INTEGER,
    SAT_Critical_Reading_Avg_Score INTEGER,
    SAT_Math_Avg_Score INTEGER,
    SAT_Writing_Avg_Score INTEGER
)
''')

# Fechar a conexão
conn.commit()
conn.close()