import os
import rich
from pytube import YouTube
from rich import print
from pytube.exceptions import PytubeError

def dlod():
    while True:
        url = input("Ссылка на видео: ")
        try:
            video = YouTube(url)
            print("***|Название видео|***")
            print(f"[bold green]{video.title}[/bold green]")
            print("**********************")
        except PytubeError as e:
            print(f"Error accessing video title: {e}")
            continue

        qs = input("Если хотите скачать нажмите ENTER, или нет нажмите N+ENTER: ")
        if qs == "":
            video1 = video.streams.get_highest_resolution()
            pht = "D:\Videos\YuLoader"
            video1.download(pht)
            qs2 = input("Хотите скачать что-нибудь ещё? ENTER - да | N + ENTER - нет: ")
            if qs2 == "":
                dlod()
            elif qs2 == "n":
                break
        elif qs == "n":
            break

dlod()