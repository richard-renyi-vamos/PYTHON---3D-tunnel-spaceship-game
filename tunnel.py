import pygame
import math

class Tunnel:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_circles = 20
        self.max_radius = 400
        self.min_radius = 50
        self.depth = 5

    def draw(self, screen):
        offset = pygame.time.get_ticks() / 1000

        for i in range(self.num_circles):
            t = i / self.num_circles
            radius = self.max_radius * (1 - t) + self.min_radius * t
            x = self.width // 2 + math.cos(t * self.depth + offset) * radius / 4
            y = self.height // 2 + math.sin(t * self.depth + offset) * radius / 4
            color = [int(255 * (1 - t))] * 3
            pygame.draw.circle(screen, color, (int(x), int(y)), int(radius), 1)
