# Michelle Scheuer
# 9/9/2021

import sys
from bs4 import BeautifulSoup
import requests

url = sys.argv[1]
response = requests.get(url, allow_redirects=True)
data = response.text
soup = BeautifulSoup(data, features="html.parser")

for link in soup.find_all('a'):
    all_links = link.get('href')
    my_list = [all_links]

    for i in my_list:
        if i.startswith("http"):
            res = requests.get(i)
            if res.headers['Content-Type'] == 'application/pdf':
                print("URI:", i, "\n",
                      "Final URL:", i, "\n",
                      "Content length:", "{:,}".format(eval(res.headers['Content-Length'])), "bytes \n")
