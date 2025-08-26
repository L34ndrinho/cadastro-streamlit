import streamlit as st
import pandas as pd


dados = pd.read_csv("clientes.csv")

st.subheader('Clientes Cadastrados', divider=True)

st.dataframe(dados,)