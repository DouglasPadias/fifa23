import streamlit as st

# configurando a pagina
st.set_page_config(
    page_title='Players',
    page_icon='🏃🏼‍♂️',
    layout='wide'
)
# lendo o conjunto de dados salvo no state na pagina Home.
df_data = st.session_state['data']

# Criando uma sidebar filtrando pelos cubles
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('CLUBES', clubes)

df_players = df_data[(df_data['Club'] == club)]

# Criando uma sidebar filtrando pelos jogadores
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('JOGADORES', players)

# Fazer o jogador aparecer
player_stats = df_data[df_data['Name'] == player].iloc[0]
st.image(player_stats['Photo'])

# Nome do jogador e demais informacões:
st.title(player_stats['Name'])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

# subheader é um titulo um pouco menor
st.subheader(f"Overall {player_stats['Overall']}")
# progress nos da uma barra com uma medida de 0 a 100
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")
