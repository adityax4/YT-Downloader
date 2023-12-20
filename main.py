import tkinter
import customtkinter
from pytube import YouTube
from tkinter import filedialog

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="green")
        finishLabel.configure(text="")
        
        download_path = download_path_var.get()  # Get the chosen directory path
        if download_path:  # If a location is chosen
            video.download(output_path=download_path)
        
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Invalid Link", text_color="red")
    
def select_location():
    chosen_directory = filedialog.askdirectory()
    if chosen_directory:
        download_path_var.set(chosen_directory)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded/total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    
    #update progress bar
    progressBar.set(float(percentage_of_completion)/100)


#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app=customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding ui elements
title = customtkinter.CTkLabel(app, text="Insert YouTube Video URL")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Entry field to display chosen directory path
download_path_var = tkinter.StringVar()
download_path_entry = customtkinter.CTkEntry(app, width=200, height=30, textvariable=download_path_var)
download_path_entry.pack(padx=10, pady=10)

# Button to trigger file dialog
choose_location_button = customtkinter.CTkButton(app, text="Choose Download Location", command=select_location)
choose_location_button.pack(padx=10, pady=10)

#finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#progress percentage bar
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#run app
app.mainloop()