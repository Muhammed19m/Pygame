import pygame
pygame.init()

from button import Button, Text, TextBox

class Reg:
    def __init__(self, h, w):
        self.h = h
        self.w = w

        self.login = Text((500, 40), '', (self.w/2-200, self.h/2-150), 32)
        self.password1 = Text((500, 40), '', (self.w/2-200, self.h/2-90), 32)
        self.password2 = Text((500, 40), '', (self.w / 2 - 200, self.h / 2 - 30), 32)
        self.code = Text((500, 40), '', (self.w / 2 - 200, self.h / 2 + 30), 32)

        self.dec1 = Text((100, 40), 'email:', (self.w/2-275, self.h/2-150), 32, color_box=(0,0,0), color=(255,255,255))
        self.dec2 = Text((120, 40), 'password:', (self.w/2-320, self.h/2-90), 32, color_box=(0,0,0), color=(255,255,255))
        self.dec3 = Text((120, 40), 'password:', (self.w/2-320, self.h/2-30), 32, color_box=(0,0,0), color=(255,255,255))
        self.dec4 = Text((210, 40), ' confirmation code:', (self.w/2-420, self.h/2+30), 32, color_box=(0,0,0), color=(255,255,255))


    def start(self, window):
        exit_b = Button((self.w/2-100, self.h/2+200, 200, 100), (255, 153, 51), 'Готово', 48, 65)
        send = Button((self.w/2-200+500+20, self.h/2-150,  100, 40), (255, 153, 51), 'send code', 18, width_text=5)

        email = 'muhammed.clams_2002@mail.ru'

        while True:
            press_mouse = pygame.mouse.get_pressed()
            poss = pygame.mouse.get_pos()
            window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            self.dec1.render()
            self.dec2.render()
            self.dec3.render()
            self.dec4.render()

            self.password1.render()
            self.password2.render()
            self.login.render()
            self.code.render()
            exit_b.render()
            if exit_b.press(poss, press_mouse): break



            if self.login.press(poss, press_mouse):
                self.login.input_text = True
                self.password1.input_text = False
                self.password2.input_text = False
                self.code.input_text = False
            if self.login.input_text:
                self.login.input()



            if self.password1.press(poss, press_mouse):
                self.login.input_text = False
                self.password1.input_text = True
                self.password2.input_text = False
                self.code.input_text = False
            if self.password1.input_text:
                self.password1.input()


            if self.password2.press(poss, press_mouse):
                self.password2.input_text = True
                self.login.input_text = False
                self.password1.input_text = False
                self.code.input_text = False
            if self.password2.input_text:
                self.password2.input()


            if self.code.press(poss, press_mouse):
                self.code.input_text = True
                self.login.input_text = False
                self.password1.input_text = False
                self.password2.input_text = False
            if self.code.input_text:
                self.code.input()



            send.render()
            if send.press(poss, press_mouse):
                break


            pygame.display.update()