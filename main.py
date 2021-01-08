from tkinter import *
import pygame as pygame
import playsound as playsound
import os
from  tkinter import filedialog

window = Tk()
window.title("MusicPlayer")
window.geometry("800x500")
pygame.mixer.init()

# Labels
track_frame = LabelFrame(window, text="SONG TRACK", font=("Helvetica", 15, "bold"), bg="Navyblue", fg="white", bd=5, relief=GROOVE)
track_frame.place(x=0, y=0, width=600, height=100)

control_panel = LabelFrame(window, text="CONTROL PANEL", font=("Helvetica", 15, "bold"), bg="green", fg="white", bd=5, relief=GROOVE)
control_panel.place(x=0, y=100, width=700, height=100)

songs_frame = LabelFrame(window, text="SONG PLAYLIST", font=("Helvetica", 15, "bold"), bg="yellow", fg="white", bd=5, relief=GROOVE)
songs_frame.place(x=600, y=0, width=400, height=200)

# Listbox for playlist.
scroller = Scrollbar(songs_frame, orient=VERTICAL)
playlist = Listbox(songs_frame, yscrollcommand=scroller.set, selectbackground="brown", selectmode=SINGLE, font=("Helvetica", 12, "bold"), bg="silver", fg="white", bd=5, relief=GROOVE)
scroller.pack(side=RIGHT, fill=Y)
scroller.config(command=playlist.yview)
playlist.pack(fill=BOTH)

# Defining and creating the buttons

pygame.mixer.init()
#song = pygame.mixer.music.load('songs/Lonely-Girl-from-Kat-and-the-Kings.ogg')

def play_song():
    playlist.get(ACTIVE)
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

play_button = Button(control_panel, text="PLAYSONG", command=play_song, width=10, height=1, font=("Helvetica", 16, "bold"), fg="pink", bg="Navyblue")
play_button.grid(row=0, column=0, padx=10, pady=5)

def pause_song():
    set("-Stopped")
    pygame.mixer.music.stop()

pause_button = Button(control_panel, text="PAUSE", command=pause_song, width=10, height=1, font=("Helvetica", 16, "bold"), fg="pink", bg="Navyblue")
pause_button.grid(row=0, column=3, padx=10, pady=5)


def unpause_song():
    set("-Playing")
    pygame.mixer.music.unpause()

unpause_button = Button(control_panel, text="UNPAUSESONG", command=unpause_song, width=12, height=1, font=("Helvetica", 16, "bold"), fg="pink", bg="Navyblue")
unpause_button.grid(row=0, column=2, padx=10, pady=5)

def stop_song():
    set("-Stopped")
    pygame.mixer.music.stop()

stop_button = Button(control_panel, text="STOPSONG", command=stop_song, width=10, height=1, font=("Helvetica", 16, "bold"), fg="pink", bg="Navyblue")
stop_button.grid(row=0, column=4, padx=10, pady=5)



os.path.exists('songs')
os.chdir('songs')
song_tracks = os.listdir()

for track in song_tracks:
    playlist.insert(END, track)








window.mainloop()
