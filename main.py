import sys
#allows use of code from open source pygame library
import pygame
#imports global constants
from constants import * 
#import player class
from player import Player
#import asteroid class
from asteroid import Asteroid
#import asteroidfield class
from asteroid_field import AsteroidField
#import shot class
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameClock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidField = AsteroidField()
    shotsGroup = pygame.sprite.Group()
    Shot.containers = (shotsGroup, updatable, drawable)

    

    while(True):
        #Process input/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Update game state
        updatable.update(dt)
        for item in asteroids:
            if item.check_collisions(player):
                print("Game Over!")
                sys.exit()
            for bullet in shotsGroup:
                if bullet.check_collisions(item):
                    bullet.kill()
                    item.split()

        #Render/Draw
        screen.fill((0,0,0)) #RGB tuple for black
        for item in drawable:
            item.draw(screen)
        pygame.display.flip() 

        #Update game clock
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()