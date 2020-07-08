# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:30:19 2020

@author: DHRUV
"""


import requests 
from bs4 import BeautifulSoup as soup
import json

i=int(input("enter the joke no.: "))
url="http://api.icndb.com/jokes/{}".format(i)

response=requests.get(url)
data=response.content

data_html=soup(data,'html.parser')
data_json=json.loads(data)

the_joke=data_json['value']['joke']

print('chuck norris cracked: ',the_joke)