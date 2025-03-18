#allows use of code from open source pygame library
import pygame
#imports global constants
from constants import * 
#import player class
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameClock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while(True):
        #Process input/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Update game state
        player.update(dt)

        #Render/Draw
        screen.fill((0,0,0)) #RGB tuple for black
        player.draw(screen)
        pygame.display.flip() 

        #Update game clock
        dt = gameClock.tick(60) / 1000


if __name__ == "__main__":
    main()