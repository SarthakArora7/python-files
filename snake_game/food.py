import pygame
import random

# Constants
GRID_SIZE = 20  # Size of each grid block
WIDTH, HEIGHT = 600, 400  # Screen dimensions

class Food:
    def __init__(self):
        self.image = pygame.image.load("food.png")  # Load food image
        self.image = pygame.transform.scale(self.image, (20, 20))  # Resize to fit grid
        self.refresh()

    def refresh(self):
        """Reposition the food randomly on the grid."""
        # self.x = random.randint(0, (WIDTH - self.size) // GRID_SIZE) * GRID_SIZE
        # self.y = random.randint(0, (HEIGHT - self.size) // GRID_SIZE) * GRID_SIZE
        self.x = random.randint(0, 29) * 20  # Grid-based position
        self.y = random.randint(0, 19) * 20  # Adjust based on screen size

    def draw(self, screen):
        """Draw food on the screen."""
        # pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        screen.blit(self.image, (self.x, self.y))  # Draw food
