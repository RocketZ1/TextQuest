import pygame

from ImageProcessor import ImageProcessor
from ScriptParser import ScriptParser

imageProcessor = ImageProcessor()

scripts = []
currentScriptNum = 0
currentScript = None
clickCount = 0


def readScript():
    file = open("script.txt", "r")
    script = ScriptParser()
    for line in file:
        line = line.replace("\n", "")
        # the background img
        if line.startswith("#") or line == "" or line is None:
            continue
        elif line.startswith("img:"):
            filePath = line[4:]
            filePath = filePath[:filePath.index("%")]
            filePath = "images\\"+filePath
            onClick = line[(line.index("%onClick:")+9):]
            onClick = int(onClick[:onClick.index("%")])
            cords = line[(line.index("%coordinates:")+13):]
            xCord = int(cords[0:cords.index(",")])
            yCord = int(cords[cords.index(",")+1:cords.index("%")])
            scale = line[(line.index("%scale:")+7):]
            xScale = int(scale[0:scale.index(",")])
            yScale = int(scale[scale.index(",")+1:scale.index("%")])
            script.addImage(filePath, onClick, (xCord, yCord), (xScale, yScale))
        elif line.startswith("background:"):
            script.setBackgroundImage("images\\" + line[11:])
        elif line.startswith("audio:"):
            script.setAudio("audio\\" + line[6:])
            # If the script is done, go to the next
        elif line.startswith("%end%"):
            scripts.append(script)
            script = ScriptParser()
        else:
            script.addText(line)
    file.close()


def leftClick():
    global currentScript
    global currentScriptNum
    global clickCount
    clickCount += 1
    if currentScriptNum >= len(scripts):
        return
    currentScript = scripts[currentScriptNum]
    lineNum = currentScript.getCurrentLine()
    if lineNum == 0:
        imageProcessor.setBackground(currentScript.getBackgroundImage())
        if currentScript.getAudio() is not None:
            pygame.mixer.music.load(currentScript.getAudio())
            pygame.mixer.music.play()
    if lineNum >= 5 or lineNum >= currentScript.getLineCount():
        if clickCount >= currentScript.getLargestOnClick()+1:
            currentScriptNum += 1
            if currentScriptNum <= len(scripts) - 1:
                imageProcessor.setBackground(scripts[currentScriptNum].getBackgroundImage())
    else:
        imageProcessor.addText(currentScript.getLine(), lineNum)
    if currentScript.getImagePath(clickCount) is not None:
        imageProcessor.setImage(currentScript.getImagePath(clickCount),
                                currentScript.getImageCords(clickCount),
                                currentScript.getImageScale(clickCount))


def rightClick():
    print("You right clicked")


def main():
    readScript()

    pygame.init()
    mainLoop = True

    while mainLoop:
        for event in pygame.event.get():
            if currentScriptNum >= len(scripts):
                mainLoop = False

            if event.type == pygame.QUIT:
                mainLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                leftClick()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                rightClick()

        pygame.display.update()

    pygame.quit()


main()
