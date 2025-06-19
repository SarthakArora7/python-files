import pygame
import random

WIDTH, HEIGHT = 700, 600
GRID_SIZE = 20

class Obstacle:
    def __init__(self, num_obstacles=6):
        self.num_obstacles = num_obstacles
        self.obstacles = []
        self.image = pygame.image.load("obstacle.jpg")  
        self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE)) 
        self.generate_obstacles()

    def generate_obstacles(self):
        self.obstacles = [
            (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
             random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
            for _ in range(self.num_obstacles)
        ]

    def refresh(self, score):
        if score % 3 == 0:  # Check if score is a multiple of 3
            self.num_obstacles += 1  # Increase obstacle count
        self.generate_obstacles()  # Generate new positions

    def draw(self, screen):
        for obs in self.obstacles:
            screen.blit(self.image, obs)
