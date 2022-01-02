import pygame
import os 
import time
import random

from pygame.transform import scale 



WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADERS MINIGAME")

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40


#LOAD IMAGES

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACE_SHIP,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACE_SHIP,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)



RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#Background 
BG = pygame.image.load(os.path.join("assets", "background-black.png"))





def main():
    FPS = 60
    run = True
    clock = pygame.time.Clock()
    
    def redraw_window():
    pygame.display.update()
    
    
    
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
main()
