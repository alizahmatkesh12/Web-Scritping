import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://mashadkala.com/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3?ProductTagId=26389'

for page in range(1, 3):
    url = f"{base_url}/?pagenumbe={page}"
    
    response = requests.get(url)  
    
    page_info = response.text
    soup = BeautifulSoup(page_info, 'html.parser')

    models = [model.text.strip() for model in soup.find_all(class_="englishtitle")]
    priceses = [price.text.strip() for price in soup.find_all(class_="km-value")]

    priceses = ['unavailable' if 'مشهد کالا' in price else re.sub(r'تومان', 't', re.sub(r'\.', '', price))
                    for price in priceses]      
          
    models = [re.sub(r'^\.{3}', '', model)
                    for model in models]

    for model, price in zip(models, priceses):
        print(f"model is {model} and price is {price}")
