import pygame
pygame.init()


win = pygame.display.set_mode((100, 100))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pres = pygame.key.get_pressed()

    for i in range(len(pres)):
        if pres[i]:
            print(i)
            print(pres)

    print(pres[pygame.K_LSHIFT])