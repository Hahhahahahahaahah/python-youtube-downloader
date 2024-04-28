import tkinter as tk
from tkinter import filedialog
from check_youtube_url import is_valid_url
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

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
    try:
        Yt = YouTube(url)
        # print(Yt.streams)
       
        if numbers_var_1.get():
            audio_stream = Yt.streams.filter(only_audio = True).first() 
            if audio_stream:
                out_file = audio_stream.download(output_path = save_path)
                base, ext = os.path.splitext(out_file)
                new_file = base+".mp3"
                audio_clip = AudioFileClip(out_file)
                audio_clip.write_audiofile(new_file)
                audio_clip.close()
                os.remove(out_file)
        
        if numbers_var_2.get():
            video_streams = Yt.streams.filter(progressive = True,
                            file_extension = "mp4").order_by("resolution").desc().first()
            
            if video_streams:
                video_streams.download(save_path)

    except Exception as e:
        messagebox.showerror("Error", "failed to download")
    
    else:
        messagebox.showinfo(f"Success", f"Downloaded to {save_path}")



def select_folder():
    fs = filedialog.askdirectory(initialdir = os.getcwd())
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

folder_path = tk.StringVar(value = os.getcwd())
path = tk.Entry(window, textvariable = folder_path, width = 50, state = "disabled") 
path.pack(padx=20)

Download_button_2 = tk.Button(window , text = "Download", command = download_video)
Download_button_2.pack()

window.mainloop()