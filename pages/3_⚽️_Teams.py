import streamlit as st

# configurando a pagina
st.set_page_config(
    page_title='Teams',
    page_icon='⚽️',
    layout='wide'
)
# lendo o conjunto de dados salvo no state na pagina Home.
df_data = st.session_state['data']

# Criando uma sidebar filtrando pelos cubles
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('CLUBES', clubes)

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

# Filtrando (escolhendo) manualmente as colunas que eu quero que apareça no meu dataframe
columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined",
           "Height(cm.)", "Weight(lbs.)",
           "Contract Valid Until", "Release Clause(£)"]

# Utilizando dataframe para configurar algumas formas de como uma coluna apresenta os dados.
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country")
             })
