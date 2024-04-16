# :bar_chart: Anatel - Acessos de Banda Larga Fixa no Brasil :chart_with_upwards_trend:

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge" #vitrinedev/>  

<img src="http://img.shields.io/static/v1?label=vers%C3%A3o%20do%20projeto&message=v1.5.0&color=red&style=for-the-badge&logo=github"/>
</p>
<img src="https://github.com/gabrielmprata/anatel/assets/119508139/980dc71b-4cea-4d4b-997c-425f4dfdbf3b" alt="Dashboard"  height="350">

</br>


# :radio_button: Objetivo 
Criar um simples Dashboard em **Python** e **Streamlit**, para a visualização das informações do cenário de Banda Larga Fixa no Brasil.

<br><br>
# Ferramentas utilizadas
<img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40" height="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg" width="40" height="40"/>   <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/plotly/plotly-original-wordmark.svg" width="40" height="40"/>  <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original-wordmark.svg" width="40" height="40"/>


<br></br>
# Introdução

Os dados apresentados nesse estudo acadêmico, referem-se aos acessos de Banda Larga Fixa (**SCM** - Serviço de Comunicação Multimídia), enviados pelas prestadoras do serviço.

O Serviço de Comunicação Multimídia é um serviço fixo de telecomunicações de interesse coletivo, prestado em âmbito nacional e internacional, no regime privado, que possibilita a oferta de capacidade de transmissão, emissão e recepção de informações multimídia, permitindo inclusive o provimento de conexão à internet, utilizando quaisquer meios, a Assinantes dentro de uma Área de Prestação de Serviço.
<br><br>

# **<font color=#85d338> 1. Definição do problema**
>
O mercado de banda larga fixa vem crescendo cada vez mais no Brasil, gerando uma grande concorrência entre empresas de telecomunicações.
>
Cada vez mais, os brasileiros desejam ter em casa uma conexão de alta velocidade e de grande estabilidade, e esse cenário é um efeito da modernização da infraestrutura de telecomunicações no país.
>
Trata-se de um movimento cujo início beneficiou principalmente grandes centros urbanos, mas que foi expandindo gradualmente para cidades pequenas e bairros mais afastados.
Não resta dúvida hoje em dia, que **a banda larga mais eficaz é a Fibra óptica**.
>
A ANATEL(Agência Nacional de Telecomunicações) divulgou em seu portal de dados, que em 2023 o Brasil registrou **48,2 milhões de acessos de banda larga fixa**, e que 74% desses acessos, são de Fibra Óptica.
>
Com os dados disponibilizados pela ANATEL, iremos entender o cenário de Banda Larga no Brasil.
>
# **<font color=#85d338> 2. Coleta de Dados**
>
Os dados foram coletados do sítio da Agência Nacional de Telecomunicações.<img align="left" width="45" height="45" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Anatel_Logo.svg/180px-Anatel_Logo.svg.png">
>
https://informacoes.anatel.gov.br/paineis/acessos
<br>
>
# **<font color=#85d338> 3. Pré-porcessamento**
>
Esta é a etapa mais demorada e trabalhosa do projeto de ciência de dados, e estima-se que consuma pelo menos 70% do tempo total do projeto.
>
Após coletar e analisar os dados naetapa anterior, é necessário limpar,transformar e apresentar melhor os seus dados, a fim de obter, na próxima etapa, os melhores resultados possíveis nos algoritmos de machine learning ou simplesmente apresentar dados mais confiáveis para os clientes em soluções de
business intelligence.
>
Como o nosso objetivo é criar um Dashboard com **Python** e **Streamlit**, iremos mnizar ao máximo o tamanho e a granularidade dos Datasets disponibilizados, a fim de termos um ambiente mais "leve" para a leitura dos dados.
>
Principais técnicas utilizadas:
>
**Limpeza:** Consiste na verifi cação da consistência das informações,correção de possíveis erros de preenchimento ou eliminação de valores desconhecidos,redundantes ou não pertencentes ao domínio
>
**Agregação:** Também pode ser considerada uma técnica de redução de dimensionalidade, pois reduz o número de linhas e colunas de um dataset.
>
**Tratamendo de dados faltantes (missing):** Identificamos e, em seguida, tratamos com um valor adequado. Não foi necessario a exclusão desses registros.
>
# **<font color=#85d338> 4. Apresentação dos resultados**
>
A Anatel divulgou os números de banda larga fixa, informados pelas operadoras de telefonia,  e no ano de 2023 o Brasil chegou a marca de 48,4 milhões de acessos instalados.
>
Em relação ao ano de 2023 o mercado cresceu apenas 6,3%.
Claro e Vivo, lideram o ranking entre as operados, com 20,6% e 13,9% de Market Share.
>
O estado de São Paulo é o que concentra o maior número de acessos, cerca de 14,6 milhões, concentrando 30% do mercado, seguido de Minas Gerais com 5,4 milhões de acessos e 11% do mercado brasileiro.
>
<img src="https://github.com/gabrielmprata/anatel/assets/119508139/7e2eb4b5-63d7-4d72-b675-7b6c906c9647" alt="Top"  height="200">
<br></br>

Os acessos de **Fibra Óptica** dominam o mercado brasileiro, com 36 milhões de instalações, representando 74,4%.
<img src="https://github.com/gabrielmprata/anatel/assets/119508139/9508e982-4dc2-4cc6-a433-721bf5dfb37b" alt="Meio de Acesso"  height="200">
<br></br>
As empresas de pequeno porte (PPPs), continuam crescendo cada vez mais, ultrapassando as empresas de grande porte, conquistando 54% do mercado brasileiro.
>
<img src="https://github.com/gabrielmprata/anatel/assets/119508139/e0f258de-4aaf-47d6-b840-f5dcde7c0b77" alt="Porte"  height="200">
<br></br>

No nosso próximo estudo iremos detalhar o mercado de **Fibra óptica**!

<br></br>
Até breve!
<br></br>
## :floppy_disk: Instalção 

No terminal, clone o projeto: 

```
git clone https://github.com/gabrielmprata/Anatel.git
```

... 

