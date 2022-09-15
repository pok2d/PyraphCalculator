import os
import pygame
blackpix = pygame.image.load('singularblackpixel.png')

slope = int(input('Please put your slope (integer): '))
bvalue = int(input('Please put your b value (integer): '))

# Initialization
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Pyraph Graphing Calculator')
running = True

xvalueslist = []
yvalueslist = []

timesslope = 1

printinglinestartnum = 0

for xvalue in range(0, 1000):
    yvalue = timesslope * slope * -1
    yvalue -= bvalue - 1000
    timesslope += 1
    xvalueslist.append(xvalue)
    yvalueslist.append(yvalue)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255, 255, 255))
    for item in xvalueslist:
        window.blit(blackpix, (item, yvalueslist[printinglinestartnum]))
        print(f'{item} and {yvalueslist[printinglinestartnum]}')
        printinglinestartnum += 1
    printinglinestartnum *= 0
    window.convert_alpha()
    pygame.display.update()

    

