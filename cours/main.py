import pygame
import time
import os
import random
import json
import pyautogui
import button
from button import ImageButton, Button, globalization, TextBox, Text, Top, Money, Market
from autorization import Reg

pygame.init()
pygame.font.init()


# -----------------ОКНО-----------------
width, height = pyautogui.size().width, pyautogui.size().height
SIZE = (width, height)
window = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
pygame.display.set_caption("Cyber cringe 2D city")

display = pygame.Surface(SIZE)
button.SIZE = SIZE
globalization(window)


# ______________________________________

player_images = {"stop": pygame.image.load("images\player\stop.png"), "goL1": pygame.image.load("images\player\goL1.png"), "goL2": pygame.image.load("images\player\goL2.png"), "goR1": pygame.image.load("images\player\goR1.png"), "goR2": pygame.image.load("images\player\goR2.png"), "wR": pygame.image.load('images\player\wR.png'), "wL": pygame.image.load('images\player\wL.png')}
weapons = {'m1L': pygame.image.load('images\weapon\m1L.png'), 'm1R': pygame.image.load('images\weapon\m1R.png')}

profile_photo = os.listdir("images\profile")
if profile_photo:
    profile_photo = pygame.image.load('images\profile\\' + os.listdir("images\profile")[0])
else:
    profile_photo = pygame.Surface((100, 100))
    profile_photo.fill((255,255,255))


file = open('data\data.json', mode='r')
data = json.load(file)









class Menu:
    def __init__(self):
        self.buttons = \
        [
            [(20, SIZE[1]-220, 300, 200), (255, 153, 51), (SIZE[0]+30, SIZE[1]-55), 'Играть', 48, 65],
            [(SIZE[0]-320, SIZE[1]-220, 300, 200), (255, 153, 51), (), 'Выйти', 48, 65],
            [(20, SIZE[1]-340, 300, 100), (194, 194, 163), (SIZE[0]+30, SIZE[1]-55), 'Режим игры', 32, 50],
            [(SIZE[0]/2-150, SIZE[1] - 250, 300, 100), (255, 153, 51), (SIZE[0] + 30, SIZE[1] - 55), 'Маркет', 32, 90],
            [(SIZE[0] / 2 - 150, SIZE[1] - 370, 300, 100), (255, 153, 51), (SIZE[0] + 30, SIZE[1] - 55), 'Инвентарь', 32, 65]
        ]
        self.buttons_ready = [Button(but[0], but[1], but[3], but[4], width_text=but[5]) for but in self.buttons]

        self.prof = ImageButton(profile_photo, (20, 20), size=(200, 200))
        #self.name_profile = Text('Player', (20, 230), 40)
        self.enter_name = False


        self.market = Market()

        self.reg = Reg(height, width)



    def start(self):

        players = {'Обдулотыф': 1341,
                   'Обдулозыс': 1298,
                   'Тяночка3': 901,
                   'Тяночка4': 856,
                   'Тяночка5': 799,
                   'Тяночка6': 690,
                   'КираМаренка': 563,
                   'Тяночка8': 375,
                   'Тяночка9': 157,
                   'Тяночка10': 145,
                   }
        top = Top((SIZE[0]-340, 20), (320, 550), players)
        moneys = Money((SIZE[0]/2-200, 0), 189)
        reg_button = Button((20, 240, 200, 80), (255, 153, 51), 'Регистрация', 24, width_text=25)



        while True:
            position_mouse = pygame.mouse.get_pos()
            press_mouse = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            window.fill((119, 51, 255))

            moneys.render()


            for button in self.buttons_ready:
                if button.name_button('Играть') and button.press(position_mouse, press_mouse):
                    self.enter_name = False
                    game.start('Вадик')




                if button.name_button('Выйти', 'Нее...') and button.press(position_mouse, press_mouse):
                    pygame.quit()
                    exit()



            if self.buttons_ready[1].cursor(position_mouse):
                self.buttons_ready[1].replace_text('Нее...')
            else: self.buttons_ready[1].replace_text('Выйти')


            #---------profile---------
            window.blit(*self.prof())
            #self.name_profile.render()
            #if self.name_profile.press(position_mouse, press_mouse) or self.enter_name:
            #    self.enter_name = True
            #if self.enter_name:
            #    if self.name_profile.input():
            #        self.enter_name = False
            #        I[0] = self.name_profile.text
            reg_button.render()
            if reg_button.press(position_mouse, press_mouse):
                self.reg.start(window)



            #-------------------------

            window.blit(player_images['stop'], (SIZE[0]/2-32, SIZE[1]/2-32))

            #----------TOP------------
            top.render(players)
            top.press(position_mouse, press_mouse)
            #-------------------------


            if self.buttons_ready[3].press(position_mouse, press_mouse):
                self.market.start()

            if self.prof.press(position_mouse, press_mouse):
                pass
            [button.render() for button in self.buttons_ready]



            pygame.display.update()







class Player:
    font = pygame.font.Font(None, 24)
    def __init__(self, name: str, first_cord: tuple, HP=100):
        self.x, self.y = first_cord
        name.title()
        self.name = name
        self.image = 'stop'
        self.timer = 0
    def render(self):
        window.blit(player_images[self.image], [self.x, self.y])

    def move(self, keys, press_mouse, pos):
        if keys[pygame.K_w] and self.y > 0: self.y -= 1
        if keys[pygame.K_s] and self.y < 1000: self.y += 1
        if keys[pygame.K_a] and self.x > 0:
            self.x -= 1
            if self.timer < 15:
                self.image = 'goL1'
            else:
                self.image = 'goL2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        if keys[pygame.K_d] and self.x < 2000:
            self.x += 1
            if self.timer < 15: self.image = 'goR1'
            else:
                self.image = 'goR2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        else: self.image = 'stop'
        if press_mouse[2]:
            if pos[0] > self.x:
                self.image = 'wR'
                window.blit(weapons['m1R'], (self.x+50, self.y+25))
            else:
                self.image = 'wL'
                window.blit(weapons['m1L'], (self.x+9, self.y+25))



    def cursor(self, position_mouse):
        if position_mouse[0] > self.x and position_mouse[0] < self.x + 100:
            if position_mouse[1] > self.y and position_mouse[1] < self.y + 100:
                self.render_name()

    def render_name(self):
        window.blit(Player.font.render(self.name, 1, (0, 153, 51)), (self.x+15, self.y-25))


    def auto_move(self, keys):
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 1
        if keys[pygame.K_DOWN] and self.y < SIZE[1] - 64:
            self.y += 1
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 1
            if self.timer < 15:
                self.image = 'goL1'
            else:
                self.image = 'goL2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        if keys[pygame.K_RIGHT] and self.x < SIZE[0] - 32:
            self.x += 1
            if self.timer < 15:
                self.image = 'goR1'
            else:
                self.image = 'goR2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        else:
            self.image = 'stop'







scroll = [0, 0]

class Game:
    def __init__(self):
        self.player = Player('Вадик', (100, 100))
        #self.player.image = 'stop'
       # self.text = Player('     Нияр', (100, 499))
        self.FPS = pygame.time.Clock()



    def start(self, name):#, players={'Muhammed': {self.player.x}}):
        self.player.name = name
        player2 = Player(' Кирилл', (400, 100))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            window.fill((255, 255, 255))
            keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            press_mouse = pygame.mouse.get_pressed()
            #scroll[0] += int(self.player.x)
            #scroll[1] += int(self.player.y)


            self.player.cursor(mouse_pos)
            self.player.render()
            self.player.move(keys, press_mouse, mouse_pos)

            player2.render()
            player2.cursor(mouse_pos)
            player2.move(keys, press_mouse, mouse_pos)
        #    self.text.auto_move(keys)
         #   self.text.render()
          #  self.text.cursor(mouse_pos)

            #map1.render()

            if keys[pygame.K_ESCAPE]:
                menu.start()


            #display.blit(pygame.transform.scale(window, (1000, 1000)), (0,0))

            pygame.display.update()


            self.FPS.tick(120)

class Players:
    def __init__(self, count_players: int, players_name: tuple):
        self.count_players = count_players
        self.players_name = players_name
        self.players = {players_name[self.count_players]: Player(players_name[self.count_players], )}


class Map:
    def __init__(self, map):
        self.map = map
        self.glass = pygame.image.load('images\\additional\grass.png')

    def render(self):
        for line in range(len(self.map)):
            for block in range(len(self.map[line])):
                if self.map[line][block] == 1:
                    window.blit(self.glass, (block*30, line*30))



map1 = Map(data['map1'])
menu = Menu()
game = Game()

menu.start()

