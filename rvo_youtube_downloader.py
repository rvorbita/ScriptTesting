import os
from pytube import YouTube

#README.
# Before using the Script download python3
# for windows user.  --> go to https://www.python.org/ 
# for linux user --> sudo apt-get install python3
# for mac user --> brew install python3

# After downloading python3
# download the pytube framework using pip
# pip install pytube

#DIRECTORY
CURRENT_DIR = os.getcwd()
MAIN_FOLDER="YT Download"
FULL_PATH = os.path.join(CURRENT_DIR, MAIN_FOLDER)
DIR_LIST = os.listdir(CURRENT_DIR)

#Audio and Video Folder
AUDIO_FOLDER="YT Download\Audio"
VIDEO_FOLDER="YT Download\Video"

def main_menu():
    #MENU
    print(""" 
         Python Youtube Downloader    
         High Quiality Video and Audio downloader 
         by: MC2022  
         
         1. Video/Audio Download        
         2. Audio Download Only         
         3. Quit   
    
    """)


def process_yt(url,type):

    print("Downloading...")
    print(f"Capturing the video :  {yt.title}")

    if type == "video":
        stream = yt.streams.filter(progressive=True,file_extension="mp4", res="720p").order_by("resolution").first().download(VIDEO_FOLDER)
    elif type == "audio":
        stream = yt.streams.filter(adaptive=True, type="audio").first().download(AUDIO_FOLDER)

    print("Download Completed!")


#Show the Main Menu.
while True:

    main_menu()

    print("Checking YT Download Folder.")

    #folder creation.
    #if folder does not exist, it will automatically be created
    if MAIN_FOLDER not in DIR_LIST:
        print("YT Download Folder does not exist.")
        print("Creating YT Download Folder.")
        os.mkdir(FULL_PATH)
        print("YT Download Folder Created...")
    else:
        print("YT Download Folder already exist.")

    #line-break
    print("")
    print("")


    menu = input("Enter your choose: ")

    if menu == '1':
        url = input("Enter YT URL: ")
        yt = YouTube(url)
        process_yt(yt,"video")

    elif menu == '2':
        url = input("Enter YT URL: ")
        yt = YouTube(url)
        process_yt(yt,"audio")

    elif menu == '3':
        print("Goodbye.")
        exit()

    else:
        print("Invalid Selection.")







