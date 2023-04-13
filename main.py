# Importa o pandas com o apelido pd
import pandas as pd

# Importa o streamlit com o apelido st
import streamlit as st

# Importa o submódulo date
from datetime import date


# Configurações da página
st.set_page_config(
    page_title='Gerador de Datas',
    page_icon=':calendar:',
    layout='centered'
)

# Define um título principal para a aplicação
st.title(':calendar: Gerador de Datas')

# Campo para o ano inicial
ano_inicial = st.number_input(label='Informe o ano inicial:', value=2023)

# Campo para o ano final
ano_final = st.number_input(label='Informe o ano final:', value=2023)


def obter_datas(inicio: int, fim: int) -> tuple:
    # Data inicial
    comeco = date(ano_inicial, 1, 1)

    # Data final
    termino = date(ano_final, 12, 31)

    # Retorna as datas
    return comeco, termino


# Obtém a data inicial e a final
data_inicial, data_final = obter_datas(ano_inicial, ano_final)

# DataFrame com o intervalo de datas
df_datas = pd.date_range(start=data_inicial, end=data_final, freq='D').to_frame(index=False, name='Data')

# Cria novas colunas no dataframe
df_datas['Dia'] = df_datas['Data'].dt.day
df_datas['Mês'] = df_datas['Data'].dt.month
df_datas['Ano'] = df_datas['Data'].dt.year

# Formata a coluna de datas
df_datas['Data'] = df_datas['Data'].dt.strftime('%d/%m/%Y')


def obter_csv(df):
    """Retorna um arquivo CSV a partir do dataframe passado."""
    return df.to_csv(index=False).encode('utf-8')


if not df_datas.empty:
    # Exibe o dataframe
    st.dataframe(df_datas)

    # Obtém o CSV
    csv = obter_csv(df_datas)

    # Botão de download
    st.download_button(
        label='📥 Baixar CSV',
        file_name='calendario.csv',
        data=csv,
        mime='text/csv'
    )
else:
    st.warning('O ano final deve ser maior ou igual ao ano inicial.')
