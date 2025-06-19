import pygame
import random

class Food:
    def __init__(self):
        self.image = pygame.image.load("food.png")  
        self.image = pygame.transform.scale(self.image, (20, 20)) 
        self.refresh()

    def refresh(self):
        self.x = random.randint(0, 29) * 20  
        self.y = random.randint(0, 29) * 20  

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
