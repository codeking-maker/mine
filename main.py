import pygame

# Initialize Pygame
pygame.init()

# Set up the main game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('3D Open-World RPG')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill((135, 206, 250))  # Light blue background

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()