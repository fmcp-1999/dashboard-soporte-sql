import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Soporte PRO", layout="wide")
st.title("📊 Dashboard PRO - 10K Tickets")

@st.cache_data
def load_data():
    return pd.read_csv('tickets_10k.csv')
df = load_data()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total", len(df))
c2.metric("Tiempo Prom", f"{df['tiempo_resolucion_horas'].mean():.1f}h")
c3.metric("Satisfacción", f"{df['satisfaccion'].mean():.2f}/5")
c4.metric("Escalados", len(df[df['estado']=='Escalado']))

df_f = df[df['categoria'].isin(st.sidebar.multiselect("Categoría", df['categoria'].unique(), default=df['categoria'].unique()))]

fig = px.bar(df_f.groupby('categoria')['tiempo_resolucion_horas'].mean().reset_index(), x='categoria', y='tiempo_resolucion_horas', title='Tiempo por Categoría')
st.plotly_chart(fig)