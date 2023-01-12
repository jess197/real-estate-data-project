#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
#%%
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
#%%

#%%
soup
# %%
houses = soup.find_all(
    'a', {'class': 'property-card__content-link js-card-title'}
)
qtd_imoveis = float(soup.find(
    'strong', {'class': 'results-summary__count'}).text.replace('.',''))
# %%
len(houses)
# %%
qtd_imoveis/36

# %%
house = houses[0]

#%%
house

#%%
df = pd.DataFrame(
    columns=[
        'description',
        'address',
        'area',
        'restrooms',
        'bathrooms',
        'garage',
        'price',
        'price_condo',
        'wlink'

    ]
)
i = 0
#%%
while qtd_imoveis > df.shape[0]:
    i += 1 
    print(i)
    print(f"valor i: {i} \t\t qtd_imoveis: {df.shape[0]}")
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    houses = soup.find_all(
        'a', {'class': 'property-card__content-link js-card-title'})
   
    for house in houses:
        try:
            description = house.find('span', {'class:', 'property-card__title'}).text.strip()
        except:
            description = None
        try:
            address = house.find('span',{'class:', 'property-card__address'}).text.strip()
        except: 
            address = None
        try:
            area = house.find('span',{'class:','property-card__detail-value'}).text.strip().replace(" ","")
        except:
            area = None
        try:
            restrooms = house.find('li',{'class:','property-card__detail-room'}).span.text.strip().replace("   "," ")
        except: 
            restrooms = None
        try:
            bathrooms = house.find('li',{'class:','property-card__detail-bathroom'}).span.text.strip().replace("   "," ")
        except:
            bathrooms = None
        try:
            garage = house.find('li',{'class:','property-card__detail-garage'}).span.text.strip().replace("   "," ")
        except:
            garage = None
        try:
            price = house.find('div',{'class:','property-card__price'}).p.text.strip().replace("   "," ")
        except: 
            price = None
        try:
            price_condo = house.find('strong',{'class:','js-condo-price'}).text.strip()
        except: 
            price_condo = None
        try:
            wlink = 'https://www.vivareal.com.br' + house['href']
        except:
            wlink = None

        df.loc[df.shape[0]] = [
            description,
            address,
            area,
            restrooms,
            bathrooms,
            garage,
            price,
            price_condo,
            wlink

        ]

#%%
print(description)
print(address)
print(area)
print(restrooms)
print(bathrooms)
print(garage)
print(price)
print(price_condo)
print(wlink)
#%%


# %%
df.to_csv('banco_de_imoveis.csv', sep=';', index=False)




# %%
