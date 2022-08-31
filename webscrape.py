import requests
from bs4 import BeautifulSoup

deger = input("Futbolcu İsmi Girin: ")
SELECTOR = "#yw0 > table > tbody > tr:nth-child(1) > td.rechts.hauptlink"
SELECTOR1 = "#yw0 > table > tbody > tr:nth-child(1) > td:nth-child(4)"
SELECTOR2 = "#yw0 > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(1) > td.hauptlink > a"
SELECTOR3 = "#yw0 > table > tbody > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(2) > td > a"
SELECTOR4 = "#yw0 > table > tbody > tr:nth-child(1) > td:nth-child(5) > img:nth-child(1) "

URLTemp = "https://www.transfermarkt.com.tr/schnellsuche/ergebnis/schnellsuche?query="
URL = URLTemp + deger


html = requests.get(
    URL,
    headers={
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
    }
).text.encode("utf-8")
soup = BeautifulSoup(html, "html.parser")
fiyat = soup.select_one(SELECTOR).text
yas = soup.select_one(SELECTOR1).text
isim = soup.select_one(SELECTOR2).text
takim = soup.select_one(SELECTOR3).text
uyruk = soup.select_one(SELECTOR4).get('title')

print(isim,yas,uyruk,takim,fiyat)
