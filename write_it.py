#lib used requests and beautiful soup.
#print to the screen the full text of 
#the arcticle on a website.
#http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture


#install beautifulsoup
#install requests
import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")


#to get the title.
title = soup.find(class_="article main-content").h1.text

#loop to the main article
for article in soup.find_all(class_="article main-content"):
    

    #testing purposes.
    #to check the arcticle text and print
    if article.text:
        print(article.text.replace("\n", " ").strip())
    else:
        print(article.text.contents[0].strip())


#to save the arcticle text into a textfile.
with open("article.txt", "w") as file:
    file.write("Vanity Webpage Content\n\n")
    file.write("Content " + title + "\n\n")
    for i in article:
        file.write(i.text)

    print("Done.")
