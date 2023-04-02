import os
import pygame
from tkinter import *
from pygame import mixer


root = Tk()


listofsongs = []
v = StringVar()


index = 0
def pausesong():
        v.set("Paused")
        mixer.music.pause()
def stopsong():
        v.set("Stopped")
        mixer.music.stop()
def resumesong():
        v.set("Resuming")
        mixer.music.unpause()    
def nextsong():
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def playsong():
        listofsongs[index]=playlist.get(ACTIVE)
        print(listofsongs[index])
        mixer.music.load(listofsongs[index])
        v.set("Playing")
        mixer.music.play()
        updatelabel()
 
def updatelabel():
    global index
    global songname
    v.set(listofsongs[index]) 
#playlist---------------
playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="yellow",font=('arial',15),width=40)
playlist.grid(columnspan=5)
directory = 'F:\working songs'
os.chdir(directory)
for files in os.listdir(directory):
	if files.endswith(".mp3"):
		listofsongs.append(files)
		print(files)

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	pygame.mixer.music.play()


listofsongs.reverse()

for items in listofsongs:
    playlist.insert(0,items)

listofsongs.reverse()

playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',20),bg="yellow",fg="black",padx=7,pady=7)
playbtn.grid(row=1,column=0)
pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',20),bg="yellow",fg="black",padx=7,pady=7)
pausebtn.grid(row=1,column=1)
stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',20),bg="yellow",fg="black",padx=7,pady=7)
stopbtn.grid(row=1,column=2)
Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',20),bg="yellow",fg="black",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)
nextbtn = Button(root,text="Next",command=nextsong)
nextbtn.config(font=('arial',20),bg="yellow",fg="black",padx=7,pady=7)
nextbtn.grid(row=1,column=4)


mainloop()
