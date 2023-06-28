from pytube import YouTube

def download_video(url):
    YouTube(url).streams.get_by_itag(22).download('C:/Users/Us1/Desktop/video')
    url_dow = YouTube(url)
    return url_dow

def main():
    url = input("Введите ссылку для скачаивания видео - ")
    download_video(url)

if __name__ == "__main__":
    main()
