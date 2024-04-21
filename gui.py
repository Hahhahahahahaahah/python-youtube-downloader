import tkinter as tk
from tkinter import filedialog
from check_youtube_url import is_valid_url
from tkinter import messagebox
from pytube import YouTube


def download_video():
    url = website_entry.get()
    save_path = folder_path.get()

    if not save_path:
        messagebox.showerror("Error", "Please select a folder to save the video")
        return
    
    if not is_valid_url(url):
        messagebox.showerror("Error", "Please put a valid URL to save the video")
        return  
    
    Yt = YouTube(url)
    print(Yt.streams)

def select_folder():
    fs = filedialog.askdirectory()
    folder_path.set(fs)

window = tk.Tk()
window.title("Youtube Video Downloader")

tk.Label(window,text="Youtube URL").pack()  
website_entry = tk.Entry(window, width = 50)
website_entry.pack(padx=20)

numbers_var_1 = tk.BooleanVar()
numbers_var_2 = tk.BooleanVar()
Checkbutton = tk.Checkbutton(window, text="Download MP3?", variable = numbers_var_1)
Checkbutton.pack(padx=20)
Checkbutton2 = tk.Checkbutton(window, text="Download MP4?", variable = numbers_var_2)
Checkbutton2.pack(padx=20)

Folder_button = tk.Button(window , text = "Choose Folder", command= select_folder) 
Folder_button.pack()

folder_path = tk.StringVar()
path = tk.Entry(window, textvariable = folder_path, width = 50) 
path.pack(padx=20)

Download_button_2 = tk.Button(window , text = "Download", command = download_video)
Download_button_2.pack()

window.mainloop()