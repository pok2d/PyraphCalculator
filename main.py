import pygame
import decimal

blackpix = pygame.image.load('singularblackpixel.png')

slope = decimal.Decimal(input('Please put your slope: '))
bvalue = int(input('Please put your b value (integer): '))
exponent = int(input('Please put your exponent: '))

# Initialization
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Pyraph Graphing Calculator')
running = True

# The two lists for where we will be saving each x value with its y value for loading.
xvalueslist = []
yvalueslist = []


# Main calculation for slope and b value.
for xvalue in range(-500, 500):
    # This calculates slope, and the reason we have a * -1 is for pygame basically counting every pixel down or right as
    # positive, completely opposite from how we normally graph it. So, we need the slope reversed.
    # Note that ** means to the power of, so x to the power of our selected exponent.
    yvalue = (xvalue ** exponent) * slope * -1
    # Here you can see we add 500 to our x and y value. This to center our line to our window. When we run this, our
    # line starts are 0, 0, the top left corner of the screen. We want it to start in the center, so by adding 500 to
    # both the default x and y values, it goes down (pos y)) to the vertical center, and then right (pos x) to the
    # horizontal center.
    yvalue -= bvalue - 500
    xvalue += 500
    # We now simply add our xvalues and yvalues to 2 lists, for loading later.
    xvalueslist.append(xvalue)
    yvalueslist.append(yvalue)


# Main game loop. If running == false, it all ends.
while running:
    # Detection if you press on the x button in the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Creates white background.
    window.fill((255, 255, 255))
    # This is the loop for loading all our pixels for the line. It starts by taking an x value and then loading it with
    # the correct y value.
    for selectedxvalue in xvalueslist:
        # Loading command.
        window.blit(blackpix, (selectedxvalue, round(yvalueslist[selectedxvalue])))
        # Next line can simply print current x and y value. Really only helpful for when troubleshooting program.
        # print(f'{selectedxvalue} and {yvalueslist[selectedxvalue]}')

    # Updates the window visually.
    pygame.display.update()
