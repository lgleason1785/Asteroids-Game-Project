import pygame, random
from circle_shape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", tuple(self.position), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            #Generate random angle and new asteroid radius
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
         
            #Generate new asteroid vectors
            positive_velocity_vector = self.velocity.rotate(random_angle)   
            negative_velocity_vector = self.velocity.rotate(-random_angle)
            
            #Create new asteroid instances
            new_positive_asteroid = Asteroid(self.position.x , self.position.y, new_radius)
            new_negative_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

            #Set new asteroids velocity
            new_positive_asteroid.velocity = positive_velocity_vector * 1.2
            new_negative_asteroid.velocity = negative_velocity_vector * 1.2

            #Add new asteroid instances to parent groups
            for group in self.groups():
                group.add(Asteroid(self.position.x, self.position.y, new_radius),
                          Asteroid(self.position.x, self.position.y, new_radius))