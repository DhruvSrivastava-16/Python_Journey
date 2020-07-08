# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 00:14:22 2020

@author: DHRUV
"""

import requests
from bs4 import BeautifulSoup as soup

url="http://books.toscrape.com/"

data_response=requests.get(url)
data=data_response.content
data_soup=soup(data,'html.parser')