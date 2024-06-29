import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Monte Carlo Simulation for π')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Simulation parameters
num_points = 0
inside_circle = 0

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Generate a random point
    x = random.uniform(0, width)
    y = random.uniform(0, height)
    num_points += 1

    # Check if the point is inside the circle
    distance = math.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2)
    if distance <= width / 2:
        inside_circle += 1
        color = green
    else:
        color = red

    # Draw the point
    pygame.draw.circle(screen, color, (int(x), int(y)), 2)

    # Calculate π
    if num_points > 0:
        pi_estimate = 4 * inside_circle / num_points
        pygame.display.set_caption(f'Value of π: {pi_estimate:.5f}')

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
