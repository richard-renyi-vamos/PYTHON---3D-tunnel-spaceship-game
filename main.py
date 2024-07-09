import pygame
from tunnel import Tunnel
from spaceship import Spaceship

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Tunnel Effect with Spaceship")

# Colors
BLACK = (0, 0, 0)

# Create game objects
tunnel = Tunnel(width, height)
spaceship = Spaceship(width, height)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle spaceship movement
    keys = pygame.key.get_pressed()
    spaceship.move(keys)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the tunnel
    tunnel.draw(screen)

    # Draw the spaceship
    spaceship.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
