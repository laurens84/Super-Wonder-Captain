#     GUI Super Wonder Captain.py
#
import io
import datetime
import hashlib
import json
import os           # Provides micellaneous operating system interfaces.
import pickle       # Provides serializing and de-serializing of Python object structures.
import random
import requests
import time         # Provides time access and conversions.

wordcount = 0

from tkinter import *           # Tkinter GUI for Python 3.X
from PIL import Image, ImageTk  # allows for image formats other than gif
from urllib.request import urlopen

def play():
    global wordcount
    wordcount = 0
    global randomcharacters
    randomcharacters = getrndchars(getcharlist())
    Characters(root)

def hint():
    print(givehint(randomcharacters))

def giveUP():
    print("Nope!!")

class Initialize:

    def __init__(self, master):
        master.resizable(0, 0)
        master.title("Super Wonder Captain")

        global background_image
        background_image = PhotoImage(file="Background.png")
        background_label = Label(master, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        global w, h
        w = background_image.width()
        h = background_image.height()
        master.geometry('%dx%d+0+0' % (w, h))

        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="Game...", menu=subMenu)
        subMenu.add_command(label="Play!!", command=play)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=master.destroy)

        self.statusBar = Label(master, text="Data provided by Marvel. © 2014 Marvel", bd=1, relief=SUNKEN, anchor=S)
        self.statusBar.pack(side=BOTTOM, fill=X)

class User:

    def __init__(self, master):
        # frame specs
        userFrame = Frame(master)
        #userFrame.pack(anchor=NW)
        userFrame.place(x=5, y=10)

        # label name for entry field
        self.label = Label(userFrame, text="Name")
        self.label.grid(row=0, column=0, sticky=E)

        nameVar = StringVar()   # String variable

        # Entry field
        self.name = Entry(userFrame, textvariable=nameVar)
        self.name.grid(row=0, column=1)

class Buttons:

    def __init__(self, master):
        # frame specs
        buttonFrame1 = Frame(master)
        buttonFrame1.place(x=5, y=35)
        # Buttons
        self.playButton = Button(buttonFrame1, text='Play', command=play, height=2, width=10)
        self.playButton.grid(row=0, column=0, sticky=W)

        self.exitButton = Button(buttonFrame1, text='Exit', command=master.destroy, height=2, width=10)
        self.exitButton.grid(row=0, column=1, padx=5, sticky=E)

        buttonFrame2 = Frame(master)
        buttonFrame2.place(x=w/2, y=h-100, anchor=S)

        self.hintButton = Button(buttonFrame2, text='Hint!', command=hint, height=3, width=15)
        self.hintButton.grid(row=0, column=0, sticky=W)

        self.giveUpButton = Button(buttonFrame2, text='Give up!', command=giveUP, height=3, width=15)
        self.giveUpButton.grid(row=0, column=1, sticky=E)

class Scores:

    def __init__(self, master):

        scoreFrame = Frame(master)       # select of names
        scoreFrame.pack(anchor=NE)
        #scoreFrame.place(x=w-175, y=20)

        scroll = Scrollbar(scoreFrame, orient=VERTICAL)
        select = Listbox(scoreFrame, yscrollcommand=scroll.set, height=10)
        scroll.config(command=select.yview)
        scroll.pack(side=RIGHT, fill=Y)
        select.pack(side=LEFT,  fill=BOTH, expand=1)

class Question:

    def __init__(self, master):
        # frame specs
        questionFrame = Frame(master)
        questionFrame.place(x=w/2, y=(h/2-100), anchor=N)

        # label name for entry field
        self.question = Label(questionFrame, text="Questionn??", font=("Helvetica", 20))
        self.question.grid(row=0, column=0)

class Characters:

    def __init__(self, master):
        characterFrame = Frame(master)
        characterFrame.place(x=(w/2), y=h/2, anchor=N)
        global image

        #characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #for character in characters:

        image = self.loadPic(getcharlist().get(randomcharacters[0][0])[1])
        name = randomcharacters[0][0][:15]
        #print(randomcharacters[0][0])

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=0)
        self.character1 = Button(characterFrame, image=image)
        self.character1.grid(row=1, column=0)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=1)
        self.character2 = Button(characterFrame, image=image)
        self.character2.grid(row=1, column=1)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=2)
        self.character3 = Button(characterFrame, image=image)
        self.character3.grid(row=1, column=2)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=3)
        self.character4 = Button(characterFrame, image=image)
        self.character4.grid(row=1, column=3)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=4)
        self.character5 = Button(characterFrame, image=image)
        self.character5.grid(row=1, column=4)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=5)
        self.character6 = Button(characterFrame, image=image)
        self.character6.grid(row=1, column=5)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=6)
        self.character7 = Button(characterFrame, image=image)
        self.character7.grid(row=1, column=6)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=7)
        self.character8 = Button(characterFrame, image=image)
        self.character8.grid(row=1, column=7)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=8)
        self.character9 = Button(characterFrame, image=image)
        self.character9.grid(row=1, column=8)

        self.label = Label(characterFrame, text=name)
        self.label.grid(row=0, column=9)
        self.character10 = Button(characterFrame, image=image)
        self.character10.grid(row=1, column=9)

    def loadPic(self, url):
        image_bytes = urlopen(url).read()
        # internal data file
        data_stream = io.BytesIO(image_bytes)
        # open as a PIL image object
        pil_image = Image.open(data_stream)
        # convert PIL image object to Tkinter PhotoImage object
        pil_image = pil_image.resize((100, 100), Image.ANTIALIAS)
        # Resize to (250, 250) is (height, width)
        return ImageTk.PhotoImage(pil_image)

def getcharlist():
    try:
        if str(datetime.datetime.fromtimestamp(os.path.getmtime('characters.pck'))).split()[0] == time.strftime("%Y-%m-%d"):
            build = False
        else:
            build = True
    except OSError:
        build = True

    if build:
        baseurl = "http://gateway.marvel.com:80/v1/public/characters"
        characterlist = {}
        offset = 0
        private_key = "ac844ec2eeadb045d5a099248aaad6b0ba944448"
        public_key = "01e99d019cdb13d44f3ec962cd0b04ad"

        while len(characterlist) < 100:
            timestamp = str(time.time())
            hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
            md5digest = str(hash.hexdigest())
            connection_url = baseurl + "?ts=" + timestamp + "&limit=100&offset=" + str(offset) + "&apikey=" + public_key + "&hash=" + md5digest
            response = requests.get(connection_url)
            jsontext = json.loads(response.text)
            if len(jsontext['data']['results']) == 0:
                break
            offset += 100

            for item in jsontext['data']['results']:
                        if len(item['description']) > 25 and item['thumbnail']['path'][-19:] != "image_not_available":
                            characterlist[item['name']] = [item['description'], item['thumbnail']['path'] + "." + item['thumbnail']['extension']]
            print(len(characterlist))

        with open('characters.pck', 'wb') as picklefile:
            pickle.dump(characterlist, picklefile)

        return characterlist

    else:
        with open('characters.pck', 'rb') as picklefile:
            characterlist = pickle.load(picklefile)

        return characterlist

def getrndchars(characterlist):
    rndnames = []
    chartoguess = []
    while len(rndnames) < 10:
        name = random.choice(list(characterlist.keys()))
        if name not in rndnames:
            rndnames.append(name)

    nameofchartoguess = random.choice(rndnames)
    chartoguess.append(nameofchartoguess)
    chartoguess.append(characterlist.get(nameofchartoguess))
    chartoguess[1][0] = str.split(chartoguess[1][0])
    chartoguess[1][0] = [w.replace(nameofchartoguess, '...') for w in chartoguess[1][0]]

    print(nameofchartoguess)
    print(chartoguess[1][1])

    return rndnames, chartoguess

def givehint(chartoguess):
    global wordcount
    wordcount += 10

    if wordcount < (len(chartoguess[1][1][0]) + 10):
        hint = "[{0}]".format(" ".join(str(i) for i in chartoguess[1][1][0][:wordcount]))
        return hint
    else:
        return 'Sorry, out of hints'

#a = getrndchars(getcharlist())

#givehint(a)
#print(a)
#print(getcharlist().get('Hulk')[2])
#print("[{0}]".format(" ".join(str(i) for i in a[1][1][1][:20])))


def main():
    global root
    getcharlist()
    root = Tk()
    Initialize(root)
    User(root)
    Buttons(root)
    Scores(root)
    Question(root)
    root.mainloop()

if __name__ == "__main__":
    main()


