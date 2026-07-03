import streamlit as st


st.set_page_config(
    page_title='Estoque GPT',
    page_icon='inventory.svg'
)
st.header('Assistente de Estoque')

model_options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
]

selected_model = st.sidebar.selectbox(label='Selecione o modelo LLM', options=model_options)
st.sidebar.markdown('### Sobre')
st.sidebar.markdown('Este agente consulta um banco de dados de estoque utilizando um modelo GPT')

st.write('Faça perguntas sobre o estoque de produto, preços e reposições.')
user_question = st.text_input('O que deseja saber?')

if st.button('Consultar'):
    if user_question:
        st.write('Fez uma pergunta')
    else:
        st.warning('Você inserir uma pergunta')