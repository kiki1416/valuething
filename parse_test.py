'''
i hate pylance
'''
from bs4 import BeautifulSoup

with open("data/raw/rtx_4070_super.html", "r", encoding="utf-8") as file:
    html = file.read()
soup = BeautifulSoup(html, "lxml")

rows = soup.select('section.details dl.clearfix')
pairs = { r.find('dt').get_text(strip=True): }
print(value)