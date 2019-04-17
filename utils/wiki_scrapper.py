from urllib.request import urlopen
from bs4 import BeautifulSoup
import io

with urlopen('https://gbf.wiki/Tiamat_(Raid)#Omega%20Showdown') as resp:
    soup = BeautifulSoup(resp.read(), 'lxml')
with io.open('res.html', 'w', encoding='utf-8') as fp:
    tabs = soup.find_all('div', class_='tabbertab')
    for tab in tabs:
        fp.write(tab.prettify())
