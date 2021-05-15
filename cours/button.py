import pygame
import os
import time
import random

window = None
def globalization(win):
    global window
    window = win


additional_pngn = os.listdir('images\\additional')
additional_png = {name[:-4]: pygame.image.load('images\\additional\\'+name) for name in additional_pngn}
del additional_pngn





class ImageButton:
    def __init__(self, image, cord: tuple, size=(100, 100)):
        self.image = image
        self.cord_x, self.cord_y = cord
        self.height = image.get_height()
        self.width = image.get_width()
        self.h_w = size
        self.surf = pygame.Surface(self.h_w)
        self.surf.blit(self.image, (0, 0))
    def render(self):
        window.blit(self.surf, (self.cord_x, self.cord_y))

    def press(self, position_mouse, press_mouse):
        if position_mouse[0] > self.cord_x and position_mouse[0] < self.cord_x + self.width:
            if position_mouse[1] > self.cord_y and position_mouse[1] < self.cord_y + self.height:
                if press_mouse[0]:
                    return True
        return False

    def __call__(self, *args, **kwargs):
        return (self.surf, (self.cord_x, self.cord_y))






class Button:
    def __init__(self, cord_w_h: tuple, color: tuple, text: str, size_font: int, color_text=(0,0,0), width_text=20):
        self.cord_x, self.cord_y, self.width, self.height = cord_w_h
        self.text = text
        self.size_font = size_font
        self.color = color
        self.width_text = width_text
        self.surf = pygame.Surface((self.width, self.height))
        self.color_text = color_text
        self.surf.fill(self.color)
        self.font = pygame.font.SysFont('verdana', self.size_font)
        self.render_text = self.font.render(self.text, 1, self.color_text)
        self.surf.blit(self.render_text, (self.width_text, (self.height-self.size_font)//2-10))



    def replace_text(self, text: str, color_text=(0,0,0)):
        self.text = text
        self.color_text = color_text
        self.surf.fill(self.color)
        self.render_text = self.font.render(self.text, 1, self.color_text)
        self.surf.blit(self.render_text, (self.width_text, (self.height-self.size_font)//2-10))

    def render(self):
        window.blit(self.surf, (self.cord_x, self.cord_y))

    def press(self, position_mouse, press_mouse):
        if position_mouse[0] > self.cord_x and position_mouse[0] < self.cord_x + self.width:
            if position_mouse[1] > self.cord_y and position_mouse[1] < self.cord_y + self.height:
                if press_mouse[0]:
                    return True
        return False

    def cursor(self, position_mouse):
        if position_mouse[0] > self.cord_x and position_mouse[0] < self.cord_x + self.width:
            if position_mouse[1] > self.cord_y and position_mouse[1] < self.cord_y + self.height:
                return True
        return False

    def name_button(self, *names):
        if self.text in names: return True
        return False



class TextBox:
    def __init__(self, size_box: tuple, text: str, cord: tuple,color_box=(51, 102, 204)):
        self.text = text.split('--')
        self.size_boz = size_box
        self.cord = cord
        self.color_box = color_box
        self.surf = pygame.Surface(self.size_boz)
        self.surf.fill(self.color_box)
        self.font = pygame.font.Font(None, 20)
        for i in range(len(self.text)):
            self.surf.blit(self.font.render(self.text[i], 1, (255,255,255)), (30, 30+(i*14)))
        self.surf.blit(additional_png['next'], (self.size_boz[0]-35, self.size_boz[1]-30))

    def render(self):
        window.blit(self.surf, self.cord)

    def press(self, position_mouse, press_mouse):
        if position_mouse[0] > self.size_boz[0]-35+self.cord[0] and position_mouse[0] < self.size_boz[0]-35 + 30+self.cord[0]:
            if position_mouse[1] > self.size_boz[1]-30+self.cord[1] and position_mouse[1] < self.size_boz[1]+self.cord[1]:
                if press_mouse[0]:
                    return True
        return False






    def replace_text(self, text):
        self.__init__(self.size_boz, self.text, self.cord)




class Text:
    def __init__(self, text: str, cord: tuple, font, color=(0, 0, 0)):
        self.cord = cord
        self.timee = 0
        self.font = font
        self.text = text
        self.color = color
    def render(self):
        window.blit(pygame.font.Font(None, self.font).render(self.text.title(), 1, self.color), self.cord)

    def input(self):
        keys_alpha = {113: 'q', 119: 'w', 101: 'e', 114: 'r', 116: 't', 121: 'y', 117: 'u', 105: 'i', 111: 'o',
                      112: 'p', 97: 'a', 115: 's', 100: 'd', 102: 'f', 103: 'g', 104: 'h', 106: 'j', 107: 'k', 108: 'l',
                      122: 'z', 120: 'x', 99: 'c', 118: 'v', 98: 'b', 110: 'n', 109: 'm'}
        key = pygame.key.get_pressed()
        for i in range(len(key)):
            if time.time() - self.timee > 0.2 and key[i]:
                self.timee = time.time()
                if i == 8:
                    self.text = self.text[:-1]
                elif i == 13:
                    return True
                else:
                    if keys_alpha.get(i) and len(self.text) <= 12:
                        self.text += keys_alpha.get(i)

    def press(self, position_mouse, press_mouse):
        if position_mouse[0] > self.cord[0] and position_mouse[0] < self.cord[0] + 200:
            if position_mouse[1] > self.cord[1] and position_mouse[1] < self.cord[1] + self.font:
                if press_mouse[0]:
                    return True
        return False

class Top:
    def __init__(self, cord: tuple, size: tuple, players: dict, I=('Player', 15), color=(255, 51, 0), type=''):
        self.cord = cord
        self.I = I
        self.type = type
        self.size = size
        self.players = players
        self.color = color
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)
        self.button = pygame.Surface((98, 60))
        self.button.fill((204, 255, 51))
        self.button.blit(pygame.font.Font(None, 40).render('day', 1, (0,0,0)), (20, 15))
        self.surf.blit(self.button, (10, size[1]-70))
        self.button.fill((204, 255, 51))
        self.button.blit(pygame.font.Font(None, 40).render('week', 1, (0, 0, 0)), (15, 15))
        self.surf.blit(self.button, (110, size[1] - 70))
        self.button.fill((204, 255, 51))
        self.button.blit(pygame.font.Font(None, 40).render('month', 1, (0, 0, 0)), (7, 15))
        self.surf.blit(self.button, (210, size[1] - 70))
        self.surf.blit(pygame.font.Font(None, 48).render('Top 10 players', 1, (0,0,0)), (45, 50))
        self.surf.blit(pygame.font.Font(None, 48).render(type, 1, (0,0,0)), (115, 100))
        self.number = 150
        count = 1
        for player, point in players.items():
            moment = f'{count}.{player}'.ljust(20, '.')
            self.surf.blit(pygame.font.Font(None, 32).render(moment+str(point), 1, (0, 51, 0)), (25, self.number))
            self.number += 40
            count += 1
        moment = f'{I[2]}.{I[0]}'.ljust(20, '.')

        self.surf.blit(pygame.font.Font(None, 32).render(moment+str(I[1]), 1, (0,0,0)), (25, self.number+50))
    def render(self, players, I):
        window.blit(self.surf, self.cord)
        self.__init__(self.cord, self.size, self.players, I, type=self.type)

    def press(self, position_mouse, press_mouse):
        if position_mouse[0] > 10+self.cord[0] and position_mouse[0] < 108+self.cord[0] and position_mouse[1] > self.size[1]-70+self.cord[1] and position_mouse[1] < self.size[1]-10+self.cord[1] and press_mouse[0]:
            self.__init__(self.cord, self.size, self.players, self.I,type='  day')
        if position_mouse[0] > 110+self.cord[0] and position_mouse[0] < 210+self.cord[0] and position_mouse[1] > self.size[1]-70+self.cord[1] and position_mouse[1] < self.size[1]+self.cord[1] and press_mouse[0]:
            self.__init__(self.cord, self.size, self.players, self.I,type=' week')
        if position_mouse[0] > 210+self.cord[0] and position_mouse[0] < self.size[0]-20+self.cord[0] and position_mouse[1] > self.size[1]-70+self.cord[1] and position_mouse[1] < self.size[1]+self.cord[1] and press_mouse[0]:
            self.__init__(self.cord, self.size, self.players, self.I,type='month')


class Money:
    def __init__(self, cord, moneys):
        self.cord = cord
        self.moneys = moneys
        self.surf = pygame.Surface((400, 100))
        self.surf.fill((0, 51, 0))
        self.surf.blit(additional_png['coin'], (50, 5))
    def render(self):
        self.surf.blit(pygame.font.Font(None, 48).render(str(self.moneys), 1, (255, 0,0 )), (200, 33))
        window.blit(self.surf, self.cord)





















