import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'

response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('#content > div.article > div.section > div.section_sise_top > div.group_type.is_active > table > tbody')

trs = tbody.select('tr')
datas = []
for tr in trs:
  name = tr.select_one('th > a').get_text()
  current_price = tr.select_one('td').get_text()
  change = tr.select_one('em > span').get_text()
  change_rate = tr.select_one('td:nth-child(4)').get_text()
  datas.append([name,current_price,change,change_rate])

print("TOP 종목")

for i in range(0,len(datas),1):
  print(datas[i])
