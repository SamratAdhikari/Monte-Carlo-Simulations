import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Random Walk')

# Colors
black = (0, 0, 0)
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255)
]

# Simulation parameters
num_particles = 100
particle_size = 2
step_size = 5

# Initialize particles
particles = []
for _ in range(num_particles):
    x = width // 2
    y = height // 2
    color = random.choice(colors)
    particles.append([x, y, color])

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update particles
    for particle in particles:
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            particle[1] -= step_size
        elif direction == 'down':
            particle[1] += step_size
        elif direction == 'left':
            particle[0] -= step_size
        elif direction == 'right':
            particle[0] += step_size
        
        # Keep particles within screen bounds
        particle[0] = max(0, min(width, particle[0]))
        particle[1] = max(0, min(height, particle[1]))
    
    # Draw particles
    screen.fill(black)
    for particle in particles:
        pygame.draw.circle(screen, particle[2], (particle[0], particle[1]), particle_size)
    
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
