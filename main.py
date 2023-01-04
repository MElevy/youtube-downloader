import tkinter as tk
from threading import Thread
from youtube_dl import YoutubeDL

class YoutubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Youtube Downloader')

        self.url_input = tk.Entry(self, borderwidth=10, relief=tk.FLAT)
        self.url_input.grid(row=0, column=0, sticky='nsew')

        self.download_btn = tk.Button(self, text='Download', borderwidth=10, relief=tk.FLAT, bg='darkgray', command=self.download)
        self.download_btn.grid(row=0, column=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def download(self):
        url = self.url_input.get()

        Thread(target=self.download_video, args=(url,), daemon=True).start()

    def download_video(self, url):
        info = YoutubeDL().extract_info(url=url, download=False)
        out_file_path = '{video_title}.mp3'.format(video_title=info['title'])

        options = {
          'format': 'bestaudio/best',
          'keepvideo': False,
          'outtmpl': out_file_path
        }

        with YoutubeDL(options) as downloader:
            downloader.download([info['webpage_url']])

if __name__ == '__main__':
    YoutubeDownloader().mainloop()
