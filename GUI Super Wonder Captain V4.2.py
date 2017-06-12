#     GUI Super Wonder Captain.py
#
import io                               # Provides to use IO
import datetime						    # Provides datetime access.
import hashlib                          # Provides to use hash codes
import json                             # Provides to use json
import os           					# Provides miscellaneous operating system interfaces.
import pickle       					# Provides serializing and de-serializing of Python object structures.
import random							# Provides function random for random numbers
import requests                         # Provides to make requests
import time         					# Provides time access and conversions.
import threading						# Provides to use threads

totalscore = 0
wordcount = 0
remaningpoints = 25
hintsleft = True
addpoints = True

from tkinter import *           		# Tkinter GUI for Python 3.X
from tkinter import messagebox		    # Tkinter messagebox
from PIL import Image, ImageTk  		# Allows for image formats other than gif
from urllib.request import urlopen	    # Allows to use url

def getHighScore():
    try:
        file = open("scores.txt", "r")
        names = []
        scores = []
        highscores = ""
        for line in file:
            currentline = line.split(",")
            name = currentline[0].replace("\n", "").split("\n")
            names.append(name)
            score = currentline[1].replace("\n", "").split("\n")
            scores.append(score)
        for n, s in zip(names, scores):
            highscores += "\n" + "".join(n) + ": " + "".join(s)
        return highscores
    except:
        return ""

def getTodaysHighScore():
    try:
        name = ""
        highscore = 0
        file = open("scores.txt", "r")
        for line in file:
            line = line.split(",")
            times = line[2].replace("\n", "").split("\n") #stores the times of the scores in scores.txt
        file.close()
        file = open("scores.txt", "r")
        for line in file:
            if str(datetime.date.today()) in line: #checks for each date if it matches today's date
                line = line.split(",")
                scores = line[1].replace("\n", "").split("\n")  #stores today's scores
                for score in scores:
                    if int(score) > highscore:
                        highscore = int(score) #assigns the highest score to highscore variable
        file.close()
        file = open("scores.txt", "r")
        for line in file:
            if str(highscore) in line: #matches the highscore to the line in which it occurs
                line = line.split(",")
                name = line[0].replace("\n", "").split("\n") #stores the name of the scores in scores.txt
        return "".join(name) + ": " + str(highscore)
    except:
        return ""

def sendScoreToFile():
    global totalscore
    if totalscore < 0: #if totalscore is smaller than 0, there are no points to be scored anymore
        totalscore = 0
    file = open("scores.txt", "a") #open scores.txt in append mode
    output = nameVar.get() + "," + str(totalscore) + "," + str(datetime.date.today())
    file.write(output + "\n") #writes to scores.txt the name of player, the score and today's date
    file.close()

def correctAnswer():
    global totalscore
    global remaningpoints

    totalscore += 25 #correct answer

    remaningpoints = 0
    Scores(root)

def falseAnswer():
    global totalscore
    global remaningpoints

    totalscore -= 1 #wrong answer

    if remaningpoints < 1:
        remaningpoints = 0
    else:
        remaningpoints -= 1
    Scores(root)

def giveHint():
    global totalscore
    global remaningpoints

    totalscore -= 3 #hint

    if remaningpoints < 3: #ensures that the remaning points does not go lower than 0
        remaningpoints = 0
    elif hintsleft:
        remaningpoints -= 3
    Scores(root)

def play():
    global hintsleft
    hintsleft = True
    if nameVar.get() == "":
        messagebox.showerror("Error", "Please enter a name and press play!")
    else:
        global wordcount, randomcharacters, remaningpoints
        hintsleft = True
        wordcount = 0
        randomcharacters = getrndchars(getcharlist())
        Characters(root)
        Description(root)
        remaningpoints = 25
        Scores(root)

def hint():
    giveHint()
    Description(root)

def giveUP():
    global remaningpoints
    remaningpoints = 0
    messagebox.showwarning("Warning", "Nope!!")
    Scores(root)

def charButtons(i):
    global addpoints
    global totalscore
    global remaningpoints
    if i == 0:
        if nameofchartoguess == randomcharacters[0][0]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 1:
        if nameofchartoguess == randomcharacters[0][1]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 2:
        if nameofchartoguess == randomcharacters[0][2]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 3:
        if nameofchartoguess == randomcharacters[0][3]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 4:
        if nameofchartoguess == randomcharacters[0][4]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 5:
        if nameofchartoguess == randomcharacters[0][5]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 6:
        if nameofchartoguess == randomcharacters[0][6]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 7:
        if nameofchartoguess == randomcharacters[0][7]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 8:
        if nameofchartoguess == randomcharacters[0][8]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()
    elif i == 9:
        if nameofchartoguess == randomcharacters[0][9]:
            addpoints = False
            messagebox.showinfo("Correct!", "Congratulations!!!")
            correctAnswer()
            sendScoreToFile()
            totalscore = 0
            play()
        else:
            falseAnswer()

def exit():
    #   Put here everything you want to close by exit
    root.destroy()

def info():
    messagebox.showinfo("Made by", "Game developed by Azzeddine, Abdel, Glenn, Kamal, Laurens & Sem")

def rules():
    messagebox.showinfo("Rules...", "You start with 25 points\n"
                                    "If you press the wrong character button you lose 1 point\n"
                                    "If you press the hint button you lose 3 points\n"
                                    "If you press the giveup button you lose all points\n"
                                    "Have fun playing this game!")

class Initialize:

    def __init__(self, master):
        master.resizable(0, 0)
        master.title("Super Wonder Captain")
        master.wm_iconbitmap('Marvel.ico')

        global background_image
        background_image = PhotoImage(file="Background.png")
        background_label = Label(master, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        global w, h
        w = background_image.width()
        h = background_image.height()
        master.geometry('%dx%d+0+0' % (w, h))

        menubar = Menu(master)
        master.config(menu=menubar)

        gameMenu = Menu(menubar)
        menubar.add_cascade(label="Game...", menu=gameMenu)
        gameMenu.add_command(label="Play!!", command=play)
        gameMenu.add_separator()
        gameMenu.add_command(label="Exit", command=exit)

        helpMemu = Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpMemu)
        helpMemu.add_command(label="Rules", command=rules)
        helpMemu.add_command(label="Info", command=info)

        statusBarFrame = Frame(master)
        statusBarFrame.pack(side=BOTTOM, fill=X)

        self.statusBar = Label(statusBarFrame, text="Data provided by Marvel. © 2014 Marvel", bd=1, relief=SUNKEN)
        self.statusBar.pack(side=LEFT, fill=X)

        global progress
        progress = StringVar()

        self.status = Label(statusBarFrame, textvariable=progress, bd=1, relief=SUNKEN)
        self.status.pack(side=RIGHT, fill=X)

class User:

    def __init__(self, master):
        # frame specs
        userFrame = Frame(master)
        #userFrame.pack(anchor=NW)
        userFrame.place(x=5, y=10)

        # label name for entry field
        self.label = Label(userFrame, text="Name")
        self.label.grid(row=0, column=0, sticky=E)

        global nameVar
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
        #global playButton, exitButton

        self.playButton = Button(buttonFrame1, text='Play', command=play, height=2, width=10)
        self.playButton.grid(row=0, column=0, sticky=W)
        #self.playButton.config(state=DISABLED)

        self.exitButton = Button(buttonFrame1, text='Exit', command=exit, height=2, width=10)
        self.exitButton.grid(row=0, column=1, padx=5, sticky=E)
        #self.exitButton.config(state=DISABLED)

class Scores:

    def __init__(self, master):
        scoreFrame = Frame(master)       # select of names
        #scoreFrame.pack(anchor=NE)
        scoreFrame.place(x=w, y=0, anchor=NE)

        labelFrame = Frame(master)
        labelFrame.place(x=w-130, y=0, anchor=NE)

        labelHS = Label(labelFrame, text="  Highscores: ", font=("Helvetica", 10))
        labelHS.grid(row=0, column=2, sticky=E)

        scroll = Scrollbar(scoreFrame, orient=VERTICAL)
        text = Text(scoreFrame, height=10, width=15, font=("Helvetica", 10))
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT,  fill=BOTH, expand=1)
        text.insert(END, getHighScore())
        text.configure(state=DISABLED)

        labelTS = Label(labelFrame, text="Today highscore: ", font=("Helvetica", 10))
        labelTS.grid(row=0, column=0, sticky=E)

        textTS = Text(labelFrame, height=1, width=15, font=("Helvetica", 10))
        textTS.grid(row=0, column=1, sticky=E)
        textTS.insert(END, getTodaysHighScore())
        textTS.configure(state=DISABLED)

        labelRP = Label(labelFrame, text="Remaining points: ", font=("Helvetica", 10))
        labelRP.grid(row=1, column=0, sticky=E)

        textRP = Text(labelFrame, height=1, width=15, font=("Helvetica", 10))
        textRP.grid(row=1, column=1, sticky=E)
        textRP.insert(END, remaningpoints)
        textRP.configure(state=DISABLED)

class Description:

    def __init__(self, master):
        # frame specs
        QuestionFrame = Frame(master)
        QuestionFrame.place(x=w/2, y=(200), anchor=S)

        DiscriptionFrame = Frame(master)
        DiscriptionFrame.place(x=w/2, y=(h/2-20), anchor=S)

        Question = Label(QuestionFrame, text="Choose a character by this description", font=("Helvetica", 16))
        Question.grid(row=0, column=0)

        Appels = givehint(randomcharacters)

        scroll = Scrollbar(DiscriptionFrame, orient=VERTICAL)
        text = Text(DiscriptionFrame, height=5, width=80, font=("Helvetica", 12))
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT,  fill=BOTH, expand=1)

        if Appels != "ok" and Appels != "":
            text.insert(END, Appels[1])
        text.configure(state=DISABLED)

class Characters:

    def __init__(self, master):
        characterFrame = Frame(master)
        characterFrame.place(x=(w/2), y=h/2, anchor=N)
        global image
        image = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        for i in image:
            image[i] = self.loadPic(getcharlist().get(randomcharacters[0][i])[1])
            self.label = Label(characterFrame, text=randomcharacters[0][i][:15])
            self.label.grid(row=0, column=i)
            self.character = Button(characterFrame, image=image[i], command=lambda i=i: charButtons(i))
            self.character.grid(row=1, column=i)

        buttonFrame = Frame(master)
        buttonFrame.place(x=w/2, y=h-100, anchor=S)

        self.hintButton = Button(buttonFrame, text='Hint!', command=hint, height=3, width=15)
        self.hintButton.grid(row=0, column=0, sticky=W)

        self.giveUpButton = Button(buttonFrame, text='Give up!', command=giveUP, height=3, width=15)
        self.giveUpButton.grid(row=0, column=1, sticky=E)

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

def loadScreen(x):
    if x > 100:
        progress.set("Building completed! {} characters loaded".format(str(x)))
        #playButton.config(state=NORMAL)
        #exitButton.config(state=NORMAL)
    else:
        progress.set("Building character-list; 100 needed: {}".format(str(x)))

# This function will check if there is a up-to-date file with all the character data.
# If there isn't one, this function will create and or update the file.
def getcharlist():
    # Try to get the file modified date. If it's equal to the system date, open the file and return it's content.
    # If it's not, or the file doesn't exist, create or update it. Then open it and return it's content.
    try:
        if str(datetime.datetime.fromtimestamp(os.path.getmtime('characters.pck'))).split()[0] == time.strftime("%Y-%m-%d"):
            build = False
        else:
            build = True
    except OSError:
        build = True

    if build:
        characterlist = {}  # Will hold the information of 100+ characters.
        offset = 0  # Will be used to get the next set of 100 characters.

        # Connection information.
        baseurl = "http://gateway.marvel.com:80/v1/public/characters"
        private_key = "ac844ec2eeadb045d5a099248aaad6b0ba944448"
        public_key = "01e99d019cdb13d44f3ec962cd0b04ad"

        # Keep asking for 100 more until we have a list of 100+ characters that meets our criteria.
        while len(characterlist) < 100:
            # Build the connection URL.
            timestamp = str(time.time())
            hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
            md5digest = str(hash.hexdigest())
            connection_url = baseurl + "?ts=" + timestamp + "&limit=100&offset=" + str(offset) + "&apikey=" + public_key + "&hash=" + md5digest
            # Get the information
            response = requests.get(connection_url)
            jsontext = json.loads(response.text)

            # Stop if we get an empty list of characters
            if len(jsontext['data']['results']) == 0:
                break

            # Add 100 to the offset so we'll get the next 100 characters next time instead of the same ones.
            offset += 100

            # Read all the 100 characters we gor from the response.
            # If one meets our criteria, we can harvest the information we need and add this character to our list.
            for item in jsontext['data']['results']:
                        if len(item['description']) > 25 and item['thumbnail']['path'][-19:] != "image_not_available":
                            characterlist[item['name']] = [item['description'], item['thumbnail']['path'] + "." + item['thumbnail']['extension']]

            loadScreen(len(characterlist))  # Indication of how manny characters we already have.

        # Open/create the file 'characters.pck' and store our characterlist.
        with open('characters.pck', 'wb') as picklefile:
            pickle.dump(characterlist, picklefile)

        # Return the characterlist so other functions can use it.
        return characterlist

    else:
        # Read the file 'characters.pck' and read it's content.
        with open('characters.pck', 'rb') as picklefile:
            characterlist = pickle.load(picklefile)

        loadScreen(len(characterlist))  # Indication of how manny characters we have.

        # Return the characterlist so other functions can use it.
        return characterlist

# This function will get ten random character names from the masterlist.
# Then it wil pick a random character of those 10 characters and get the description of it.
# The description of this character wil then be altered so the name of the character won't be in the hints.
def getrndchars(characterlist):
    rndnames = []   # Will hold ten random character names.
    chartoguess = []    # Will hold the character data of the character that has to be guessed.
    texttoremove = []   # Will hold the names of the character that has to be guessed.

    # Pick a random character from the masterlist until we have ten.
    while len(rndnames) < 10:
        name = random.choice(list(characterlist.keys()))
        # Be sure the random name we picked is not already in the list. Add it if it isn't.
        if name not in rndnames:
            rndnames.append(name)

    # Pick a random name from the list with ten names we just build and add it to a list.
    global nameofchartoguess
    nameofchartoguess = random.choice(rndnames)
    chartoguess.append(nameofchartoguess)

    # Get all the details we need of the character from the masterlist and add this to the list.
    chartoguess.append(characterlist.get(nameofchartoguess))

    # Split the name of the character.
    texttoremove = str.split(nameofchartoguess)

    # Replace all the occurrences of the characters names in the description with '...'
    for key in texttoremove:
        chartoguess[1][0] = chartoguess[1][0].replace(key, '...')

    # Split the characters description.
    chartoguess[1][0] = str.split(chartoguess[1][0])

    # Return the ten random names and the character that has to be guessed.
    return rndnames, chartoguess

# This function will return a part of the description of the character that has to be guessed.
def givehint(chartoguess):
    global wordcount
    wordcount += 10  # Will hold the amount of words there are already given.

    # Return ten words from the description if there are still words lef
    if wordcount < (len(chartoguess[1][1][0]) + 10):
        hint = "{0}".format(" ".join(str(i) for i in chartoguess[1][1][0][:wordcount]))
        return 'Here is your hint: ', hint
    else:
        global hintsleft
        hintsleft = False
        return messagebox.showinfo("Sorry", "Sorry out of hints!"), chartoguess[1][1][0]

def main():
    global root
    root = Tk()
    Initialize(root)
    User(root)
    Buttons(root)
    threading.Thread(target=getcharlist).start()
    root.mainloop()

if __name__ == "__main__":
    main()
