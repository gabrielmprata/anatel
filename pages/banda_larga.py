#######################
# Importando libraries
import json
from urllib.request import urlopen
import streamlit as st
import plotly.express as px
import webbrowser
import pandas as pd
from st_aggrid import AgGrid

#######################
# Configuração da página
st.set_page_config(
    page_title="Banda Larga - Acessos",
    page_icon="🏠",
    layout="wide"
)


#######################
# Load data
df_data = st.session_state["data"]


# Dataframes auxiliares

#######################
# Quadro com o total e a variação

df_total_ant = df_data.groupby(["ano", "mes"])['Acessos'].sum().reset_index()
df_total_ant['acesso_ant'] = df_total_ant.Acessos.shift(1)
df_total_ant['var_acesso'] = df_total_ant['Acessos']-df_total_ant['acesso_ant']
df_total_ant['acesso_ant'].fillna(0, inplace=True)
df_total_ant['var_acesso'].fillna(0, inplace=True)
df_total_ant['acesso_ant'] = df_total_ant['acesso_ant'].astype(int)
df_total_ant['var_acesso'] = (
    df_total_ant['var_acesso'].astype(int)/1000).round(1)

df_total_ant['Acessos'] = ((df_total_ant['Acessos'])/1000000).round(1)

#######################
# Quantidade de acesso por estado, com bandeira e progress column
UF_flag = pd.read_csv('datasets/UF_flags.csv', encoding="utf_8", sep=';') #carrega dataset com o caminho das imagens

df_UF = df_data.groupby(["UF","mes"])['Acessos'].sum().reset_index()

df_UF_flag = df_UF[(df_UF['mes'] == 12)].groupby(["UF"])['Acessos'].sum().reset_index()
df_UF_flag_data = pd.merge(UF_flag, df_UF_flag,  left_on='uf', right_on='UF')
df_UF_flag_data = df_UF_flag_data.sort_values(by='Acessos', ascending=False)

#######################
# Carregar Mapa do Brasil

# Carregando o arquivo Json com o mapa do Brasil
with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson') as response:
    Brasil = json.load(response)

state_id_map = {}
for feature in Brasil["features"]:
    feature["id"] = feature["properties"]["sigla"]
    # definindo a informação do gráfico
    state_id_map[feature["properties"]["sigla"]] = feature["id"]

# Choropleth map
# Reaproveitando o dataframe df_UF_flag

# Criando o grafico
choropleth = px.choropleth_mapbox(
    df_UF_flag,  # database
    locations='UF',  # define os limites no mapa
    geojson=Brasil,  # Coordenadas geograficas dos estados
    color="Acessos",  # define a metrica para a cor da escala
    hover_name='UF',  # informação no box do mapa
    hover_data=["UF"],
    title="Acessos",  # titulo do mapa
    mapbox_style="white-bg",  # define o style do mapa
    center={"lat": -14, "lon": -55},  # define os limites para plotar
    zoom=2.5,  # zoom inicial no mapa
    color_continuous_scale="greens",  # cor dos estados
    range_color=(0, max(df_UF_flag.Acessos)),  # Intervalo da legenda
    opacity=0.5  # opacidade da cor do mapa, para aparecer o fundo
)

choropleth.update_layout(

    plot_bgcolor='rgba(0, 0, 0, 0)',
    coloraxis_showscale=False,  # Tira a legenda
    margin=dict(l=0, r=0, t=0, b=0),
    height=350
)

# Heatmap
#######################

# Ordenar o dataframe por UF para ordenar o eixo X
df_data.sort_values(by='UF', ascending=True,inplace=True)

# Criando o grafico
heatmap = px.density_heatmap(df_data, 
                         x="UF", 
                         y="mes", 
                         z="Acessos", 
                         histfunc="sum", 
                         color_continuous_scale="greens"
                         )

heatmap.update_layout(yaxis = dict(
                                tickmode = 'array', # alterando o modo dos ticks
                                tickvals = df_data['mes'], # setando a posição do tick de x
                                ticktext = df_data['mes']),# setando o valor do tick de x
                                title="",
                                xaxis_title="",
                                yaxis_title="",
                                coloraxis_showscale=False # tira a legenda
                    ) 

heatmap.update_traces(hovertemplate='UF: %{x}<br>' +
                                 'Mês: %{y}<br>' +
                                 'Acessos: %{z}<br>'
                   )

#######################
# Pie Chart
# Dataframe agrupando por Meio acesso
df_meio_acesso = df_data.groupby(["mes","meio_acesso"])['Acessos'].sum().reset_index()

# Dataframe como o mês atual
df_meio_acesso_pie = df_meio_acesso[(df_meio_acesso['mes'] == 12)]

# Criando o grafico
pie =   px.pie(df_meio_acesso_pie, 
             values='Acessos', 
             names='meio_acesso', 
             height=350, #altura
             width=300,  #largura
             labels=dict(meio_acesso="Meio de acesso"),
             color_discrete_sequence=px.colors.sequential.Greens_r
             )
pie.update_layout(showlegend=False)
pie.update_traces(textposition='outside',
                  textinfo='percent+label')
                  
#######################
# Line Chart

# Criando o grafico
line = px.line(df_meio_acesso, x='mes', y='Acessos',
              color='meio_acesso',
              markers=True,
              title=" ",
              #height=600, width=800, #altura x largura
              labels=dict(meio_acesso="Meio de acesso", mes="Mês"),
              color_discrete_sequence=px.colors.sequential.Greens_r,
              line_shape="spline",
              template="plotly_white"
              )
line.update_layout(xaxis = dict(linecolor='rgba(0,0,0,1)', # adicionando linha em y = 0
                                tickmode = 'array', # alterando o modo dos ticks
                                tickvals = df_meio_acesso['mes'], # setando a posição do tick de x
                                ticktext = df_meio_acesso['mes']),# setando o valor do tick de x
                                title_x = 0.5) #centralizando o titulo

line.update_xaxes(showspikes=True, spikecolor="black", spikesnap="cursor", spikemode="across")
line.update_yaxes(showspikes=True, spikecolor="blue", spikethickness=2)
line.update_layout(spikedistance=1000, hoverdistance=100)

#######################
# Top 10 empresas
#dataframe com o logo das operadoras
img_oper = pd.read_csv('datasets/df_logo_oper.csv', encoding="utf_8", sep=';') #carrega dataset com o caminho das imagens

#Dataframe agrupado por empresa em colunas
acesso_bl_2023_col = pd.read_csv("datasets/banda_larga_fixa_2023_colunas.zip", compression='zip', index_col=0) 

#Agrupando o dataframe por empresa
acesso_hist = acesso_bl_2023_col.groupby(['empresa']).sum(['2023-01','2023-02','2023-03','2023-04','2023-05','2023-06','2023-07','2023-08','2023-09','2023-10','2023-11','2023-12']).reset_index()

#Criando a coluna histórico
acesso_hist["historico"] = "[" + acesso_hist["2023-01"].apply(str) + ", " + acesso_hist["2023-02"].apply(str) + ", " + acesso_hist["2023-03"].apply(str) + ", " + acesso_hist["2023-04"].apply(str)+ ", " + acesso_hist["2023-05"].apply(str) + ", " + acesso_hist["2023-06"].apply(str) + ", " + acesso_hist["2023-07"].apply(str) + ", " + acesso_hist["2023-08"].apply(str) + ", " + acesso_hist["2023-09"].apply(str) + ", " + acesso_hist["2023-10"].apply(str) + ", " + acesso_hist["2023-11"].apply(str) + ", " + acesso_hist["2023-12"].apply(str) + "]"

#Sumarizado os acessos de 2023-12
mkt_share_tot = sum(acesso_hist["2023-12"])

#Calculando o Mkshare de 202312
acesso_hist['market_share'] = ((acesso_hist['2023-12']/mkt_share_tot)*100).round(2)
acesso_hist['ranking'] = (acesso_hist["2023-12"].rank(ascending = False)).astype(int)
gr_mktshare = acesso_hist.sort_values(by='ranking', ascending=True).head(10)

gr_mktshare = pd.merge(img_oper, gr_mktshare,  left_on='empresa', right_on='empresa')

#######################
# Evolução porte das operadoras
#Dataframe agrupado por porte
df_porte = df_data.groupby(["mes","porte_prestadora"])['Acessos'].sum().reset_index()

# Criando o grafico
gr_porte = px.line(df_porte, x='mes', y='Acessos',
              color='porte_prestadora',
              markers=True,
              title=" ",
              height=500, width=800, #altura x largura
              labels=dict(porte_prestadora="Porte da Prestadora", mes="Mês"),
              color_discrete_sequence=["#85d338", "green"],
              #color_discrete_sequence=px.colors.sequential.Greens,
              line_shape="spline",
              template="plotly_white"
              )
gr_porte.update_layout(xaxis = dict(#linecolor='rgba(0,0,0,1)', # adicionando linha em y = 0
                                tickmode = 'array', # alterando o modo dos ticks
                                tickvals = df_porte['mes'], # setando a posição do tick de x
                                ticktext = df_porte['mes']),# setando o valor do tick de x
                                title_x = 0.5) #centralizando o titulo



#######################
# Dashboard Main Panel
col = st.columns((1.2, 3.5, 3.5), gap='medium')


with col[0]:

    st.markdown('### Total Acessos')
    st.metric(label="", value=str(
        df_total_ant.Acessos.values[11])+" M", delta=str(df_total_ant.var_acesso.values[11])+"K")

with col[1]:
    st.markdown('###')
    st.plotly_chart(choropleth, use_container_width=True)

with col[2]:
    st.markdown('### Meio de Acesso')
    st.plotly_chart(pie, use_container_width=True)
    
col1 = st.columns((4.7, 3), gap='medium')

with col1[0]:
    st.markdown('### Top 10 Operadoras')  
    st.markdown('')  
    
    st.dataframe(
        gr_mktshare,
        column_order=("oper_logo", "empresa", "2023-12", "market_share", "ranking", "historico"),
        column_config={
            "oper_logo": st.column_config.ImageColumn(" ", width="small"),
            "empresa": "Operadora",
            "Acessos": "Acessos",
            #"market_share": "Market Share", 
            "market_share": st.column_config.NumberColumn(
            "Market Share",
            help="% de Participacão no mercado",
            format="%.2f",
        ),
            "ranking": "Ranking",
            "historico": st.column_config.LineChartColumn(
            "Histórico 12 meses"
        ),
        },
        hide_index=True,
    )    

with col1[1]:  
    st.markdown('### Top Estados')  
    st.markdown('')  
    
    st.data_editor(
        df_UF_flag_data,
        column_order=("flag", "UF", "Acessos"),
        column_config={
            "flag": st.column_config.ImageColumn(" "),
            "UF": "UF",
            "Acessos": st.column_config.ProgressColumn(
                "Acessos",
                format='%d',

                min_value=0,
                max_value=max(df_UF_flag_data.Acessos)
            ),
        },
        hide_index=True,
    )

st.markdown('### Histórico de Acessos')
st.plotly_chart(heatmap, use_container_width=True)

st.markdown('### Evolução anual por meios de acesso')      
st.plotly_chart(line, use_container_width=True)

st.markdown('### Evolução dos acessos por Porte da Prestadora')
st.plotly_chart(gr_porte, use_container_width=True)