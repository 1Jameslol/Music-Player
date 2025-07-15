from tkinter import filedialog
class Logic:
    #filepath
    filepath = ""

    #soundControl
    sound = None

    def __init__(self, sound):
        self.sound=sound

    #recursive algorithm to remove slashes
    def removeSlash(self, filepath):
        try:
            if(filepath.index("/")<-1):
                print("")
            else:
                filepath = filepath[filepath.index("/")+1:len(filepath)]
                self.removeSlash(filepath)
        except:
            print("parsed")
            self.setFilePath(filepath)

    #returns filepath
    def getFilePath(self):
        return self.filepath
    
    #sets filepath
    def setFilePath(self, filepath):
        self.filepath=filepath

    #functions to select file logic
    def selectFile(self):
        print("selectFile")
        try:
            self.removeSlash(filedialog.askopenfilename())
            print("file selected (" + self.getFilePath()+")")
            try:
                self.sound.load(self.getFilePath())
                print("file loaded (" + self.getFilePath()+")")
            except:
                self.sound.load(self.getFilePath())
                print("file failed to load")
        except:
            print("file not read properly")

