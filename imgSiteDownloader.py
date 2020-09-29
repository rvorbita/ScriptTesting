#imgSiteDownloader - download img from photosite.
from bs4 import BeautifulSoup
import requests
import os


def img_downloader(seach, count):

    #create a dir where to save the pictures.
    url = "https://unsplash.com/s/photos/" + ''.join(search)
    os.makedirs('Unsplash', exist_ok=True)

    res = requests.get(url)
    res.raise_for_status

    #parse html using soup
    soup = BeautifulSoup(res.text, "html.parser")
    print("Searching photos......")
    source = soup.find_all("div", class_="_2vsJm", limit=count)

    for i, img in enumerate(source):

        img_url_s = source[i].a.get('href')
        img_url = img_url_s[: -5]

        #downlaod request.
        res = requests.get(img_url)
        res.raise_for_status()

        #download the image and move to created folder.
        imgFile = open(os.path.join('Unsplash', os.path.basename(f"{img_url}-{i}.jpeg")), "wb")
        print(f"Downloading the image {img_url}")
        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()

    return len(img_url)


search = input("Search photos: ")
count = int(input("How many imgs?: "))
download = img_downloader(search, count)

#check for completed downloads.
if download == 0:
    print("No images found.")
else:
    print(f"Their are {str(download)} files found")
    print(f"{str(count)} file(s) successfully downloaded")

print("Done!")

