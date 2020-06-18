import pygame
import random
from termcolor import colored
from time import sleep

# pygame.init()

pygame.font.init()
pygame.mixer.init()

win = pygame.display.set_mode((1000, 700))
title = pygame.image.load("images/title.png")
workspace = pygame.image.load("images/workspace.png")
small_person = pygame.image.load("images/small-person.png")
small_person = pygame.transform.scale(small_person, (25,60))
pygame.display.set_caption("Papers Please Remake")
font = pygame.font.SysFont('Tahoma', 60, True, False)
#text = font.render('Bauhaus 93 | Size: 36 | Colour: White | Background: Blue', True, (255, 255, 255), (0, 0, 255))
pygame.mixer.music.load("musics/song.mp3")
pygame.mixer.music.play(-1)


run = True

def random_num(start: int, end: int, num: int):
    arr = []
    answer = ""
    for i in range(start, end+1):
        arr.append(i)
    for i in range(num):
        answer += str(random.choice(arr))
    return answer

class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, text):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        text = font.render(text, 1, (100, 100, 100))
        win.blit(text, (450, 600))

    def is_click(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


play_button = Button(450, 600, 130, 50, (255, 255, 255))
while run:
    # pygame.time.delay(100)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.is_click(pos):
                pygame.mixer.music.stop()
                run = False

    win.blit(title, (0,0))
    play_button.draw("Play")
    pygame.display.update()

play = True
day_count = 1
avail = True
display_next = False
iterator = 0

while play:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN and (pos[0] > 300 and pos[0] < 400) and (pos[1] > 100 and pos[1] < 200) and avail:
            print(colored(pygame.mouse.get_pos(), "red"))
            avail = False
            iterator = 0

    win.blit(workspace, (0,0))
    # win.blit(small_person, (0, 30))
    for i in range(8):
        win.blit(small_person, (0 + i*20 + int(random_num(1, 2, 1)) / 2, 30 + int(random_num(1, 2, 1)) / 2))

    win.blit(small_person, (150 + int(random_num(-3, 3, 1)) / 2, 60 + int(random_num(1, 2, 1)) / 2))

    for i in range(8):
        win.blit(small_person, (0 + i*20 + int(random_num(1, 2, 1)) / 2, 90 + int(random_num(1, 2, 1)) / 2))

    win.blit(small_person, (0 + int(random_num(-3, 3, 1)) / 2, 140 + int(random_num(1, 2, 1)) / 2))

    for i in range(13):
        win.blit(small_person, (0 + i*20 + int(random_num(1, 2, 1)) / 2, 140 + int(random_num(1, 2, 1)) / 2))

    if not avail and iterator < 30:
        text = font.render("NEXT!", 1, (100, 100, 100))
        win.blit(text, (450, 600))
        iterator+=1

    pygame.display.update()

pygame.quit()