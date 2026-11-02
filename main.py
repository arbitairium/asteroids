#Call Pygame Library
import pygame
#Call constants settings
import asteroidfield
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
#Call logger state
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt: float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
        #Ability to exit game
            if event.type == pygame.QUIT:
                return

        #Fill screen with black
        screen.fill("black")

        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.update()

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        #set framerate
        dt = Clock.tick(60) / 1000

        #Refresh Screen - DO THIS LAST
        pygame.display.flip()

if __name__ == "__main__":
    main()
