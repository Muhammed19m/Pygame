import pygame
import os


window = None
def globalization(win):
    global window
    window = win


additional_pngn = os.listdir('images\\additional')
additional_png = {name[:-4]: pygame.image.load('images\\additional\\'+name) for name in additional_pngn}
del additional_pngn





class ImageButton:
    def __init__(self, image, cord: tuple, h_w=(100, 100)):
        self.image = image
        self.cord_x, self.cord_y = cord
        self.height = image.get_height()
        self.width = image.get_width()
        self.h_w = h_w
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
        self.__init__(self.size_boz, text, self.cord)






























