from bs4 import BeautifulSoup
import requests, os


url = "https://mangaread.co/manga/boruto-naruto-next-generations/ch-001/p/1/"
os.makedirs("manga", exist_ok=True)


while not url.endswith("https://mangaread.co/manga/boruto-naruto-next-generations/ch-001/p/64/"):

    print("Downloading the page.")
    res = requests.get(url)
    res.raise_for_status()

    print("Getting img source files.")
    soup = BeautifulSoup(res.content, "lxml")
    content = soup.find(class_="reading-content")
    img = content.img.get('data-src')
    print(img)

    # print("Downloading Image")
    res = requests.get(img)
    res.raise_for_status()

    imgfile = open(os.path.join('manga', os.path.basename(img)), "wb")
    for chunk in res.iter_content(100000):
        imgfile.write(chunk)
    imgfile.close()

    #get the new page link 
    nextLink = soup.find(class_="nav-next")
    url = nextLink.a.get('href')
    print(url)