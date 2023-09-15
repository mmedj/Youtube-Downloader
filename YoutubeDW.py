from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import *
import youtube_dl
import threading
root = Tk()
root.geometry('1200x800')
root.resizable(0,0)
root.config(bg='dark slate blue')
root.title("YouTube Downloader")
titre=Label(root,text = 'YouTube Video/Audio Downloader', font ='verdana 25 bold italic',pady=60)
titre.pack()
titre.config(bg='dark slate blue',fg='lavender')
link = StringVar()
zone=Label(root, text = 'Paste Link Here:', font = 'arial 15 bold underline')
zone.place(x= 525 , y = 160)
zone.config(bg='dark slate blue',fg='lavender')
link_enter = Entry(root, width = 70,textvariable = link).place(x = 400, y = 210)
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)
def MP4_Downloader():
    url =YouTube(str(link.get()))
    file_name=url.title
    my_progress.place(x=200, y=600)
    my_progress.config(mode="determinate")
    my_progress.start(10)
    lab1 = Label(root, text="Downloading...")
    lab1.place(x=800, y=600)
    video = url.streams.get_highest_resolution()
    video.download(path_label.cget("text"))
    my_progress.place_forget()
    lab1.place_forget()
    lab2=Label(root, text = f"Download complete... {file_name}", font = 'arial 12')
    lab2.place(x=300 , y = 600)
    root.after(6000,lab2.place_forget)
def MP3_downloader():
    my_progress.place(x=200, y=600)
    my_progress.config(mode="determinate")
    my_progress.start(10)
    lab1=Label(root,text="Downloading...")
    lab1.place(x=800, y=600)
    video_info = youtube_dl.YoutubeDL().extract_info(url =link.get(),download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':f'{path_label.cget("text")}\{filename}'
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    my_progress.place_forget()
    lab1.place_forget()
    lab2=Label(root,text=f"Download complete... {format(filename)}",font="arial 12")
    lab2.place(x=300,y=600)
    root.after(6000,lab2.place_forget)
def MP3_Playlist():
    p = Playlist(link.get())
    my_progress.place(x=200, y=600)
    my_progress.config(mode="determinate")
    my_progress.start(10)
    lab1 = Label(root, text="Downloading...")
    lab1.place(x=800, y=600)
    for url in p.video_urls:
        video_info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': f'{path_label.cget("text")}\{filename}'
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
    my_progress.place_forget()
    lab1.place_forget()
    lab2=Label(root, text="Download complete...", font="arial 12")
    lab2.place(x=300, y=600)
    root.after(6000,lab2.place_forget)
def MP4_Playlist():
    p = Playlist(link.get())
    my_progress.place(x=200, y=600)
    my_progress.config(mode="determinate")
    my_progress.start(10)
    lab1 = Label(root, text="Downloading...")
    lab1.place(x=800, y=600)
    for url in p.video_urls:
        ytb = YouTube(url)
        video = ytb.streams.get_highest_resolution()
        video.download(path_label.cget("text"))
    my_progress.place_forget()
    lab1.place_forget()
    lab2=Label(root, text="Download complete...", font="arial 12")
    lab2.place(x=300, y=600)
    root.after(6000,lab2.place_forget)
def playlist_downloader():
    ask=Label(root,text="Would you like to download this playlist as: ",font='arial 14')
    ask.place(x=420,y=440)
    ask.config(bg='dark slate blue',fg='white')
    Button(root,text='MP3',bg='indigo',fg='lavender',font ='arial 13',command=on_click_playlist_audio).place(x=550,y=500)
    Button(root,text='MP4',bg='indigo',fg='lavender',font='arial 13',command=on_click_playlist_video).place(x=620,y=500)
def on_clickMP3():
    thread = threading.Thread(target=MP3_downloader)
    thread.start()
def on_clickMP4():
    thread = threading.Thread(target=MP4_Downloader)
    thread.start()
def on_click_playlist_video():
    thread = threading.Thread(target=MP4_Playlist)
    thread.start()
def on_click_playlist_audio():
    thread = threading.Thread(target=MP3_Playlist)
    thread.start()
path_label = Label(root,text='Get Path')
Button(root,text='Select Path',fg='lavender',bg='indigo',font ='arial 20 bold',command=select_path).place(x=520,y=270)
Button(root,text = 'MP4 DOWNLOAD', font = 'arial 15 bold' ,bg = 'thistle',fg='dark slate blue', padx = 2, command = on_clickMP4).place(x=80 ,y = 380)
Button(root,text='MP3 DOWNLOAD',font='arial 15 bold',bg='thistle',fg='dark slate blue',padx=2,command = on_clickMP3).place(x=900,y=380)
Button(root,text='PLAYLIST',font='arial 15 bold',bg='thistle',fg='dark slate blue',padx=2,command = playlist_downloader).place(x=550,y=380)
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode="indeterminate")
root.mainloop()