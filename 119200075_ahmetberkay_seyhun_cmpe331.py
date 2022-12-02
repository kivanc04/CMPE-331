# -*- coding: utf-8 -*-
"""119200075_ahmetberkay_seyhun_cmpe331.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/BerkaySeyhun/da28d21775eae82971510afb1a346a44/119200075_ahmetberkay_seyhun_cmpe331.ipynb

#Stage : Development -01
@author : Ahmet Berkay Seyhun , 119200075
@author : Müge Güney , 120200058
"""

pip install bs4  # install Beautiful Soup Librariy

import requests

from bs4 import BeautifulSoup

# Assign url value from airbnb to url variable
URL = "https://www.airbnb.com.tr/s/çanakkale/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change"

# Assign header value and give user agent value to website
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"}

site = requests.get(URL,headers=headers)

content = BeautifulSoup(site.content,"html.parser")

# print(content) // Just for testing

# We need price span id 
homeName= content.find(class="EMPTY").getText().strip()

price = content.find(id="EMPTY").getText().strip()

print(homeName)

print(price)