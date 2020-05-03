#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://github.com/pomber/covid19
print('Initializing São Paulo\'s analysis!')
import numpy as np
import pandas as pd
import folium, html, json
import matplotlib.pyplot as plt
import datetime


# In[2]:


df = pd.read_csv('../data/saoPaulo_corona19_data.csv')
df['date'] = df['date'].astype('datetime64[ns]')
df['codigo_ibge'] = df['codigo_ibge'].astype('int') # para tirar o .0
df['codigo_ibge'] = df['codigo_ibge'].astype('str')

today = str(df.date.max().date())
tomorrow = str(df.date.max().date() + datetime.timedelta(days=1))
yesterday = str(df.date.max().date() - datetime.timedelta(days=1))
qtdeMonitored = 5

df.head()


# In[3]:


state_geo = json.load(open('../data/saoPaulo-cidades.json'))
m = folium.Map(location=[-22.60, -48.44], zoom_start=7)

folium.Choropleth(
    geo_data=state_geo,
    name='Mortalidade',
    data=df,
    columns=['codigo_ibge','avg7_perc_death'],
    key_on='feature.properties.codarea',
    highlight=True,
    fill_color='YlOrRd',#'YlGn',
#     ‘BuGn’, ‘BuPu’, ‘GnBu’, ‘OrRd’, ‘PuBu’, ‘PuBuGn’, ‘PuRd’, ‘RdPu’, ‘YlGn’, ‘YlGnBu’, ‘YlOrBr’, and ‘YlOrRd’.
    fill_opacity=0.7,
    line_opacity=0.3,
    nan_fill_color = 'white',
    nan_fill_opacity = 0.1,
    legend_name= '% mortalidade (media movel 7 ultimos dias)'
).add_to(m)

for key,estado in df.iterrows():
    dados = df[df['codigo_ibge']==estado.codigo_ibge]
    detalhes = '<center><b>'+dados.city.values[0] +'</b></center>\n'
    detalhes += 'casos: ' + str(dados.cases.values[0]) + ', mortes: ' + str(dados.deaths.values[0])
    detalhes += ', mortalidade: ' + str(dados.perc_death.values[0]) + '%'
#     detalhes = udetalhes
    
    folium.CircleMarker(
        location=[estado.latitude,estado.longitude],
        radius=2,
#         popup=detalhes,
        color='#727b7d',
        fill=True,
        fill_color='#ffff',
        tooltip=detalhes,
        icon=folium.Icon(color='blue',
             icon_color='black',
             icon='info-sign',
             prefix='es')
    ).add_to(m)

folium.LayerControl().add_to(m)

m.save('../analysis/maps/saoPauloMapDeaths.html')
m


# In[4]:


m = folium.Map(location=[-22.60, -48.44], zoom_start=7)

folium.Choropleth(
    geo_data=state_geo,
    name='Contaminações',
    data=df,
    columns=['codigo_ibge', 'avg7_cases'],
    key_on='feature.properties.codarea',
    fill_color='PuRd',#'YlGn',
    #     ‘BuGn’, ‘BuPu’, ‘GnBu’, ‘OrRd’, ‘PuBu’, ‘PuBuGn’, ‘PuRd’, ‘RdPu’, ‘YlGn’, ‘YlGnBu’, ‘YlOrBr’, and ‘YlOrRd’.
    fill_opacity=0.7,
    line_opacity=0.3,
    nan_fill_color = 'white',
    nan_fill_opacity = 0.1,
    legend_name='media movel de casos (7 ultimos dias)'
).add_to(m)

for key,estado in df.iterrows():
    dados = df[df['codigo_ibge']==estado.codigo_ibge]
    detalhes = '<center><b>'+dados.city.values[0] +'</b></center>\n'
    detalhes += 'casos: ' + str(dados.cases.values[0]) + ', mortes: ' + str(dados.deaths.values[0])
    detalhes += ', mortalidade: ' + str(dados.perc_death.values[0]) + '%'
#     detalhes = udetalhes
    
    folium.CircleMarker(
        location=[estado.latitude,estado.longitude],
        radius=2,
#         popup=detalhes,
        color='#727b7d',
        fill=True,
        fill_color='#ffff',
        tooltip=detalhes,
        icon=folium.Icon(color='blue',
             icon_color='black',
             icon='info-sign',
             prefix='es')
    ).add_to(m)

folium.LayerControl().add_to(m)

m.save('../analysis/maps/saoPauloMapCases.html')
m


# In[5]:


# #https://www.mankier.com/1/wkhtmltoimage#--width
# import imgkit
# print('Gerando imagens dos mapas de São Paulo')
# options = {
#     'format': 'png',
# #     'crop-h': '3',
# #     'crop-w': '3',
# #     'crop-x': '3',
# #     'crop-y': '3',
#     'width':'300',
#     'encoding': "UTF-8",
#     'custom-header' : [
#         ('Accept-Encoding', 'gzip')
#     ],
# }
# imgkit.from_file('../analysis/maps/saoPauloMapDeathsContainer.html', '../analysis/maps/saoPauloMapDeaths.png', options=options)
# imgkit.from_file('../analysis/maps/saoPauloMapCasesContainer.html', '../analysis/maps/saoPauloMapCases.png', options=options)


# ----------------------------
# ### São Paulo - Analysis and monitoring

# #### Top death cities  + Santa Gertrudes + Lucelia + Rio Claro

# In[19]:


cols = ['city', 'date', 'day','case_day', 'cases', 'death_day', 'deaths', 'avg7_cases', 'avg7_deaths','avg7_perc_death', 'perc_death']
addCity = ['santa gertrudes', 'lucelia', 'rio claro']

df_top_deaths = df[df['date']==today].sort_values('avg7_perc_death', ascending = False)

df_top_deaths.reset_index(0, inplace=True)
df_top_deaths.index = df_top_deaths.index + 1
df_top_deaths = df_top_deaths[cols].head(qtdeMonitored).append(df_top_deaths[df_top_deaths['city'].isin(addCity)][cols])

df_top_deaths


# In[12]:


df_top_deaths[(df_top_deaths['city']=='santa gertrudes') | (df_top_deaths['city']=='lucelia') | (df_top_deaths['city']=='rio claro')][cols]


# #### Top 10 most transmissible countries + Santa Gertrude + Lucélia + Rio Claro - São Paulo

# In[21]:


df_top_cases = df[df['date']==today].sort_values('avg7_cases', ascending = False)

df_top_cases.reset_index(0, inplace=True)
df_top_cases.index = df_top_cases.index + 1
df_top_cases = df_top_cases[cols].head(qtdeMonitored).append(df_top_cases[df_top_cases['city'].isin(addCity)][cols])

df_top_cases


# #### Cities of São Paulo to be analised

# #### Cases and deaths 

# In[22]:


#inform the countries you want to analise
monitoredCities = df_top_cases['city'].head(qtdeMonitored).to_numpy()
monitoredCities = np.delete(monitoredCities,np.where([monitoredCities == 'sao paulo'] or [monitoredCities == 'total geral']))
monitoredCities = np.append(monitoredCities,[addCity])


# In[23]:


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(20, 15))
fig.tight_layout(pad=5.0)

ax1.set_title("Cumulatative cases")
ax1.set_xlabel("days from the first case")
ax1.grid(color='gray', alpha = 0.4)

ax2.set_title("Cumulative deaths")
ax2.set_xlabel("days from the first case")
ax2.grid(color='gray', alpha = 0.4)

ax3.set_title("Cases - moving average (last 7 days)")
ax3.set_xlabel("days from the first case")
ax3.grid(color='gray', alpha = 0.4)

ax4.set_title("Deaths - moving average (last 7 days)")
ax4.set_xlabel("days from the first case")
ax4.grid(color='gray', alpha = 0.4)

for city in monitoredCities:
    ax1.plot(df[df['city'] == city].day, df[df['city'] == city].cases, label = city)
    ax2.plot(df[df['city'] == city].day, df[df['city'] == city].deaths, label = city)
    ax3.plot(df[df['city'] == city].day, df[df['city'] == city].avg7_cases, label = city)
    ax4.plot(df[df['city'] == city].day, df[df['city'] == city].avg7_deaths, label = city)
#     ax1.plot(df[df['country'] == country].day, df[df['country'] == country].cases, label = country)
#     ax2.plot(df[df['country'] == country].day, df[df['country'] == country].deaths, label = country)
#     ax3.plot(df[df['country'] == country].day, df[df['country'] == country].avg7_cases, label = country)
#     ax4.plot(df[df['country'] == country].day, df[df['country'] == country].avg7_deaths, label = country)

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
fig.savefig('../analysis/saoPaulo_cities_cases_deaths.png')


# ### Generating the html file

# In[28]:


f = open('../html/saoPaulo_analysis.html', 'w')
f1 = open('../html/templates/saoPaulo_analysis_01.html', 'r').read()
f2 = open('../html/templates/saoPaulo_analysis_02.html', 'r').read()
f3 = open('../html/templates/saoPaulo_analysis_03.html', 'r').read()

readme = f1
readme += '<p>Estas análises são relativas aos dados da pandemia Covid19 no estado de São Paulo até a data de <strong>' + today + '</strong>.</p>'
readme += f2
readme += '        <div class="container">'
readme += '          <h3>Top ' + str(qtdeMonitored) + ' cidades mais mortais do estado de São Paulo</h3>'
readme += '          <p><i>mais Santa Gertrudes, Rio Claro e Lucélia</i></p>'
readme += '          <p>O ranking é feito a partir da média móvel de 7 dias do percentual de mortalidade de cada cidade.</p>'
readme += df_top_deaths.to_html(classes='table', decimal=',', justify='justify')
readme += '        </div>'
readme += '        <br>'
readme += '        <div class="container">'
readme += '          <h3>Top ' + str(qtdeMonitored) + ' cidades mais transmissíveis do estado de São Paulo</h3>'
readme += '          <p><i>mais Santa Gertrudes, Rio Claro e Lucélia</i></p>'
readme += '          <p>O ranking é feito a partir da média móvel de 7 dias do percentual de casos acumulados de cada cidade.</p>'
readme += df_top_cases.to_html(classes='table', decimal=',', justify='justify')
readme += '        </div>'
readme += '        <br>'
readme += f3

f.write(readme)
f.close()

###########################################

f = open('../html/saoPaulo_analysis_EN.html', 'w')
f1 = open('../html/templates/saoPaulo_analysis_EN_01.html', 'r').read()
f2 = open('../html/templates/saoPaulo_analysis_EN_02.html', 'r').read()
f3 = open('../html/templates/saoPaulo_analysis_EN_03.html', 'r').read()

readme = f1
readme += '<p>These analysis are related to state of San Paulo Convid19 pandemic data up to <strong>' + today + '</strong>.</p>'
readme += f2
readme += '        <div class="container">'
readme += '          <h3>Top ' + str(qtdeMonitored) + ' deadliest cities of Sao Paulo</h3>'
readme += '          <p><i>plus Santa Gertrudes, Rio Claro and Lucélia</i></p>'
readme += '          <p>This ranking is done from the moving avarege of the last 7 days over the mortality percentage of each city.</p>'
readme += df_top_deaths.to_html(classes='table', decimal=',', justify='justify')
readme += '        </div>'
readme += '        <br>'
readme += '        <div class="container">'
readme += '          <h3>Top ' + str(qtdeMonitored) + ' most transmissible cities of Sao Paulo</h3>'
readme += '          <p><i>plus Santa Gertrudes, Rio Claro and Lucélia</i></p>'
readme += '          <p>This ranking is done from the moving avarege of the last 7 days over the cumulative cases of each city.</p>'
readme += df_top_cases.to_html(classes='table', decimal=',', justify='justify')
readme += '        </div>'
readme += '        <br>'
readme += f3

f.write(readme)
f.close()

print('Sao Paulo\'s analysis done!')


# In[11]:


# df[df['state']=='SP'][['date','death_day']]


# In[ ]:




