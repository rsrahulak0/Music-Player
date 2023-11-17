from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("669x640+290+85")
root.configure(bg="black")
root.resizable(False, False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

def stop_song():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

def pause_song():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

def resume_song():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])


#icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

top = PhotoImage(file="top.png")
Label(root, image=top, bg="#0f1a2b").pack()

#logo
Logo = PhotoImage(file="logo.png")
Label(root, image=Logo, bg="#0f1a2b").place(y=20)

#button
play_button = PhotoImage(file="play-modified.png")
Button(root, image=play_button,bg="#0f1a2b", bd=0, command=play_song).place(x=70, y=300)

stop_button = PhotoImage(file="stop-modified.png")
Button(root, image=stop_button,bg="#0f1a2b", bd=0, command=stop_song).place(x=100, y=500)

resume_button = PhotoImage(file="resume-modified.png")
Button(root, image=resume_button,bg="#0f1a2b", bd=0, command=resume_song).place(x=30, y=500)

pause_button = PhotoImage(file="pause-modified.png")
Button(root, image=pause_button,bg="#0f1a2b", bd=0, command=pause_song).place(x=170, y=500)

#label
music = Label(root, text="", font=("arial", 15), fg="white", bg="#0f1a2b")
music.place(x=150, y=340, anchor="center")

#music
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=265, y=270, width=560, height=250)

Button(root, text="Open Folder", width=15, height=2, font=("arial", 10, "bold"), fg="white", bg="#21b3de", command=open_folder).place(x=265, y=220)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("arial", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)





root.mainloop()