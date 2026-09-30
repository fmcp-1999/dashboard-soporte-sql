import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')
df = pd.read_sql("SELECT categoria, AVG(tiempo_resolucion_horas) FROM tickets GROUP BY categoria", conn)
print(df)