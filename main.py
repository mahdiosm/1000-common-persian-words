import requests
from bs4 import BeautifulSoup as Bs
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
f = open(os.path.join(BASE_DIR, 'words.txt'), 'w', encoding='utf8')

response = requests.get(
    "https://1000mostcommonwords.com/1000-most-common-persian-words/#:~:text=1000%20Most%20Common%20Persian%20Words"
    "%20%20%20,%20%20that%20%20114%20more%20rows%20")

response_content = response.content.decode()

ss = Bs(response_content, 'html.parser')

table = ss.find_all("table")[0]

all_trs = table.find_all("tr")[1:]

for div in all_trs:
    text = div.find_all("td")[1].text
    f.write(text)
    f.write('\n')
f.close()
