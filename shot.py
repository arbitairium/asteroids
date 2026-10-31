from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame

class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, "white", (int(self.position.x), int(self.position.y)), self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
