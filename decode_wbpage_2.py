#lib used requests and beautiful soup.
#print to the screen the full text of 
#the arcticle on a website.
#http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture


#install beautifulsoup
#install requests

import requests
import pprint
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

title = soup.find(class_="article main-content").h1.text



for article in soup.find_all(class_="article main-content"):
    
    if article.text:
        print(article.text.replace("\n", " ").strip())
    else:
        print(article.text.contents[0].strip())


with open("article.txt", "w") as file:

    file.write("Vanity Webpage Content\n\n")
    file.write("Content " + title + "\n\n")
    for i in article:
        file.write(i.text)

    print("Done.")

    





