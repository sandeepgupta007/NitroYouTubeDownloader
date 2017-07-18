#for Windows - Nitro YouTube Downloader

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from pytube import YouTube

def quality():
    print ('Video Quality -')
    print ('Enter 1 for Simple 360p')
    print ('Enter 2 for Baseline 480p')
    print ('Enter 3 for High 720p')
    video_quality = int(input())
    if (video_quality == 1):
        viedo_quality = 0
    elif(video_quality == 2):
        video_quality = -2
    else:
        video_quality = -1
    return video_quality

def download(url):
    yt = YouTube(url)
    video_quality = quality()
    video = yt.filter('mp4')[video_quality]
    print ('Your Video will be Downloaded in ~/Downloads/Nitro-YouTube-Downloader')
    download_folder = os.path.expanduser("~")+"/Downloads/"
    path = os.system('if not exist "download_folder/Nitro-YouTube-Downloader" mkdir download_folder/Nitro-YouTube-Downloader')
    
    #video.download(path)
    

def search():
    print ('Type your query :-) ',end=' ')
    query = input()
    for i in range(len(query)):
        if(query[i] == ' '):
            query = query[:i]+"+"+query[i+1:];

    search_url = urlopen("https://www.youtube.com/results?search_query=%s"%query)
    page = search_url.read()
    page_soup = soup(page,'lxml')
    count = 0
    links = {}
    for i in page_soup.find_all('h3',{'class':'yt-lockup-title '}):
        count+=1
        links[count] = i.a["href"]
        print ('!! ',count,' '+i.a["title"])
        if(count >= 15):
            break

    print ('Enter the number to be Downloaded - ',end=' ')
    download_choice = int(input())
    if(download_choice in links):
        URL = "http://www.youtube.com%s"%links[download_choice]
        download(URL)
        print ('You have Downloaded Video Effortlessly ! \n')
    else:
        print ('\n Wrong Choice')
        search()
    

def Playlist(playlist):
    playlist_url = urlopen(playlist)
    page = playlist_url.read()
    page_soup = soup(page,'lxml')
    count = 0
    video_quality = quality()
    for i in page_soup.find_all('td',{'class':'pl-video-title'}):
        count+=1
    print ('There are',count,'number of videos in Playlist to be downloaded')
    print ('Enter Location Complete Path - ')
    path = input()
    os.system('cls')
    Downloading=0
    for i in page_soup.find_all('td',{'class':'pl-video-title'}):
        Downloading += 1
        print ('Downloaded - ',end=' ')
        print (int((Downloading-1)/count)*100,'%')
        video = i.a["href"]
        URL = "http://www.youtube.com%s"%video
        yt = YouTube(URL)
        video = yt.filter('mp4')[video_quality]

        #video.download(path)
        
    
    
def type():
    while(True):
        out = True
        print ('Enter 1 for SEARCH')
        print ('Enter 2 for Download via link')
        print ('Enter 3 for Download Playlist')
        print ('Enter 4 for EXIT')
        print ('\n')
        print ('Your Choice - ',end=' ')
        choice = int(input())
        if(choice == 1):
            search()
        elif(choice == 2):
            print ("Paste your Video URL here: ",end=' ')
            video_url = input()
            download(video_url)
        elif(choice == 3):
            print("Paste your Playlist URL here: ",end=' ')
            playlist = input()
            Playlist(playlist)
        else:
            out = False
            print ('Really Exit - Enter any key to exit else press y -',end=' ')
            ch = input()
            if(ch == 'y' or ch == 'Y'):
                out = True
        if(out == False):
            exit()
            
        

def main():       
    print ("************* Nitro YouTube Downloader ************")
    type()

main()
