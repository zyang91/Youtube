from pytube import YouTube
import tkinter
import customtkinter as ctk


def start_download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video= ytObject.streams.get_highest_resolution()
        video.download()
        finish.configure(text="Finished Downloading")
    except:
        finish.configure(text="Error", text_color="red")
    

#GUI setup
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#GUI frame
app= ctk.CTk()
app.title("Youtube Downloader")
app.geometry("720x480")

# Adding GUi elements
title = ctk.CTkLabel(app, text="Insert a youtube link:", font=("Arial", 20))
title.pack(padx=10, pady=10)

#link input
url =tkinter.StringVar()
link = ctk.CTkEntry(app, textvariable=url, width=350, height= 40)
link.pack()

# Finished Downloading
finish = ctk.CTkLabel(app, text="")
finish.pack()

# Download button
download = ctk.CTkButton(app, text="Download", command= start_download)
download.pack(padx=10, pady=10)

app.mainloop()
