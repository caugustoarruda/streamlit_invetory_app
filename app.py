import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain import hub

from decouple import config

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

model = ChatOpenAI(
    api_key=config('OPENAI_API_KEY'),
    model=selected_model
    )

db = SQLDatabase.from_uri('sqlite:///stock.db')
toolkit = SQLDatabaseToolkit(db=db, llm=model)

system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(),
    prompt=system_message
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True
)

prompt = '''
    Use as ferramentas necessárias para responder as perguntas relacionadas o estoque de produtos. Voce fornecerá insights sobre produtos, preços, reposição de esoque e relatorios conforme
    solicitado pelo usuário. A resposta final deve ter uma formatação amigável de visualização para o usuário.
    Sempre responda em português brasileiro.
    Pergunta: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)

if st.button('Consultar'):
    if user_question:
        with st.spinner('Consultado banco de dados:'):
            formatted_prompt = prompt_template.format(q=user_question)
            output = agent_executor.invoke({'input': formatted_prompt})
            st.markdown(output.get('output'))
    else:
        st.warning('Você inserir uma pergunta')