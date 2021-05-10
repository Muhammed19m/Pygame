import pygame
import time
import os
import random
import json

from button import ImageButton, Button, globalization, TextBox

pygame.init()
pygame.font.init()


# -----------------ОКНО-----------------
SIZE = (1080, 750)
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Cyber cringe 2D city")

display = pygame.Surface(SIZE)

globalization(window)


# ______________________________________

player_images = {"stop": pygame.image.load("images\player\stop.png"), "goL1": pygame.image.load("images\player\goL1.png"), "goL2": pygame.image.load("images\player\goL2.png"), "goR1": pygame.image.load("images\player\goR1.png"), "goR2": pygame.image.load("images\player\goR2.png")}


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
            [(20, SIZE[1]-120, 200, 100), (255, 204, 0 ), (SIZE[0]+30, SIZE[1]-55), 'Играть', 48, 15],
            #[(20, SIZE[1]-120, 200, 100), (255, 255, 255), (), 'Photo', 14]
        ]
        self.buttons_ready = [Button(but[0], but[1], but[3], but[4], width_text=but[5]) for but in self.buttons]
        text = 'Чтобы установить автарку,--нужно в папку images\profile--вставить фотку--(фотка рекомендуется быть--размерорами 100х100)'
        self.box_test = TextBox((250, 130), text, (500, 300))
        self.text2 = 'и еще, если ты--то нонстоп'

        self.prof = ImageButton(profile_photo, (20, 20))

    def start(self):

        while True:
            position_mouse = pygame.mouse.get_pos()
            press_mouse = pygame.mouse.get_pressed()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            window.fill((119, 51, 255))

            self.box_test.render()
            if self.box_test.press(position_mouse, press_mouse):
                self.box_test.replace_text(self.text2)

            for button in self.buttons_ready:
                if button.press(position_mouse, press_mouse):
                    button.replace_text('подбор')
                    game.start()


            window.blit(*self.prof())

            if self.prof.press(position_mouse, press_mouse):
                pass
            [button.render() for button in self.buttons_ready]



            pygame.display.update()







class Player:
    font = pygame.font.Font(None, 24)
    def __init__(self, name: str, first_cord: tuple, HP=100):
        self.x, self.y = first_cord
        self.name = name
        self.image = 'stop'
        self.timer = 0
    def render(self):
        window.blit(player_images[self.image], [self.x, self.y])

    def move(self, keys):
        if keys[pygame.K_w] and self.y > 0: self.y -= 0.5
        if keys[pygame.K_s] and self.y < SIZE[1] - 64: self.y += 0.5
        if keys[pygame.K_a] and self.x > 0:
            self.x -= 0.5
            if self.timer < 15:
                self.image = 'goL1'
            else:
                self.image = 'goL2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        if keys[pygame.K_d] and self.x < SIZE[0] - 32:
            self.x += 0.5
            if self.timer < 15: self.image = 'goR1'
            else:
                self.image = 'goR2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        else: self.image = 'stop'

    def cursor(self, position_mouse):
        if position_mouse[0] > self.x and position_mouse[0] < self.x + 64:
            if position_mouse[1] > self.y and position_mouse[1] < self.y + 64:
                self.render_name()

    def render_name(self):
        window.blit(Player.font.render(self.name, 1, (0, 153, 51)), (self.x-8, self.y-25))

    def auto_move(self, keys):
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 0.5
        if keys[pygame.K_DOWN] and self.y < SIZE[1] - 64:
            self.y += 0.5
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 0.5
            if self.timer < 15:
                self.image = 'goL1'
            else:
                self.image = 'goL2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        if keys[pygame.K_RIGHT] and self.x < SIZE[0] - 32:
            self.x += 0.5
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
    def __init__(self, ):
        self.player = Player('Muhammed', (100, 100))
        #self.player.image = 'stop'
       # self.text = Player('     Нияр', (100, 499))
        self.FPS = pygame.time.Clock()



    def start(self):#, players={'Muhammed': {self.player.x}}):


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            window.fill((255, 255, 255))
            keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            #scroll[0] += int(self.player.x)
            #scroll[1] += int(self.player.y)

            self.player.move(keys)
            self.player.cursor(mouse_pos)
            self.player.render()

        #    self.text.auto_move(keys)
         #   self.text.render()
          #  self.text.cursor(mouse_pos)

            map1.render()

            if keys[pygame.K_ESCAPE]:
                menu.start()


            #display.blit(pygame.transform.scale(window, (1000, 1000)), (0,0))

            pygame.display.update()


            self.FPS.tick(120)

class Players:
    def __init__(self, count_player: int, players_name: tuple):
        self.count_player = count_player
        self.players_name = players_name
        self.players = {players_name[count]: Player(players_name[count], )}


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

