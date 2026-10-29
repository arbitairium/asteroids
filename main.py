#Call Pygame Library
import pygame
#Call constants settings
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
#Call logger state
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt: float = 0.0

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        log_state()
        for event in pygame.event.get():
        #Ability to exit game
            if event.type == pygame.QUIT:
                return


        #Fill screen with black
        screen.fill("black")

        player.draw(screen)

        #set framerate
        dt = Clock.tick(60) / 1000

        #Refresh Screen - DO THIS LAST
        pygame.display.flip()

if __name__ == "__main__":
    main()
