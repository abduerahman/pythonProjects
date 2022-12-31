from pytube import YouTube
from pytube import Playlist

def download_vedio(link,data):
    yt = YouTube(link)
    downloads(yt.streams,data)

def downloads(streams,data):
    if(data[0] == "vedio"):
        streams.filter(res=data[1]).first().download()
        return
    else:
        streams.filter(type="audio").first().download()
        
def playlist_vedios(link,data):
    plty = Playlist(link)
    for url in plty.video_urls:
        download_vedio(url,data)

def downloader(link,data):
    if(link.__contains__('playlist')):
        playlist_vedios(link,data)
    else: 
        download_vedio(link,data)      
    
link = input('Enter The link: ')
data = []

input = input("Enter The type: ")
data.append(input)
input = input("Enter the reslution: ")
data.append(input)

downloader(link,data)