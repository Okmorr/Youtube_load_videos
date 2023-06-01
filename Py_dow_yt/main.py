from pytube import YouTube

def download_video(url):
    url_dow = YouTube(url).streams.first().download('C:/Users/Us1/Desktop/1')
    return url_dow

def main():
    url = input("Введите ссылку для скачаивания видео - ")
    download_video(url)

if __name__ == "__main__":
    main()
