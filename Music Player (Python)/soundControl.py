from tkinter import *
import pygame
import random
class SoundControl:
    pygame.mixer.init()

    #controls instance
    controls = None

    #ArrayOfQueue
    queueList = []
    
    #used to store the filepath for queue
    filepathStore = None       
    
    #initControls
    def controls(self, controls):
        self.controls=controls

    #basic sound Controls
    def queue(self):
        if(self.filepathStore==None):
            print("nothing to queue")
            print("***********")
            print(self.queueList)
            print("***********")
        else:
            self.controls.checkDupes(self.queueList, self.filepathStore)
        self.controls.displayQueue()
        
    def play(self):
        print("play2")
        pygame.mixer.music.play()
        if(len(self.queueList)>1):
            self.controls.displaySong.config(text="Current Song: "+self.filepathStore)

    def stop(self):
        print("stop")
        pygame.mixer.music.stop()
        
    def load(self, filepath):
        print("loading....." + filepath)
        pygame.mixer.music.load(filepath)
        self.storeFilePath(filepath)

    #delets the to be played song and plays the next
    def playNext(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.queueList[0])
        del self.queueList[0]
        self.controls.queueLabelList[0].destroy()
        del self.controls.queueLabelList[0]
        self.resetLists()

        print("-----------")
        print(self.queueList)
        print("-----------")

        if(len(self.queueList)==1):
            self.controls.displaySong.config(text="Current Song: "+self.queueList[0])
        self.play()
        
    #destroys the gui of the queueLabelList and resets the queueLabelList
    def resetLists(self):
        for i, label in enumerate(self.controls.queueLabelList):
            label.destroy()
        self.controls.queueLabelList.clear()
        for i, unused in enumerate(self.queueList):
            label = label = Label(self.controls.root, text = self.queueList[i])
            self.controls.queueLabelList.append(label)
        self.controls.displayQueue()

    #shuffles the queueList and remaps the queueLabelList
    def shuffle(self):
        random.shuffle(self.queueList)
        self.resetLists()
        
    #stores the filepath
    def storeFilePath(self, filepathStore):
        self.filepathStore=filepathStore

    

