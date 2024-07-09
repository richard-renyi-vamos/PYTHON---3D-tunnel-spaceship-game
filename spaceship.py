import pygame

class Spaceship:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed = 5
        self.size = 20

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), [
            (self.x, self.y - self.size // 2),
            (self.x - self.size // 2, self.y + self.size // 2),
            (self.x + self.size // 2, self.y + self.size // 2)
        ])
