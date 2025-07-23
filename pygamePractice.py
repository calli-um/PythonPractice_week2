import pygame
import sys

#initialising all pygame modules
pygame.init()

#setup the screen
screen=pygame.display.set_mode((640,480)) #WIDTH, HEIGHT
pygame.display.set_caption("My First Pygame App")

#set-up colours (RGB format)
WHITE=(255,255,255)   #values for RBG 0-255 
BLUE=(0,0,255)          

#main game loop
running=True
while running:
    screen.fill(WHITE) #clear screen with white

    #event handling loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #draw something
    pygame.draw.circle(screen, BLUE, (220,140),50) 
    pygame.draw.ellipse(screen, BLUE, (520,240 , 100, 60))

    #update display
    pygame.display.flip()

#quit pygame
pygame.quit()
sys.exit()