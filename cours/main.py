import pygame
import time
import os
import json
import pyautogui
import button
from button import ImageButton, Button, globalization, TextBox, Text, Top, Money, Market
from autorization import Reg
from inventory import Inventory
from player import Player

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
        self.moneys = 2050

        self.market = Market(self.moneys)

        self.reg = Reg(height, width)

        self.inventory = {}


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
        reg_button = Button((20, 240, 200, 80), (255, 153, 51), 'Регистрация', 24, width_text=25)

        inventory_m = Inventory(SIZE, player_images, self.inventory)
        tim = time.time()


        self.put_on = {}

        while True:
            position_mouse = pygame.mouse.get_pos()
            press_mouse = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            window.fill((119, 51, 255))

            Money((SIZE[0]/2-200, 0), self.moneys).render()


            for button in self.buttons_ready:
                if button.name_button('Играть') and button.press(position_mouse, press_mouse):
                    self.enter_name = False
                    game.start('Вадик', self.put_on)




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
                tim = time.time()




            #-------------------------

            window.blit(player_images['stop'], (SIZE[0]/2-32, SIZE[1]/2-32))

            #----------TOP------------
            top.render(players)
            top.press(position_mouse, press_mouse)
            #-------------------------


            if self.buttons_ready[3].press(position_mouse, press_mouse) and time.time()-tim > 0.3:
                self.inventory, self.moneys = self.market.start()
                tim = time.time()

            if self.buttons_ready[4].press(position_mouse, press_mouse) and time.time()-tim > 0.3:
                self.put_on = inventory_m.start(window, self.inventory)
                tim = time.time()



            if self.prof.press(position_mouse, press_mouse):
                pass
            [button.render() for button in self.buttons_ready]



            pygame.display.update()










scroll = [0, 0]

class Game:
    def __init__(self):
        self.player = Player('Вадик', (100, 100))
        #self.player.image = 'stop'
       # self.text = Player('     Нияр', (100, 499))
        self.FPS = pygame.time.Clock()



    def start(self, name, put_on):#, players={'Muhammed': {self.player.x}}):
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


            self.player.cursor(mouse_pos, window)
            self.player.render(window, player_images, put_on)
            self.player.move(keys, press_mouse, mouse_pos, window, weapons)

            player2.render(window, player_images, put_on)
            player2.cursor(mouse_pos, window)
            player2.move(keys, press_mouse, mouse_pos, window, weapons)
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

