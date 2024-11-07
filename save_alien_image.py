import pygame
import os

# Initialize Pygame
pygame.init()

# Make sure the images directory exists
current_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_dir, 'images')
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Create a surface for the alien
alien_surface = pygame.Surface((60, 60), pygame.SRCALPHA)

# Draw the alien (a more detailed shape)
# Body (dark green)
pygame.draw.ellipse(alien_surface, (60, 120, 60), (0, 20, 60, 30))
# Head (light green)
pygame.draw.circle(alien_surface, (80, 150, 80), (30, 20), 15)
# Eyes (white with black pupils)
pygame.draw.circle(alien_surface, (255, 255, 255), (23, 18), 5)
pygame.draw.circle(alien_surface, (255, 255, 255), (37, 18), 5)
pygame.draw.circle(alien_surface, (0, 0, 0), (23, 18), 2)
pygame.draw.circle(alien_surface, (0, 0, 0), (37, 18), 2)

# Save path
alien_path = os.path.join(images_dir, 'alien.bmp')

# Save the image
pygame.image.save(alien_surface, alien_path)
print(f"Alien image saved successfully at: {alien_path}")