import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="G.E.I FLOW Protótipo", layout="wide")

st.sidebar.title("G.E.I FLOW")
menu = st.sidebar.radio("Navegação", ["Dashboard", "Peças", "Empresas", "Comunicação", "Relatórios", "Configurações"])

if menu == "Dashboard":
    st.title("📊 Dashboard")
    st.metric("Peças Enviadas", 120)
    st.metric("Peças Devolvidas", 80)
    st.metric("Peças Pendentes", 40)
    
    st.subheader("Gráfico de Peças Processadas")
    data = pd.DataFrame({
        'Semana': ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
        'Enviadas': [30, 40, 20, 30],
        'Devolvidas': [20, 20, 20, 20]
    })
    st.bar_chart(data.set_index('Semana'))

elif menu == "Peças":
    st.title("📦 Cadastro de Peças")
    numero = st.text_input("Número do Material")
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=0)
    status = st.selectbox("Status", ["Enviado", "Processando", "Devolvido"])
    empresa = st.selectbox("Empresa Destinatária", ["Empresa A", "Empresa B", "Empresa C"])
    if st.button("Salvar"):
        st.success("Peça cadastrada com sucesso!")

elif menu == "Empresas":
    st.title("🏢 Cadastro de Empresas")
    nome = st.text_input("Nome da Empresa")
    contato = st.text_input("Contato")
    if st.button("Cadastrar"):
        st.success("Empresa cadastrada!")

elif menu == "Comunicação":
    st.title("💬 Comunicação")
    empresa = st.selectbox("Empresa", ["Empresa A", "Empresa B", "Empresa C"])
    mensagem = st.text_area("Mensagem")
    if st.button("Enviar"):
        st.info(f"Mensagem enviada para {empresa}")

    st.subheader("Histórico de Mensagens")
    st.write("[2025-05-29] — Fulano: Olá, enviamos as peças.")
    st.write("[2025-05-29] — Ciclano: Recebido, obrigado.")

elif menu == "Relatórios":
    st.title("📄 Relatórios")
    st.write("Em breve: geração de relatórios em Excel e PDF.")

elif menu == "Configurações":
    st.title("⚙️ Configurações")
    st.write("Configurações gerais do sistema.")

