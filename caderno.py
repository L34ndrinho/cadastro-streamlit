import streamlit as st
import pandas as pd
from datetime import date 

def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today(): 
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nasc}, {tipo}\n")   
        st.session_state["sucesso"] = True #Crie uma variável de sessão  
    else:
        st.session_state["sucesso"] = False

lateral = st.sidebar # Cria a barra lateral, apenas uma variável

st.set_page_config( # Configurações da página
    page_title="Cadastro de Clientes",
    page_icon=":clipboard:",
    layout="centered",
)

st.header("Cadastro de Clientes", divider=True)
st.divider()

nome = st.text_input("DIgite o nome do cliente:", 
                     key="nome_cliente")

dt_nasc = st.date_input("Data de Nascimento:", 
                        key="data_nascimento", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de Cliente:", 
                    ["Pessoa Física", "Pessoa Jurídica", "Autônomo", "Outros"],
                    key="tipo_cliente")

btn_cadastrar = st.button("Cadastrar Cliente", 
                          on_click=gravar_dados, 
                          args=(nome, dt_nasc, tipo))

if btn_cadastrar:
    if st.session_state['sucesso']:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
    else:
        st.error("Erro no cadastro. Verifique os dados e tente novamente.",
                 icon="❌")