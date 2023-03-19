import requests 
from bs4 import BeautifulSoup 

#Motor
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}  

#Request da pagina (Dado)
page = requests.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&ei=YUESZL2rFJSa0AaehZWoAw&oq=cota&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDAToKCAAQRxDWBBCwAzoHCAAQsAMQQzoSCC4QxwEQ0QMQyAMQsAMQQxgBOgwILhDIAxCwAxBDGAE6CggAELEDEIMBEEM6BggAEAoQQzoECAAQQzoICAAQsQMQgwE6BQguEIAEOggILhCDARCxAzoRCC4QgAQQsQMQgwEQxwEQ0QM6CAguELEDEIMBOgsILhCABBCxAxCDAToFCAAQgARKBAhBGABQlQ9Y3hRggDhoBXABeACAAdgBiAHGBZIBBTAuMi4ymAEAoAEByAELwAEB2gEECAEYCA&sclient=gws-wiz-serp', headers= headers) 
page2 = requests.get('https://www.google.com/search?q=hor%C3%A1rio+de+bras%C3%ADlia&newwindow=1&hl=pt-BR&sxsrf=AJOqlzW_dfMl4gFIG5EzcYdPgbHacWVsFw%3A1679159744158&ei=wPEVZIqgCYiI4dUPkZ69qAI&oq=hor%C3%A1rio+de+br&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoHCAAQsAMQQzoNCAAQ5AIQ1gQQsAMYAToMCC4QyAMQsAMQQxgCOg8ILhDUAhDIAxCwAxBDGAI6BAgjECc6CwgAEIAEELEDEIMBOg4ILhDHARCxAxDRAxCABDoECAAQAzoICAAQsQMQgwE6BAgAEEM6EQguEIAEELEDEIMBEMcBENEDOgoIABCABBCxAxAKOgcIABCABBAKOg0IABCABBCxAxCDARAKSgQIQRgAUKNqWIyMAWC4lQFoCHABeACAAYEBiAG_CpIBAzYuN5gBAKABAcgBEsABAdoBBggBEAEYCdoBBggCEAEYCA&sclient=gws-wiz-serp', headers= headers)

#Aplicando a biblioteca (Conhecimento)
soup = BeautifulSoup(page.content, 'html.parser') 
soup2 = BeautifulSoup(page2.content, 'html.parser')

#Tratando os dados ()
horario = soup2.find_all('div', class_ ="gsrt vk_bk FzvWSb YwPhnf")[0]
valor_dolar = soup.find_all('span', class_ ="DFlfde SwHCTb")[0] 
data = soup2.find_all('div', class_="vk_gy vk_sh")[0]
local = soup2.find_all('span', class_="vk_gy vk_sh")[0]

#Saida de dados
print(f'Sistema Automatizado Vassouras\nHoje{data.text}\n{horario.text}{local.text}\nO dolar esta {valor_dolar.text}') 
