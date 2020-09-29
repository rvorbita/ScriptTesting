#!/usr/bin/python3
#search anything from goole, open 5 tabs using webscrape.

from bs4 import BeautifulSoup
import requests, webbrowser, sys

source = requests.get('https://www.google.com/search?q='+''.join(sys.argv[1:]))
source.raise_for_status()

soup = BeautifulSoup(source.text, 'html.parser')
link = soup.find_all('a')

numOpen = min(5, len(link))

for i in range(numOpen):

    openTab = "https://www.google.com" + link[i].get('href')
    print(f"Opening {openTab}")
    webbrowser.open(openTab)

