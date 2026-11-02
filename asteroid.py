import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "white", (int(self.position.x), int(self.position.y)), self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt


    #if asteroid is shot
    def split(self) -> None:
        #kill original sprite
        self.kill()
        #if was smallest asteriod size, kill all
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        #if was bigger, split into 2 smaller asteroids
        log_event("asteroid_split")
        #create new random angle for new asteroids
        random_angle = random.uniform(20, 50)
        #determine size of new asteriods
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #determine new vector and velocity of the 2 astroids, in opposite angles
        new_velocity1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        new_velocity2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)

        #create new asteriods and give them the vectors/velocities
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        #speed up the baby asteriods
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2
