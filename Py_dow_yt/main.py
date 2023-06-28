# pytube говно
from pytube import *
from tkinter import *
from tkinter.ttk import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def dow_but(self):
        url = self.entry.get()
        download_video(url)

 
    def initUI(self):
        self.parent.title("Скачивание видео из ютуб")
        self.style = Style()
        self.style.theme_use("default")
 
        self.pack(fill=BOTH, expand=1)
 
        quitButton = Button(self, text="Скачать", command=self.dow_but)
        
        #label = Label(text="Hello, Tkinter",foreground="white",background="black")
        self.entry = Entry(width=50)
        
        #label.place(x=300, y=50)
        quitButton.place(x=100, y=50)
        self.entry.place(x=300, y=50)

def download_video(url):
    YouTube(url).streams.get_by_itag(22).download('C:/Users/Us1/Desktop/video')
    url_dow = YouTube(url)
    return url_dow

def main():
    # window = Tk()
    # #url = input("Введите ссылку для скачаивания видео - ")
    # window.geometry("800x460")
    # Example(window)
    # window.mainloop()


if __name__ == "__main__":
    main()
