#######################
# Importando libraries
import streamlit as st
import webbrowser
import pandas as pd
from streamlit.components.v1 import html

#######################
# Configuração da página
st.set_page_config(
    page_title="Anatel - Acessos",
    page_icon=":phone:",
    layout="wide"
)

#######################
# CSS styling

# Criando estilo CSS para o botão
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color:#44c767;
	border-radius:28px;
	border:1px solid #18ab29;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:17px;
    font-weight:bold;
	padding:16px 31px;
	text-decoration:none;
	text-shadow:0px 1px 0px #2f6627;
}

div.stButton > button:hover {
	background-color:#5cbf2a;
}
</style>""", unsafe_allow_html=True)


def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


#######################
# Carregando dataset

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/banda_larga_fixa_2023.zip", compression='zip', index_col=0)
    st.session_state["data"] = df_data

st.image('images/anatel_logo.gif', width=120)

st.markdown("# Anatel - Acessos Banda Larga Fixa")

st.markdown(
    """
    Os dados apresentados nesse estudo acadêmico, referem-se aos acessos de Banda Larga Fixa (Serviço de Comunicação Multimídia – SCM), enviados pelas prestadoras do serviço.

    O Serviço de Comunicação Multimídia é um serviço fixo de telecomunicações de interesse coletivo, prestado em âmbito nacional e internacional, no regime privado, que possibilita a oferta de capacidade de transmissão, emissão e recepção de informações multimídia, permitindo inclusive o provimento de conexão à internet, utilizando quaisquer meios, a Assinantes dentro de uma Área de Prestação de Serviço.
"""
)

st.markdown("# Objetivo")

st.markdown(""" O mercado de banda larga fixa vem crescendo cada vez mais no Brasil, gerando uma grande concorrência entre empresas de telecomunicações.

Cada vez mais, os brasileiros desejam ter em casa uma conexão de alta velocidade e de grande estabilidade, e esse cenário é um efeito da modernização da infraestrutura de telecomunicações no país.

Trata-se de um movimento cujo início beneficiou principalmente grandes centros urbanos, mas que foi expandindo gradualmente para cidades pequenas e bairros mais afastados. 

Não resta dúvida hoje em dia, que **a banda larga mais eficaz é a Fibra óptica**.

A ANATEL(Agência Nacional de Telecomunicações) divulgou em seu portal de dados, que em 2023 o Brasil registrou **48,2 milhões de acessos de banda larga fixa**, e que 74% desses acessos, são de Fibra Óptica.""")

st.markdown("# Coleta dos Dados")
st.markdown(""" Os dados foram coletados no sítio da Agência """)
st.button('Acesse Dados.gov.br', on_click=open_page, args=('https://dados.gov.br/dados/conjuntos-dados/acessos---banda-larga-fixa',))