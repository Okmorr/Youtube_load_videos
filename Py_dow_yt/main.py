from pytube import YouTube

def download_video():
    url = input("Введите ссылку для скачаивания видео - ")
    url_dow = YouTube(url).streams.first().download('C:/Users/Us1/Desktop/Py_dow_yt')
    return url_dow

def main():
    download_video()

if __name__ == "__main__":
    main()
