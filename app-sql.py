import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Soporte SQL", layout="wide")
st.title("📊 Proyecto 2: Dashboard con SQL REAL")

conn = sqlite3.connect('soporte.db')

# CONSULTA 1: La que te preguntan en entrevista
st.subheader("1. Tiempo promedio por categoría (con SQL)")
q1 = "SELECT categoria, AVG(tiempo_resolucion_horas) as promedio FROM tickets GROUP BY categoria"
df1 = pd.read_sql(q1, conn)
st.dataframe(df1)
st.plotly_chart(px.bar(df1, x='categoria', y='promedio'))

# CONSULTA 2
st.subheader("2. Top agentes con más escalados")
q2 = "SELECT agente, COUNT(*) as escalados FROM tickets WHERE estado='Escalado' GROUP BY agente ORDER BY escalados DESC"
st.dataframe(pd.read_sql(q2, conn))

# CONSULTA 3
st.subheader("3. Clientes en riesgo (satisfaccion < 3 y más de 2 tickets)")
q3 = """
SELECT cliente, COUNT(*) as num_tickets, AVG(satisfaccion) as sat_prom 
FROM tickets 
GROUP BY cliente 
HAVING sat_prom < 3 AND num_tickets > 2
ORDER BY sat_prom ASC
LIMIT 10
"""
st.dataframe(pd.read_sql(q3, conn))

conn.close()