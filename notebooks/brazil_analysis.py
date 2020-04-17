#!/usr/bin/env python
# coding: utf-8

# In[187]:


#https://github.com/pomber/covid19
import numpy as np
import pandas as pd
import folium, html
import matplotlib.pyplot as plt
import datetime


# In[406]:


df = pd.read_csv('../data/brazil_corona19_data.csv')
df_estados = pd.read_csv('../data/brazilian_states.csv')
df['date'] = df['date'].astype('datetime64[ns]')

today = str(df.date.max().date())
tomorrow = str(df.date.max().date() + datetime.timedelta(days=1))
yesterday = str(df.date.max().date() - datetime.timedelta(days=1))

df.tail()


# In[451]:


df_brasil = pd.merge(df[df['date']==today], df_estados, how='inner', on=None, left_on='state', 
                 right_on='sigla_estado', left_index=False, right_index=False, sort=False)   

df_brasil = df_brasil[df_brasil['date']==today][['id_estado','avg7_perc_death','sigla_estado','nome_estado','cases','deaths','perc_death']]
df_brasil['id_estado'] = df_brasil['id_estado'].astype('str')# para fazer o key_on no folium

df_brasil.tail()


# In[410]:


state_geo = json.load(open('../data/brasil-estados.json'))
for state in state_geo['features']: 
    latLon =  state['properties']['centroide']
    codarea = state['properties']['codarea']
    df_estados.loc[df_estados['id_estado']==int(codarea),'lat'] = latLon[1]
    df_estados.loc[df_estados['id_estado']==int(codarea),'lon'] = latLon[0]

df_estados.tail()


# In[472]:


state_geo = json.load(open('../data/brasil-estados.json'))
m = folium.Map(location=[-15.75, -47.95], zoom_start=4)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=df_brasil,
    columns=['id_estado', 'avg7_perc_death'],
    key_on='feature.properties.codarea',
    fill_color='YlOrRd',#'YlGn',
#     ‘BuGn’, ‘BuPu’, ‘GnBu’, ‘OrRd’, ‘PuBu’, ‘PuBuGn’, ‘PuRd’, ‘RdPu’, ‘YlGn’, ‘YlGnBu’, ‘YlOrBr’, and ‘YlOrRd’.
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name='% letalidade (media movel 7 ultimos dias)'
).add_to(m)

for key,estado in df_estados.iterrows():
    dados = df_brasil[df_brasil['sigla_estado']==estado.sigla_estado]
    detalhes = '<center><b>'+dados.nome_estado.values[0] + ' (' + dados.sigla_estado.values[0] + ')</b></center>\n'
    detalhes += 'casos: ' + str(dados.cases.values[0]) + ', mortes: ' + str(dados.deaths.values[0])
    detalhes += ', letalidade: ' + str(dados.perc_death.values[0]) + '%'
#     detalhes = udetalhes
    
    folium.CircleMarker(
        location=[estado.lat,estado.lon],
        radius=5,
#         popup=detalhes,
        color='#727b7d',
        fill=True,
        fill_color='#727b7d',
        
        tooltip=detalhes,
        icon=folium.Icon(color='blue',
             icon_color='black',
             icon='info-sign',
             prefix='es')
    ).add_to(m)

folium.LayerControl().add_to(m)

m.save('../analysis/brazilMap.html')
m


# ----------------------------
# ### Brasil - Analysis and monitoring

# #### Top 5 deadliest countries + Brazil

# In[168]:


cols = ['state', 'date', 'day','case_day', 'cases', 'death_day', 'deaths', 'avg7_cases', 'avg7_deaths','avg7_perc_death', 'perc_death']
df_top_deaths = df[df['date']==today].sort_values('avg7_perc_death', ascending = False)

df_top_deaths.reset_index(0, inplace=True)
df_top_deaths.index = df_top_deaths.index + 1
df_top_deaths = df_top_deaths[cols].head(10)
df_top_deaths


# #### Top 5 most transmissible countries + Brazil

# In[169]:


df_top_cases = df[df['date']==today].sort_values('avg7_cases', ascending = False)

df_top_cases.reset_index(0, inplace=True)
df_top_cases.index = df_top_cases.index + 1
df_top_cases = df_top_cases[cols].head(10)
df_top_cases


# #### Brazilian states to be analised

# #### Cases and deaths 

# In[379]:


#inform the countries you want to analise
monitoredStates = df_top_deaths['state'].head(10).to_numpy()
monitoredStates


# In[380]:


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

for state in monitoredStates:
    ax1.plot(df[df['state'] == state].day, df[df['state'] == state].cases, label = state)
    ax2.plot(df[df['state'] == state].day, df[df['state'] == state].deaths, label = state)
    ax3.plot(df[df['state'] == state].day, df[df['state'] == state].avg7_cases, label = state)
    ax4.plot(df[df['state'] == state].day, df[df['state'] == state].avg7_deaths, label = state)
#     ax1.plot(df[df['country'] == country].day, df[df['country'] == country].cases, label = country)
#     ax2.plot(df[df['country'] == country].day, df[df['country'] == country].deaths, label = country)
#     ax3.plot(df[df['country'] == country].day, df[df['country'] == country].avg7_cases, label = country)
#     ax4.plot(df[df['country'] == country].day, df[df['country'] == country].avg7_deaths, label = country)

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
fig.savefig('../analysis/brazilian_states_cases_deaths.png')


# ### Generating the markdown file

# In[475]:


f = open('../analysis/README.md', 'w')

readme = '[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/gb.png" width="40"  /> English version](README_EN.md)'
readme += '\n\n#**Análises e monitoramento**\n'

readme += '\n###Letalidade dos estados brasileiros\n'
readme += 'O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.\n'
readme += '<<insertHTML:[brazilMap.html]'

readme += 'Estas análises são relativas aos dados da pandemia Covid19 no Brasil até a data de **' + today + '**.\n\n'
readme += 'Como existem muitos estados, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionados os 10 mais mortais:'
readme += str(monitoredStates) + '.\n\n'
readme += '\n***Dica**: você pode alterar você mesmo neste notebook quais estados você prefere comparar.*\n\n'
readme += '## Top 10 estados mais letais do Brasil\n'
readme += df_top_deaths.to_markdown()
# readme += tabulate(df_top_deaths.values,df_top_deaths.columns, tablefmt="pipe")
readme += '\n\n\n ## Top 10 estados mais transmissíveis do Brasil\n'
readme += df_top_cases.to_markdown()
#tabulate(df_top_cases.values,df_top_cases.columns, tablefmt="pipe")

readme += '\n----------------------\n'
readme += '## Casos e mortes\n'
readme += '![](brazilian_states_cases_deaths.png)'

readme += '\n\n [Comparativos do Brasil com outro países do mundo podem ser encontratos aqui.](README_WORLD.md#brazils-analysis)'


f.write(readme)
f.close()

###########################################

f = open('../analysis/README_EN.md', 'w')
readme = '[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="40"  /> Versão em português](README_WORLD.md)'

readme += '\n\n#**Analysis and monitoring**\n'

readme += '\n###Lethality of the brazilian states\n'
readme += 'The lethality level shown in this map is defined from the moving average of the last 7 days of each state lethality.\n'
readme += '<<insertHTML:[brazilMap.html]'

readme += 'These analysis are related to Brazil Convid19 pandemic data up to **' + today + '**.\n\n'
readme += 'As there are too many states to have their data plotted together, were selected the 10 deadliest:'
readme += str(monitoredStates) + '.\n\n'
readme += '\n***Tip**: you can yourself select in this notebook which states you prefer to compare.*\n\n'
readme += '## Top 5 deadliest states of Brazil\n'
readme += df_top_deaths.to_markdown()
# readme += tabulate(df_top_deaths.values,df_top_deaths.columns, tablefmt="pipe")
readme += '\n\n\n ## Top 5 most transmissible states of Brazil\n'
readme += df_top_cases.to_markdown()
#tabulate(df_top_cases.values,df_top_cases.columns, tablefmt="pipe")

readme += '\n----------------------\n'
readme += '## Cases and deaths\n'
readme += '![](brazilian_states_cases_deaths.png)'

readme += '\n\n [Comparison of Brazil and among some other contries around the world can be found here.](README_WORLD_EN.md#brazils-analysis)'

f.write(readme)
f.close()
print('Brazilian analysis done!')


# In[ ]:




