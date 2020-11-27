import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

extracted = soup.find('div', class_='mw-parser-output')
tabledata = extracted.table.tbody
column_names = ['Postalcode','Borough','Neighborhood']
TableTrimed = pd.DataFrame(columns = column_names)

for tri in tabledata.find_all('tr'):
   cnt=0
   for tdi in tri.find_all('td'):
       cnt=cnt+1
       if cnt ==1:
           Postem=tdi.text
       elif cnt==2:
           Bortem=tdi.text
           if Bortem.find('Not assigned') != -1:
               Bortem=np.nan
       elif cnt==3:
           Neitem=tdi.text
           if Neitem.find('Not assigned') != -1:
               Neitem=Bortem
           TableTrimed = TableTrimed.append({'Postalcode': Postem,'Borough': Bortem,'Neighborhood': Neitem},ignore_index=True)

TableTrimedr=TableTrimed.dropna() 

print(TableTrimedr.shape)