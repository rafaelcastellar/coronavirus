#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Initializing data engineering!')
import pandas as pd
import numpy as np
import datetime
from pandas.io.json import json_normalize
import json, requests


# ### World data engineering
# #### Fetching worldwide data

# In[2]:


# df = pd.read_json('https://pomber.github.io/covid19/timeseries.json')
# df = pd.read_json('https://covidapi.info/api/v1/country/BRA')
# df = pd.read_json('https://api.covid19api.com/dayone/country/brazil/status/confirmed')
#https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#cc76052f-6601-4645-80e5-ca7aaa36f8ef
df_countries = pd.read_csv('../data/world_countries_2019.csv')

df = pd.DataFrame()
url = "https://pomber.github.io/covid19/timeseries.json"
req = requests.get(url)
# r = r.json()
j = json.loads(req.text)


# #### Fetching countries's pandemic data from Pomber's JSON to a dataframe 

# In[3]:


# Loading countries names to dict
countries = []
df = pd.DataFrame()
for country in j:
    countries.append(country)

df['country'] = pd.Series(countries)

# Loading countries data do dict then to dataframe
dic = []
for country in countries:
    i = 0
    while i < len(j[country]):
        if j[country][i]['confirmed'] == 0:
            i += 1
            continue
        row = {'country': country, 'date': j[country][i]['date'], 'cases':j[country][i]['confirmed'],
               'deaths':j[country][i]['deaths'], 'recoveries':j[country][i]['recovered']}
        dic.append(row)
        i += 1 
df = pd.DataFrame.from_dict(dic)
df[df['country']=='Brazil'].tail()


# #### Feature engineering

# In[4]:


for country in countries:
    qtdeDays = len(df[df.country == country])+1
    df.loc[df.country == country, 'day'] = (np.arange(1,qtdeDays,1))
#     df.drop(df[case].index, inplace=True)
    # valores diários
    df.loc[df.country == country, 'case_day'] = df[df.country == country]['cases'].diff()    
    df.loc[df.country == country, 'death_day'] = df[df.country == country]['deaths'].diff()
    df.loc[df.country == country, 'recovery_day'] = df[df.country == country]['recoveries'].diff()

    # % daily variations
    df.loc[df.country == country, '%var_case_day'] = ((df[df.country == country]['case_day'] - df[df.country == country]['case_day'].shift()) / df[df.country == country]['case_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    df.loc[df.country == country, '%var_death_day'] = ((df[df.country == country]['death_day'] - df[df.country == country]['death_day'].shift()) / df[df.country == country]['death_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    df.loc[df.country == country, '%var_recovery_day'] = ((df[df.country == country]['recovery_day'] - df[df.country == country]['recovery_day'].shift()) / df[df.country == country]['recovery_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    
    # Igualo o valor da primeira linha igual ao primeiro número do acumulado, pois se o acumulado começa em 1 o primeiro diff fica igual a 0
    df.loc[(df.country == country) & (df.day == 1), 'case_day']= df.loc[(df.country == country) & (df.day==1), 'cases']
    df.loc[(df.country == country) & (df.day == 1), 'death_day']= df.loc[(df.country == country) & (df.day==1), 'deaths']
    df.loc[(df.country == country) & (df.day == 1), 'recovery_day']= df.loc[(df.country == country) & (df.day==1), 'recoveries']
    
    # Buscando a população do país e calculado os indicador per milhão
    if not df_countries[df_countries['country']==country].empty:
        million = df_countries[df_countries['country']==country]['PopTotal'].values[0] / 1000
        cases_million = (df[df.country == country]['case_day'] / million).round(1)
        deaths_million = (df[df.country == country]['death_day'] / million).round(1)
        recoveries_million = (df[df.country == country]['recovery_day'] / million).round(1)
    else:
        cases_million = 0
        deaths_million = 0
        recoveries_million = 0
    
    df.loc[df.country == country, 'cases_million'] = cases_million
    df.loc[df.country == country, 'deaths_million'] = deaths_million
    df.loc[df.country == country, 'recoveries_million'] = recoveries_million
    
    # moving averages (from last 7 days)
    df.loc[df.country == country, 'avg7_cases'] = df[df.country == country]['case_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_deaths'] = df[df.country == country]['death_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_recoveries'] = df[df.country == country]['recovery_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    
    df.loc[df.country == country, 'avg7_cases_million'] = df[df.country == country]['cases_million'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_deaths_million'] = df[df.country == country]['deaths_million'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_recoveries_million'] = df[df.country == country]['recoveries_million'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    

df['perc_death'] = (df['deaths']/df['cases'] * 100).round(2)
df['perc_recovery'] = (df['recoveries']/df['cases'] * 100).round(2)
df['active_cases'] = df['cases'] - df['recoveries'] - df['deaths']

df.fillna(0, inplace=True)

df['day'] = df['day'].astype('int')
df['case_day'] = df['case_day'].astype('int')
df['death_day'] = df['death_day'].astype('int')
df['recovery_day'] = df['recovery_day'].astype('int')

df.tail()


# In[5]:


#Adjusting wrong negative variations (wrong number from the source)
# df.loc[df.case_day < 0, ['cases']] = df[df.case_day < 0].shift().cases#, ['cases']]
df.loc[df.case_day < 0, ['case_day']] = df[df.case_day < 0].shift().case_day#, ['cases']]
df.loc[df.cases_million < 0, ['cases_million']] = 0#df[df.cases_million < 0].cases_million.shift()#, ['cases']]
# country = 'Spain'

# df.case_day.min()
# df[df.cases_million < 0].cases_million.shift()
# df.loc[df.index == df[df['country']=='Spain'].cases.min()]
# plt.plot(df[df['country']=='Spain'].case_day)


# #### Saving CSV

# In[6]:


df.to_csv('../data/world_corona19_data.csv', index = False)


# In[7]:


df[df['country']=='Brazil'].tail()


# #### countries not located in UN dataset

# In[8]:


for country in countries:
    if df_countries[df_countries['country']==country]['PopTotal'].empty:
        print(country)
# df[df['pais'] == pais].tail()
# df_countries[df_countries['Location']==pais]['PopTotal']


# ### Brazil data engineering

# In[9]:


import requests

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'x-parse-application-id':'unAFkcaNDeXajurGB7LChj8SgQYS2ptm',
}
req = requests.get("https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeral",
                           headers=headers)
req_json = req.json()
url = req_json['results'][0]['arquivo']['url']
response = requests.get(url)

with open('../data/gov_brazil_corona19_data.csv', 'wb') as f:
    f.write(response.content)

df = pd.read_csv('../data/gov_brazil_corona19_data.csv', sep=';')
df.rename(columns={'regiao': 'region', 'estado':'state', 'data':'date','casosNovos': 'case_day', 'casosAcumulados':'cases', 'obitosNovos':'death_day','obitosAcumulados':'deaths'}, inplace= True)
df['date'] = df['date'].astype('datetime64[ns]')

df.tail()


# #### Feature engineering

# In[10]:


states = df.state.unique()
df.drop(df[df['cases'] == 0 ].index, axis=0, inplace= True)

for state in states:
    qtdeDays = len(df[df.state == state])+1
    df.loc[df.state == state, 'day'] = (np.arange(1,qtdeDays,1))
#     df.drop(df[case].index, inplace=True)
    # valores diários
    df.loc[df.state == state, 'case_day'] = df[df.state == state]['cases'].diff()    
    df.loc[df.state == state, 'death_day'] = df[df.state == state]['deaths'].diff()
#     df.loc[df.state == state, 'recovery_day'] = df[df.state == state]['recoveries'].diff()

    # % daily variations
    df.loc[df.state == state, '%var_case_day'] = ((df[df.state == state]['case_day'] - df[df.state == state]['case_day'].shift()) / df[df.state == state]['case_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    df.loc[df.state == state, '%var_death_day'] = ((df[df.state == state]['death_day'] - df[df.state == state]['death_day'].shift()) / df[df.state == state]['death_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
#     df.loc[df.state == state, '%var_recovery_day'] = ((df[df.state == state]['recovery_day'] - df[df.state == state]['recovery_day'].shift()) / df[df.state == state]['recovery_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    
    # Igualo o valor da primeira linha igual ao primeiro número do acumulado, pois se o acumulado começa em 1 o primeiro diff fica igual a 0
    df.loc[(df.state == state) & (df.day == 1), 'case_day']= df.loc[(df.state == state) & (df.day==1), 'cases']
    df.loc[(df.state == state) & (df.day == 1), 'death_day']= df.loc[(df.state == state) & (df.day==1), 'deaths']
    
    # moving averages (from last 7 days)
    df.loc[df.state == state, 'avg7_cases'] = df[df.state == state]['case_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.state == state, 'avg7_deaths'] = df[df.state == state]['death_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.state == state, 'perc_death'] = (df[df.state == state]['deaths']/df[df.state == state]['cases']*100).round(2) 
    df.loc[df.state == state, 'avg7_perc_death'] = df[df.state == state]['perc_death'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)

df['perc_death'] = (df['deaths']/df['cases'] * 100).round(2)
# df['perc_recovery'] = (df['recoveries']/df['cases'] * 100).round(2)
# df['active_cases'] = df['cases'] - df['recoveries'] - df['deaths']

df.fillna(0, inplace=True)

df['day'] = df['day'].astype('int')
df['case_day'] = df['case_day'].astype('int')
df['death_day'] = df['death_day'].astype('int')
# df['recovery_day'] = df['recovery_day'].astype('int')

df.tail()


# In[11]:


df.to_csv('../data/brazil_corona19_data.csv', index = False)


# ### São Paulo data engineering

# In[12]:


df = pd.read_csv('https://raw.githubusercontent.com/seade-R/dados-covid-sp/master/data/dados_covid_sp.csv', sep=';')
df.rename(columns={'munic': 'city', 'casos': 'cases','obitos':'deaths'}, inplace= True)
df['date'] = pd.to_datetime(dict(year=2020, month=df.mes, day=df.dia))
df.fillna(0, inplace = True)
df.drop(['dia','mes'], inplace=True, axis=1)

df = df[~df['city'].isin(['ignorado','outro estado', 'total geral', 'outro pais'])] 

df.tail()


# #### Feature engineering

# In[13]:


cities = df.city.unique()
df.drop(df[df['cases'] == 0 ].index, axis=0, inplace= True)

for city in cities:
    qtdeDays = len(df[df.city == city])+1
    df.loc[df.city == city, 'day'] = (np.arange(1,qtdeDays,1))
#     df.drop(df[case].index, inplace=True)
    # valores diários
    df.loc[df.city == city, 'case_day'] = df[df.city == city]['cases'].diff()    
    df.loc[df.city == city, 'death_day'] = df[df.city == city]['deaths'].diff()
#     df.loc[df.city == city, 'recovery_day'] = df[df.city == city]['recoveries'].diff()

    # % daily variations
    df.loc[df.city == city, '%var_case_day'] = ((df[df.city == city]['case_day'] - df[df.city == city]['case_day'].shift()) / df[df.city == city]['case_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    df.loc[df.city == city, '%var_death_day'] = ((df[df.city == city]['death_day'] - df[df.city == city]['death_day'].shift()) / df[df.city == city]['death_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
#     df.loc[df.city == city, '%var_recovery_day'] = ((df[df.city == city]['recovery_day'] - df[df.city == city]['recovery_day'].shift()) / df[df.city == city]['recovery_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    
    # Igualo o valor da primeira linha igual ao primeiro número do acumulado, pois se o acumulado começa em 1 o primeiro diff fica igual a 0
    df.loc[(df.city == city) & (df.day == 1), 'case_day']= df.loc[(df.city == city) & (df.day==1), 'cases']
    df.loc[(df.city == city) & (df.day == 1), 'death_day']= df.loc[(df.city == city) & (df.day==1), 'deaths']
    
    # moving averages (from last 7 days)
    df.loc[df.city == city, 'avg7_cases'] = df[df.city == city]['case_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.city == city, 'avg7_deaths'] = df[df.city == city]['death_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.city == city, 'perc_death'] = (df[df.city == city]['deaths']/df[df.city == city]['cases']*100).round(2) 
    df.loc[df.city == city, 'avg7_perc_death'] = df[df.city == city]['perc_death'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)

df['perc_death'] = (df['deaths']/df['cases'] * 100).round(2)
# df['perc_recovery'] = (df['recoveries']/df['cases'] * 100).round(2)
# df['active_cases'] = df['cases'] - df['recoveries'] - df['deaths']

df.fillna(0, inplace=True)

df['day'] = df['day'].astype('int')
df['case_day'] = df['case_day'].astype('int')
df['death_day'] = df['death_day'].astype('int')
# df['recovery_day'] = df['recovery_day'].astype('int')

df.tail()


# In[14]:


df.to_csv('../data/saoPaulo_corona19_data.csv', index = False)


# In[15]:


# df[df['country']=='Belgium']
print('Data engineering done!')


# In[ ]:





# In[ ]:




