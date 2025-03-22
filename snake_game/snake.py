import pygame

# Constants
GRID_SIZE = 20  # Size of each grid block
WHITE = (255, 255, 255)  # Snake color

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Initial snake positions
        self.direction = (GRID_SIZE, 0)  # Moving right initially
        self.snake_head_img = pygame.image.load("snake_head.png")  # Load Snake Head Image
        self.snake_body_img = pygame.image.load("snake_body.png")  # Load Snake Body Image
        self.snake_head_img = pygame.transform.scale(self.snake_head_img, (20, 20))  # Resize
        self.snake_body_img = pygame.transform.scale(self.snake_body_img, (20, 20))

    def move(self):
        """Move the snake forward by shifting segments."""
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)  # Add new head position
        self.body.pop()  # Remove tail

    def extend(self):
        """Extend the snake by adding a new segment at the tail."""
        self.body.append(self.body[-1])

    def reset_snake(self):
        """Reset snake to its initial position."""
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (GRID_SIZE, 0)

    def change_direction(self, new_direction):
        """Change the movement direction while preventing reverse movement."""
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, screen):
        """Draw the snake on the screen."""
        # for segment in self.body:
        #     pygame.draw.rect(screen, WHITE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        for i, pos in enumerate(self.body):
            x, y = pos
            if i == 0:
                screen.blit(self.snake_head_img, (x, y))  # Draw head
            else:
                screen.blit(self.snake_body_img, (x, y))  # Draw body
