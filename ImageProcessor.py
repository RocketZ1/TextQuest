import pygame

BLACK = (0, 0, 0)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
txtBox = pygame.image.load("images/textbox.png").convert_alpha()
txtBox = pygame.transform.scale(txtBox, (2000, 380))


class ImageProcessor:
    def __init__(self):
        self.setBackground()
        self.image = None

    def addText(self, text, lineNum=0):
        if lineNum == 0:
            screen.blit(txtBox, (-325, 450))

        font = pygame.font.SysFont(None, 24)
        img = font.render(text, True, BLACK)
        screen.blit(img, (200, 545 + (30 * lineNum)))

    def setBackground(self, filePath="images/coffee background.jpg"):
        background = pygame.image.load(filePath).convert()
        background = pygame.transform.scale(background, (1280, 720))
        screen.blit(background, (0, 0))

    def setImage(self, filePath, cords=(0, 0), scale=(640, 360)):
        self.image = pygame.image.load(filePath).convert()
        self.image = pygame.transform.scale(self.image, scale)
        screen.blit(self.image, cords)
