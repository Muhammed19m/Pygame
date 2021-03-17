import pygame
pygame.init()

# -----------------ОКНО-----------------
__SIZE = (1080, 740)
window = pygame.display.set_mode(__SIZE)
pygame.display.set_caption("More Players")
# ______________________________________

player_images = {"player_stop": pygame.image.load("images\player\player_stop.png")}

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100

    def move(self, typ):
        if typ == 'w': self.y -= 0.5
        if typ == 's': self.y += 0.5
        if typ == 'a': self.x -= 0.5
        if typ == 'd': self.x += 0.5


player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((255,255,255))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.y > 0: player.move('w')
    if keys[pygame.K_s] and player.y < __SIZE[1]-64: player.move('s')
    if keys[pygame.K_a] and player.x > 0: player.move('a')
    if keys[pygame.K_d] and player.x < __SIZE[0]-32: player.move('d')


    window.blit(player_images["player_stop"], [player.x, player.y])



    pygame.display.update()