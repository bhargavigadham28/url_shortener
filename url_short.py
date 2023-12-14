from tkinter import *
import pyshorteners

root=Tk()
root.title("URL Shortener")
root.resizable(0,0)
root.geometry("800x350")

def shortUrl():
    entered_url = url.get()
    result = pyshorteners.Shortener().tinyurl.short(entered_url)
    urlEntry.insert(END, result)

Label(root, text="Generate Short URL", font=("Georgia 45 bold"),fg="Purple").pack(pady=12)
frame_long = Frame(root)
Label(frame_long, text="Paste URL Here:", font=("Georgia 15 bold")).pack(side=LEFT)
url = Entry(frame_long, width="45",font=("Georgia"))
url.pack()
frame_long.pack(pady=12)

Button(root, text="Generate Link", font=("Georgia 15 bold"), command=shortUrl).pack(pady=12)
frame_short = Frame(root)
Label(frame_short, text="Shortened URL :", font=("Georgia 15 bold")).pack(side=LEFT)
urlEntry = Entry(frame_short, width="35", fg="Purple", font=("Georgia 15"))
urlEntry.pack()
frame_short.pack(pady=12)
root.mainloop()

