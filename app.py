import pygame
from pygame.locals import *
import random
from termcolor import colored
from time import sleep
from helpers import passport_img, convert_degrees_to_pygame

# pygame.init()

COUNTRIES = ["antegria", "arstotzka", "obristan", "impor", "kolechia", "republia", "united-federation"]

pygame.font.init()
pygame.mixer.init()
people_count = 0

alphas = "abcdefghijklm"
characters = {"m": [], "f": [], "s": []}
special_characters = []
for i in range(len("abcdefghijklm")):
    if "abcdefghijklm"[i] == "a":
        characters["f"].append(pygame.transform.scale(pygame.image.load(f"images/characters/{alphas[i]}.png"), (75, 90)))
    else:
        characters["m"].append(pygame.transform.scale(pygame.image.load(f"images/characters/{alphas[i]}.png"), (75, 90)))
characters["s"].append(pygame.image.load(f"images/characters/elisa.png"))
characters["s"].append(pygame.image.load(f"images/characters/ezic.png"))
characters["s"].append(pygame.image.load(f"images/characters/jorji.png"))

# print(characters)

win = pygame.display.set_mode((1000, 700))
title = pygame.image.load("images/title.png")
workspace = pygame.image.load("images/workspace.png")
small_person = pygame.image.load("images/small-person.png")
arstotaka_passport = pygame.image.load("images/passports/arstotzka.png")
small_person = pygame.transform.scale(small_person, (25,60))
pygame.display.set_caption("Papers Please Remake")
font = pygame.font.SysFont('Tahoma', 60, True, False)
font_a = pygame.font.Font("fonts/a.ttf", 10)
game_map = pygame.image.load("images/map.jpeg")
#text = font.render('Bauhaus 93 | Size: 36 | Colour: White | Background: Blue', True, (255, 255, 255), (0, 0, 255))
w_citation = pygame.image.load("images/warning-citation.png")
lw_citation = pygame.image.load("images/last-warning-citation.png")
p_citation = pygame.image.load("images/penalty-citation.png")

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

    def draw(self, text, font_type="font"):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if font_type == "font":
            text = font.render(text, 1, (100, 100, 100))
        elif font_type == "font_a":
            text = font_a.render(text, 1, (100, 100, 100))
        win.blit(text, (self.x, self.y))

    def is_click(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def move_person(x, y):
    pass

iterator = 0
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

    if iterator < 10:
        win.blit(title, (0,-10))
        iterator += 1
    elif iterator < 20:
        iterator += 1
        win.blit(title, (0,0))
    else:
        iterator = 0
    play_button.draw("Play")
    pygame.display.update()

play = True
day_count = 1
avail = True
display_next = False
iterator = 0

pass_button = Button(900, 450, 50, 50, (0, 255, 0))
denied_button = Button(900, 500, 50, 50, (255, 0, 0))

correct = None
char = None
current_country = None
a = 0

while play:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN and (pos[0] > 300 and pos[0] < 400) and (pos[1] > 100 and pos[1] < 200) and avail:
            char = None
            print(colored(pygame.mouse.get_pos(), "red"))
            avail = False
            iterator = 0
            people_count += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pass_button.is_click(pos):
                # do once approve button is clicked
                if correct != True:
                    win.blit(w_citation, (0, 0))
                avail = True
                iterator = 0
            elif denied_button.is_click(pos):
                # do once denied button is clicked
                if correct != False:
                    if a < 30:
                        print(a)
                        win.blit(w_citation, (0, 0))
                        a+=1
                avail = True
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

    # pygame.draw.circle(win, (98, 76, 39), (40, 650))
    if not avail:
        if char == None:
            gender = random.choice("mf")
            char = random.choice(characters[gender])

        if day_count == 1:

            if people_count == 4 or people_count > 5:
                if iterator == 0:
                    country = random.choice(COUNTRIES)
                    if country != "arstotzka":
                        correct = False
                    else:
                        correct = True
                    current_country = country
                    passport_img(country, sex=gender, exp=True) # True is valid, False otherwise
                    passport = pygame.image.load("output.png")

            if people_count == 1:
                if iterator == 0:
                    correct = True
                    current_country = "arstotzka"
                    passport_img(current_country, sex=gender, exp=True)
                    passport = pygame.image.load("output.png")

            if people_count == 2:
                if iterator == 0:
                    correct = False
                    current_country = "impor"
                    passport_img(current_country, sex=gender, exp=True)
                    passport = pygame.image.load("output.png")

            if people_count == 3:
                if iterator == 0:
                    correct = False
                    current_country = "republia"
                    passport_img(current_country, sex=gender, exp=True)
                    passport = pygame.image.load("output.png")

            if people_count == 5:
                if iterator == 0:
                    correct = False
                    text = font_a.render("Open this gate is stupid", 1, (100, 100, 100))
                    win.blit(text, (250, 250))
                    #passport_img("kolechia")
                    #passport = pygame.image.load("output.png")

            if people_count != 5:
                merged = passport.copy()
                if current_country in ["antegria", "obristan", "republia"]:
                    merged.blit(char, (150, 190))
                else:
                    merged.blit(char, (15, 190))
                win.blit(merged, (400, 250))
                win.blit(char, (250, 250))
                iterator += 1
            pygame.display.update()

    pass_button.draw("VALID", font_type="font_a")
    denied_button.draw("DENIED", font_type="font_a")
    # win.blit(game_map, (0, 0))
    pygame.display.update()

pygame.quit()