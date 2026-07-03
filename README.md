# Estoque GPT

Aplicação em **Streamlit** que utiliza **Python + LangChain + OpenAI** para consultar um banco de dados de estoque e responder perguntas em linguagem natural sobre produtos, preços, reposição e relatórios.

## Visão geral

O **Estoque GPT** é um assistente inteligente para consulta de estoque.  
A aplicação permite que o usuário faça perguntas em texto livre, enquanto o agente interpreta a solicitação e consulta o banco de dados SQLite para retornar uma resposta amigável e objetiva.

## Funcionalidades

- Consulta de dados do estoque em linguagem natural
- Suporte a perguntas sobre:
  - produtos
  - preços
  - reposição de estoque
  - relatórios
- Seleção de modelo LLM na interface
- Interface simples e responsiva com Streamlit
- Respostas em português brasileiro

## Tecnologias utilizadas

- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI API**
- **SQLite**

## Estrutura principal

- `app.py` — aplicação principal do Streamlit
- `stock.db` — banco de dados SQLite com os dados do estoque
- `requirements.txt` — dependências do projeto
- `inventory.svg` — ícone utilizado na interface

## Como funciona

1. O usuário digita uma pergunta na interface.
2. A aplicação usa um agente do LangChain para interpretar a intenção.
3. O agente consulta o banco `stock.db`.
4. A resposta é exibida em formato amigável no Streamlit.

## Requisitos

- Python 3.10+ recomendado
- Conta e chave de API da OpenAI
- Banco SQLite configurado com os dados de estoque

## Instalação

Clone o repositório:

```bash
git clone https://github.com/caugustoarruda/streamlit_invetory_app.git
cd streamlit_invetory_app
```

Crie e ative o ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Crie um arquivo .env na raiz do projeto e adicione sua chave da OpenAI:
```bash
OPENAI_API_KEY=sua_chave_aqui
```

Executando a aplicação
```bash
streamlit run app.py
```