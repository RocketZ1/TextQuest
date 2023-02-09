class ScriptParser:
    def __init__(self, background_image="images/Phase2 Dorms"):
        self.background_image = background_image
        self.audio = None
        self.text = []
        self.current_line = 0
        self.imagePath = {
            1: None
        }
        self.imageCords = {
            1: None
        }
        self.imageScale = {
            1: None
        }

    def addText(self, text):
        self.text.append(text)

    def getLineCount(self):
        return len(self.text)

    def getLine(self, line=None):
        if line is None:
            line = self.current_line
        self.current_line += 1
        if self.current_line > len(self.text):
            return "Null"
        else:
            return self.text[line]

    def getCurrentLine(self):
        if self.current_line < 0:
            return 0
        else:
            return self.current_line

    def setBackgroundImage(self, background_image):
        self.background_image = background_image

    def getBackgroundImage(self):
        return self.background_image

    def setAudio(self, audio):
        self.audio = audio

    def getAudio(self):
        return self.audio

    def addImage(self, imagePath, onClick, cords=(0, 0), scale=(640, 360)):
        print(onClick)
        self.imagePath[onClick] = imagePath
        self.imageCords[onClick] = cords
        self.imageScale[onClick] = scale

    def getImagePath(self, onClick):
        if onClick in self.imagePath.keys():
            return self.imagePath[onClick]
        else:
            return None

    def getImageCords(self, onClick):
        return self.imageCords[onClick]

    def getImageScale(self, onClick):
        return self.imageScale[onClick]

    def getLargestOnClick(self):
        return max(self.imagePath.keys())

