
import pygame
import sys

pygame.init()

winWidth = 800 
winHeight = 600 
win = pygame.display.set_mode((winWidth, winHeight))

image = pymgae.image.load("fondo.png")
image = pygame.transform.scale(fondo.png,(winWidth, winHeight))

running = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

    win.blint(fondo.png,(0,0))
    pygame.display.update()

pygame.quit()
