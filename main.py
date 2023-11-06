from pytube import YouTube
import tkinter
import customtkinter as ctk


def start_download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video= ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="green")
        video.download()
        finish.configure(text="Finished Downloading")
    except:
        finish.configure(text="Error", text_color="red")
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per=str(int(percentage_of_completion)) 
    progress.configure(text=per+"%")
    progress.update()

    progressBar.set(float(percentage_of_completion)/100)

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

# progress percentage
progress = ctk.CTkLabel(app, text="0%")
progress.pack()

progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)



# Download button
download = ctk.CTkButton(app, text="Download", command= start_download)
download.pack(padx=10, pady=10)

app.mainloop()
