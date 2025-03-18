#allows use of code from open source pygame library
import pygame
#imports global constants
from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while(True):
        #Process input/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Update game state

        #Render/Draw
        screen.fill((0,0,0)) #RGB tuple for black
        pygame.display.flip() 
if __name__ == "__main__":
    main()