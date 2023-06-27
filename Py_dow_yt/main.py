from pytube import YouTube
from tkinter import *


# def download_video(url):
#     YouTube(url).streams.get_by_itag(22).download('C:/Users/Us1/Desktop/video')
#     url_dow = YouTube(url)
#     return url_dow


def main():
    window = Tk()
    #url = input("Введите ссылку для скачаивания видео - ")
    #download_video(url)
    window.geometry("800x460")
    window.mainloop()


if __name__ == "__main__":
    main()
