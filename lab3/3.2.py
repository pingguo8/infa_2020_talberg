import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

#фон
rect(screen, (36, 117, 102), (0, 350, 700, 350))
rect(screen, (246, 161, 75), (0, 280, 500, 70))
rect(screen, (213, 133, 138), (0, 190, 500, 90))
rect(screen, (208, 137, 191), (0, 120, 500, 70))
rect(screen, (169, 118, 219), (0, 80, 500, 40))
rect(screen, (55, 12, 141), (0, 0, 500, 80))

#рыба
polygon(screen, (236, 83, 83), [[350, 667], [350, 627], [320, 627]])
polygon(screen, (236, 83, 83), [[350, 677], [355, 700], [365, 697]])
polygon(screen, (236, 83, 83), [[330, 677], [330, 695], [310, 695]])
ellipse(screen, (46, 97, 192), (306, 645, 80, 45))
polygon(screen, (46, 97, 192), [[306, 667], [276, 650], [270, 690]])
ellipse(screen, (0, 0, 0), (365, 660, 15, 15))

#птицы маленькие
x = 100
y = 240
line(screen, (255, 255, 255), (x, y), (x-50, y-30), 4)
line(screen, (255, 255, 255), (x, y), (x+50, y-40), 4)

x = 100
y = 50
line(screen, (255, 255, 255), (x, y), (x-50, y-30), 4)
line(screen, (255, 255, 255), (x, y), (x+50, y-40), 4)

x = 300
y = 140
line(screen, (255, 255, 255), (x, y), (x-50, y-30), 4)
line(screen, (255, 255, 255), (x, y), (x+50, y-40), 4)

#клюв
polygon(screen, (255, 222, 0), [[380, 496], [415, 490], [425, 500], [380, 500]])
polygon(screen, (0, 0, 0), [[380, 496], [415, 490], [425, 500], [380, 500]], 1)
polygon(screen, (255, 222, 0), [[380, 496], [400, 498], [415, 498], [425, 500],
                                [415, 510], [380, 506]])
polygon(screen, (0, 0, 0), [[380, 496], [400, 498], [415, 498], [425, 500],
                                [415, 510], [380, 506]], 1)

#хвост
polygon(screen, (255, 255, 255), [[200, 535], [110, 480], [100, 545]])
polygon(screen, (0, 0, 0), [[200, 535], [110, 480], [100, 545]], 1)

#крыло
polygon(screen, (255, 255, 255), [[245, 510], [235, 430], [185, 410], [120, 360],
                                  [140, 410], [200, 460], [190, 510]])
polygon(screen, (0, 0, 0), [[245, 510], [235, 430], [185, 410], [120, 360],
                                  [140, 410], [200, 460], [190, 510]], 1)
polygon(screen, (255, 255, 255), [[225, 510], [215, 450], [125, 440], [90, 420], [135, 475],
                                  [175, 480], [195, 510]])
polygon(screen, (0, 0, 0), [[225, 510], [215, 450], [125, 440], [90, 420], [135, 475],
                                  [175, 480], [195, 510]], 1)


#лапа1
polygon(screen, (255, 222, 0), [[300, 605], [340, 603], [340, 605], [300, 607], [338, 615],
                                [308, 617], [336, 621], [307, 620], [305, 650], [303, 640],
                                [306, 605]])
polygon(screen, (0, 0, 0), [[300, 605], [340, 603], [340, 605], [300, 607], [338, 615],
                                [308, 617], [336, 621], [307, 620], [305, 650], [303, 640],
                            [306, 605]], 1)

#лапа2
polygon(screen, (255, 222, 0), [[283, 620], [273, 627],[270, 647], [271, 658], [278, 629],
                [285, 627], [309, 639], [307, 634], [290, 627],
                [316, 631], [283, 620], [310, 610],[280, 615]])
polygon(screen, (0, 0, 0), [[283, 620], [273, 627],[270, 647], [271, 658], [278, 629],
                [285, 627], [309, 639], [307, 634], [290, 627],
                [316, 631], [283, 620], [310, 610],[280, 615]], 1)


serf1 = pygame.Surface((500, 700), pygame.SRCALPHA)
pygame.draw.ellipse(serf1, (255, 255, 255), (10, 360, 30, 60))
serf1 = pygame.transform.rotate(serf1, 30)
screen.blit(serf1, (0, 0))

serf1 = pygame.Surface((500, 700), pygame.SRCALPHA)
pygame.draw.ellipse(serf1, (255, 255, 255), (30, 370, 30, 50))
serf1 = pygame.transform.rotate(serf1, 30)
screen.blit(serf1, (0, 0))

serf1 = pygame.Surface((700, 700), pygame.SRCALPHA)
pygame.draw.ellipse(serf1, (255, 255, 255), (140, 200, 20, 75))
serf1 = pygame.transform.rotate(serf1, 70)
screen.blit(serf1, (0, 0))

serf1 = pygame.Surface((700, 700), pygame.SRCALPHA)
pygame.draw.ellipse(serf1, (255, 255, 255), (120, 180, 20, 75))
serf1 = pygame.transform.rotate(serf1, 70)
screen.blit(serf1, (0, 0))

ellipse(screen, (255, 255, 255), (160, 500, 150, 70))
ellipse(screen, (255, 255, 255), (285, 505, 70, 30))
ellipse(screen, (255, 255, 255), (333, 487, 50, 30))
ellipse(screen, (0, 0, 0), (365, 496, 8, 5))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
