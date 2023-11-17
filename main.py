from pytube import *

class downloadAnyCodec:
#this class show all information of video in 2 extention: video and audio. And class can download

    def showAllVideoInPlaylist(self, link_on_playlist: str):
        p = Playlist(link_on_playlist)
        print(*p, sep="\n")

    
    def showAllCodec(self, link_on_video: str, type: str):
        try:    
            yt = YouTube(link_on_video)
            if type == "video":
                ans = yt.streams.filter(type="video")
            elif type == "audio":
                ans = yt.streams.filter(type="audio")

            print(*ans, sep="\n")

        except Exception:
            print("Ошибка при работе с YouTube")

    def downloadThisVideo(self, res: str, link_on_video: str):
        yt = YouTube(link_on_video)
        
        video = yt.streams.filter(resolution=f"{res}p").first().download(yt.title)
    

