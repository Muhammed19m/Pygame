import pygame


class Player:
    font = pygame.font.Font(None, 24)
    def __init__(self, name: str, first_cord: tuple, inventory={}, HP=100):
        self.x, self.y = first_cord
        name.title()
        self.name = name
        self.image = 'stop'
        self.timer = 0



    def render(self, window, player_images, inventory={}):
        window.blit(player_images[self.image], [self.x, self.y])
        for name, image in inventory.items():
            if name == 'helmet':
                cord = (self.x+50-10, self.y-2)
                window.blit(image, cord)
            elif name == 'armor':
                cord = (self.x+50-13, self.y+25)
                window.blit(image, cord)
            elif name == 'short':
                cord = (self.x+50-13, self.y+52)
                window.blit(image, cord)
            elif name == 'boot':
                if self.image=='stop':
                    window.blit(image, (self.x+27, self.y+93))
                    window.blit(image, (self.x+57, self.y+93))
                elif self.image == 'goL1':
                    window.blit(image, (self.x + 15, self.y + 80))
                    window.blit(image, (self.x + 57, self.y + 93))
                elif self.image == 'goL2':
                    window.blit(image, (self.x + 27, self.y + 93))
                    window.blit(image, (self.x + 57, self.y + 93))
                elif self.image == 'goR1':
                    window.blit(image, (self.x + 40, self.y + 93))
                    window.blit(image, (self.x + 72, self.y + 82))
                elif self.image == 'goR2':
                    window.blit(image, (self.x + 47, self.y + 80))
                    window.blit(image, (self.x + 60, self.y + 93))
                elif self.image == 'wL':
                    window.blit(image, (self.x + 28, self.y + 93))
                    window.blit(image, (self.x + 47, self.y + 93))
                elif self.image == 'wR':
                    window.blit(image, (self.x + 38, self.y + 93))
                    window.blit(image, (self.x + 57, self.y + 93))

    def move(self, keys, press_mouse, pos, window, weapons):
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



    def cursor(self, position_mouse, window):
        if position_mouse[0] > self.x and position_mouse[0] < self.x + 100:
            if position_mouse[1] > self.y and position_mouse[1] < self.y + 100:
                self.render_name(window)

    def render_name(self, window):
        window.blit(Player.font.render(self.name, 1, (0, 153, 51)), (self.x+15, self.y-25))


    def auto_move(self, keys, SIZE):
        if keys[pygame.K_UP]:
            self.y -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_LEFT]:
            self.x -= 1
            if self.timer < 15:
                self.image = 'goL1'
            else:
                self.image = 'goL2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        if keys[pygame.K_RIGHT]:
            self.x += 1
            if self.timer < 15:
                self.image = 'goR1'
            else:
                self.image = 'goR2'
                if self.timer == 30: self.timer = 0
            self.timer += 1
        else:
            self.image = 'stop'



