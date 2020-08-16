import os
from tkinter.filedialog import askdirectory
import pandas as pd

import random
import pygame
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
from tkinter import *

root = Tk()
root.minsize(300,300)

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

dislike = 0
weight = [1,0,0]
position = 0
myindex = [0,1,2,3,4,5,6,7,8,9,10,11]  #11 songs were there in the file
currentsong = random.choice(myindex)
ind = 0
df = pd.DataFrame({},index=[0],columns=['title','album','artist','genre'])
#df = pd.DataFrame({'title':'Senorita','album':'Zindagi Na Milegi Dobara (2011)','artist':'Farhan Akhtar','genre':'Party'},currentsong=[ind])
#ind+=1

def directorychooser():

    directory = askdirectory()
    os.chdir('E:\MUSIC PROJECT')     #Music files stored in the folder - MUSIC PROJECT

    for files in os.listdir('E:\MUSIC PROJECT'):
        if files.endswith(".mp3"):
            global df
            global ind
            realdir = os.path.realpath(files)
            audio = EasyID3(realdir)
            aud = ID3(realdir)
            realnames.append(audio['title'])
            #new_row = pd.DataFrame({'title':"audio['title']",'album':"audio['album]",'artist':"audio['artist']",'genre':"audio['genre']"},currentsong=[ind])
            # simply concatenate both dataframes

            df.loc[ind,'title'] = audio['title']
            df.loc[ind,'album'] = audio['album']
            df.loc[ind,'artist'] = audio['artist']
            df.loc[ind, 'genre'] = audio['genre']
            ind+=1
            #df = pd.concat([new_row, df]).reset_currentsong(drop = True)

            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

def same(w,i):
    global currentsong
    if(w==0):
        if df.loc[i,'genre']==df.loc[currentsong,'genre']:
            return 1
        return 0
    elif (w == 1):
        if df.loc[i, 'artist'] == df.loc[currentsong, 'artist']:
            return 1
        return 0
    elif (w == 2):
        if df.loc[i, 'album'] == df.loc[currentsong, 'album']:
            return 1
        return 0

def mood():
    global myindex
    global currentsong
    global weight
    global dislike
    global position
    for i in range(10):
        i  = random.choice(myindex)
        if same(0,i) == 0:
            currentsong = i
    weight = [1,0,0]
    position = 0
    dislike = 0
    print("mood changed")



def updatepos():
    global position
    global weight
    position = (position + 1)%3
    weight[position] = weight[position] + 1
    print("position updated ",weight)

def bestsong():
    global currentsong
    global weight
    global dislike
    max = 0
    max_index = 0

    if(dislike>2):
        mood()

    for i in range(12):
        target = 0
        curr = (currentsong + i)%12
        for j in range(3):
            target = target + (weight[j]*same(j,curr))
        if(target>max and curr!=currentsong):
            max = target
            max_index = curr
    return max_index

def updatelabel():
    global currentsong
    #global songname
    v.set(realnames[currentsong])
    return realnames[currentsong]

def dlike(event):
    global dislike
    updatepos()
    dislike = dislike + 1
    print("disliked",dislike)
    next(event)


def like(event):
    global weight
    global dislike
    global position
    weight[position] = weight[position]+5
    dislike = 0
    print("liked ",position)
    print(weight)

def previous(event):
    global currentsong
    currentsong -= 1
    pygame.mixer.music.load(listofsongs[currentsong])
    pygame.mixer.music.play()
    updatelabel()

def next(event):
    global currentsong
    global dislike
    currentsong = bestsong()
    #dislike = dislike + 1
    pygame.mixer.music.load(listofsongs[currentsong])
    pygame.mixer.music.play()
    updatelabel()
    print(df)

def stopsong(event):
    global currentsong
    pygame.mixer.music.stop()
    v.set("")
    return realnames[currentsong]

label = Label(root,text="Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()

realnames.reverse()

for items in listofsongs:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()

likebutton = Button(root,text = 'Like')
likebutton.pack()

dislikebutton = Button(root,text = 'Dislike')
dislikebutton.pack()

nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text = 'Stop Music')
stopbutton.pack()

likebutton.bind("<Button-1>",like)
dislikebutton.bind("<Button-1>",dlike)
nextbutton.bind("<Button-1>",next)
previousbutton.bind("<Button-1>",previous)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
directorychooser()
root.mainloop()
