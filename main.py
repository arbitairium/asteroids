#Call Pygame Library
import pygame
#Call constants settings
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
#Call logger state
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        #Ability to exit game

        #Fill screen with black
        screen.fill("black")

        #Ability to exit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Refresh Screen - DO THIS LAST
        pygame.display.flip()

if __name__ == "__main__":
    main()
