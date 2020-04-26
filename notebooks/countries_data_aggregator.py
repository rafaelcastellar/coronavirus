#!/usr/bin/env python
# coding: utf-8

# In[13]:


#https://population.un.org/wpp/Download/Standard/CSV/
#https://github.com/novelcovid/api
print('Initializing country/state data aggregator!')
import pandas as pd
import json
import requests


# ## World - Countries aggretation
# ### Fetching countries geo-data from corona.lmao.ninja's API

# In[14]:


url = "https://corona.lmao.ninja/v2/countries?sort=country"
req = requests.get(url)
j = json.loads(req.text)

# getting countries names for reference
countries = []
df = pd.DataFrame()
for country in j:
    countries.append(country)

df['country'] = pd.Series(countries)

# Parsing countries data do dict, then pandas dataframe
dic = []
i = 0
for country in countries:
    row = {'country': j[i]['country'], '_id': j[i]['countryInfo']['_id'], 'iso2': j[i]['countryInfo']['iso2'], 'iso3': j[i]['countryInfo']['iso3'],  
       'lat':j[i]['countryInfo']['lat'], 'long': j[i]['countryInfo']['long'], 'flag':j[i]['countryInfo']['flag']}
                 
    dic.append(row)
    i += 1 
df = pd.DataFrame.from_dict(dic)
df.tail()


# ### Fecthing countries data from UN's API
# #### 2019 data

# In[15]:


df_un= pd.read_csv('../data/WPP2019_TotalPopulationBySex.csv')
df_un = df_un[df_un['Time']==2019]
df_un.tail()


# In[16]:


# normalizing unmatchables country names
df_un.loc[df_un['Location']=='United States of America (and dependencies)', 'Location'] = 'US'
df_un.loc[df_un['Location']=='Bolivia (Plurinational State of)', 'Location'] = 'Bolivia'
df.loc[df['country']=='UK', 'country'] = 'United Kingdom'
df.loc[df['country']=='USA', 'country'] = 'US'

df_un.loc[df_un['Location']=='France']


# #### Merging both dataframes and saving to csv

# In[17]:


df_countries = pd.merge(df, df_un, how='inner', on=None, left_on='country', 
                 right_on='Location', left_index=False, right_index=False, sort=False)   

df_countries.drop(['_id', 'Location', 'MidPeriod'], axis=1, inplace=True)
df_countries.tail()


# In[6]:


df_countries.to_csv('../data/world_countries_2019.csv',  index = False)


# In[7]:


df_un['Location'].unique()


# ### Fetching São Paulo cities geo-data from IBGE's API

# In[12]:


#https://servicodados.ibge.gov.br/api/docs/localidades
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'google-colab',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
}
estado_jsons = requests.get("https://servicodados.ibge.gov.br/api/v2/malhas/35/?formato=application/vnd.geo+json&resolucao=5",
                           headers=headers)
estado_json = estado_jsons.json()

f = open('../data/saoPaulo-cidades.json', 'w')
json.dump(estado_json, f)
f.close()

cidades = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios",
                       headers=headers).json()
dic = []
for cidade in cidades:
    linha = {'id':cidade['id'], 'nome': cidade['nome']}
    dic.append(linha)

df_cidades = pd.DataFrame.from_dict(dic)
df_cidades.head()
df_cidades.to_csv('../data/saoPaulo_cities.csv',  index = False)


# In[10]:


print('Countries aggregation done!')


# In[ ]:




