import pygame

GRID_SIZE = 20  

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  
        self.direction = (GRID_SIZE, 0) 
        self.snake_head_img = pygame.image.load("snake_head.png") 
        self.snake_body_img = pygame.image.load("snake_body.png")  
        self.snake_head_img = pygame.transform.scale(self.snake_head_img, (20, 20)) 
        self.snake_body_img = pygame.transform.scale(self.snake_body_img, (20, 20))

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head) 
        self.body.pop() 

    def extend(self):
        self.body.append(self.body[-1])

    def reset_snake(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (GRID_SIZE, 0)

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, screen):
        for i, pos in enumerate(self.body):
            x, y = pos
            if i == 0:
                screen.blit(self.snake_head_img, (x, y))  
            else:
                screen.blit(self.snake_body_img, (x, y))  
