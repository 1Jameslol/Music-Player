from tkinter import *
from logic import Logic
from soundControl import SoundControl
class Controls:
    #soundControl
    sound = SoundControl()

    #programLogic
    logic = Logic(sound)

    #buttons
    selectFileBtn = None
    queueBtn = None
    playBtn = None
    stopBtn = None
    nextBtn = None
    shuffleBtn = None

    #labels
    displaySong = None
    queueLabel = None

    #queueLabelList
    queueLabelList = []

    #used for shifting buttons

    root = None
    xShifter = -275

    def __init__(self, root):
        #init buttons
        self.initButtons(root)

        #place Buttons and label
        self.selectFileBtn.place(x=380, y=285)
        self.queueBtn.place(x=500+self.xShifter, y=330)
        self.playBtn.place(x=600+self.xShifter, y=330)
        self.stopBtn.place(x=770+self.xShifter, y=330)
        self.nextBtn.place(x=685+self.xShifter, y=330)
        self.shuffleBtn.place(x=280, y=285)
        self.displaySong.place(x=350, y=250)
        self.queueLabel.place(x=373, y=385)

        #init controls instance from sound
        self.sound.controls(self)

        self.root=root


    #from the constructor
    def initButtons(self, root):
        #init Buttons
        self.selectFileBtn = Button(root, text="Select Audio File", command = self.logic.selectFile)
        self.queueBtn = Button(root, text="Queue", command = self.sound.queue)
        self.playBtn = Button(root, text="Play", command = self.sound.play)
        self.stopBtn = Button(root, text="Stop", command = self.sound.stop)
        self.nextBtn = Button(root, text="Next", command = self.sound.playNext)
        self.shuffleBtn = Button(root, text="Shuffle", command = self.sound.shuffle)
        self.displaySong = Label(root, text = "Current Song: ")
        self.queueLabel = Label(root, text = "Queue")


    #algorithm to check dupes in queueList
    def checkDupes(self, queueList, filepathStore):
        for i in queueList:
            if(i==filepathStore):
                print("duplicate deteted")
                print("***********")
                print(queueList)
                print("***********")
                return
            else:
                pass
        self.sound.queueList.append(self.sound.filepathStore)
        label = Label(self.root, text =  filepathStore )
        self.queueLabelList.append(label)
        
        self.sound.queue()
        print("-----------")
        print(self.sound.queueList)
        print("-----------")

    #displaying the queue
    def displayQueue(self):
        for i, label in enumerate(self.queueLabelList):
            label.place(x=373, y=415+i*30)