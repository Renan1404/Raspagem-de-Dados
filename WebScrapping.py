import requests 
from bs4 import BeautifulSoup 

 
 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}  
page = requests.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&ei=YUESZL2rFJSa0AaehZWoAw&oq=cota&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDAToKCAAQRxDWBBCwAzoHCAAQsAMQQzoSCC4QxwEQ0QMQyAMQsAMQQxgBOgwILhDIAxCwAxBDGAE6CggAELEDEIMBEEM6BggAEAoQQzoECAAQQzoICAAQsQMQgwE6BQguEIAEOggILhCDARCxAzoRCC4QgAQQsQMQgwEQxwEQ0QM6CAguELEDEIMBOgsILhCABBCxAxCDAToFCAAQgARKBAhBGABQlQ9Y3hRggDhoBXABeACAAdgBiAHGBZIBBTAuMi4ymAEAoAEByAELwAEB2gEECAEYCA&sclient=gws-wiz-serp', headers= headers) 
soup = BeautifulSoup(page.content, 'html.parser') 
valor_dolar = soup.find_all('span', class_ ="DFlfde SwHCTb")[0] 
print(valor_dolar) 
print(valor_dolar.text) 
print(valor_dolar['data-value'])  

 
