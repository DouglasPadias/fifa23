# Importante lembrar de colocar as bibliotecas de terceiros 
# dentro do arquivo requirements.txt para não aver problemas futuros

import streamlit as st
import pandas as pd
from datetime import datetime

# configurando a pagina
st.set_page_config(
    page_title='Projeto FIFA',
    page_icon='🏠',
    layout='wide'
)

# Criando o state
# State é utilizado para (rodar, carregar) o conteudo da pagina home nas outras paginas.
# você não precisa criar o mesmo conteudo da pagina home nas outras paginas, é so usar o state.
if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    #df_data = df_data[df_data['Value(￡)'] >= 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

# Utilizando texto markdown
st.markdown('# FIFA23 OFFICIAL DATASET! ⚽️')

# Criando um link no sidebar
st.sidebar.markdown("Desenvolvido por [Douglas Padias](https://www.instagram.com/douglaspadias/)")

# Criando um botão
btn = st.link_button(
    'Acesse os dados do Kaggle',
    'https://www.kaggle.com/discussions/getting-started/355983')

# Texto sobre Kaggle
st.markdown(
    '''
O Kaggle é uma plataforma online popular para cientistas de dados e entusiastas de machine learning,
onde podem acessar datasets, participar de competições de data science, e colaborar com outros
profissionais da área. Oferece um ambiente de notebooks baseado em nuvem, ferramentas de aprendizado,
e uma comunidade ativa para troca de conhecimento. Empresas também utilizam o Kaggle para lançar 
desafios e encontrar soluções inovadoras para problemas reais. É uma excelente ferramenta para praticar
habilidades de análise de dados e **machine learning**, além de construir um portfólio público.
'''
)
# Inserindo audio
st.audio("fala.mp3")
