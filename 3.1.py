import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (150, 150, 150), (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 175), 150)
rect(screen, (0, 0, 0), (120, 240, 180, 30))
circle(screen, (255, 0, 0), (120, 125), 40)
circle(screen, (0, 0, 0), (120, 125), 40, 1)
circle(screen, (0, 0, 0), (124, 128), 15)
circle(screen, (255, 0, 0), (280, 115), 35)
circle(screen, (0, 0, 0), (280, 115), 35, 1)
circle(screen, (0, 0, 0), (275, 120), 15)
polygon(screen, (0, 0, 0), [(50,75), (55,60), (185,90), (180,105)])
polygon(screen, (0, 0, 0), [(320,80), (315,65), (215,95), (220,110)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()