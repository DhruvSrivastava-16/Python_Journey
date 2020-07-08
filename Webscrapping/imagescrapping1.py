# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:10:28 2020

@author: DHRUV
"""


#image scrappin from passiton

import requests
from bs4 import BeautifulSoup as soup

url="https://www.passiton.com/inspirational-quotes"
response=requests.get(url)
data=response.content

data_soup=soup(data,'html.parser')

with open("scrapped.jpg","wb") as f:
    r=requests.get("https://assets.passiton.com/quotes/quote_artwork/5429/medium/20200514_thursday_quote.jpg?1588967448")
    d=r.content
    f.write(d)
    
    #wb means binary mode!