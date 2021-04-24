# Fazendo a chamada das bibliotecas para conseguir abrir a URL onde se encontra o arquivo com os dados Geolocalizados:
from urllib.request import urlopen
import json

# Esses dados correpondem a regiões dos EUA (Seguindo o padrão FIPS-> Federal Information Processing Standard)
# E estão armazenados num arquivo 'json' (Arquivos parecidos com Planilhas do Excel)
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    condados = json.load(response)

# Aqui chamo a Biblioteca Pandas (Que lê estes arquivos parecidos com planilhas)
import pandas as pd

dados = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv', dtype={"fips": str})

# Esta biblioteca gera a visualização (Qua vai abrir no navegador) plotly.express é uma biblioteca de alto nivel.
import plotly.express as px

# Cada linha do objeto DataFrame (variavel "dados" é representada como uma região no mapa coropletico)
vis = px.choropleth_mapbox(
    dados,                              # Aqui informo qual o conjunto de dados
    geojson=condados,                   # deve conter uma coleção de recursos de poligonos, com IDs, que se referem a Locais
    locations='fips',                   # os valores desta coluna/variavel devem ser interpretados e mapeados para log./latitude
    color='unemp',                      # variavel relacionada a taxa de desemprego definirá atribuição das cores
    color_continuous_scale="Viridis",   # paleta de cores continua, padrão variando de azul escuro até amarelo
    range_color=(0, 15),                # variaçã das cores de acordo com os valores da taxa de cada local
    mapbox_style="carto-positron",      # estilo do mapa que será utilizado
    zoom=2,                             # definição do zoom padrão, o usuario podera aumentar ou diminuir o mapa (durante a interação)
    center={"lat": 50.0902, 'lon': -115.7129},# definição da localização que irá centralizar o mapa logo ao abrir
    opacity=0.8,                        #valor 0 e 1. Define a opacidade para marcadores
    height=800,                         # define a altura da figura
    title='Exemplo de mapa coroplético (choropleth map)',# Titulo da visualização
    labels={'unemp': 'Taxa de desemprego', 'fips': 'Condado/FIPS'}#Convertendo o nome das variaveis em versões para apresentar
)                                                                #.. no mapa quando o usuario passar o mouse sob determinada região.

vis.show()
