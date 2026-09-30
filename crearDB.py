import sqlite3
import pandas as pd

df = pd.read_csv('tickets_10k.csv')
conn = sqlite3.connect('soporte.db')
df.to_sql('tickets', conn, if_exists='replace', index=False)
conn.close()
print("soporte.db creada con 10k tickets")