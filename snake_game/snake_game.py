import pygame
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load background
background_img = pygame.image.load("background.png")  # Optional background
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.blit(background_img, (0, 0))  # Draw background image

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -GRID_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, GRID_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-GRID_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((GRID_SIZE, 0))

    # Move snake
    snake.move()

    # **Wall Wrapping Logic**
    head_x, head_y = snake.body[0]
    if head_x < 0:
        head_x = WIDTH - GRID_SIZE  # Move to right side
    elif head_x >= WIDTH:
        head_x = 0  # Move to left side
    if head_y < 0:
        head_y = HEIGHT - GRID_SIZE  # Move to bottom
    elif head_y >= HEIGHT:
        head_y = 0  # Move to top
    snake.body[0] = (head_x, head_y)

    # Collision with food
    if snake.body[0] == (food.x, food.y):
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # # Collision with walls
    # head_x, head_y = snake.body[0]
    # if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
    #     scoreboard.reset_score()
    #     snake.reset_snake()

    # Collision with tail
    if snake.body[0] in snake.body[1:]:
        scoreboard.reset_score()
        snake.reset_snake()

    # Draw everything
    food.draw(screen)
    snake.draw(screen)
    scoreboard.draw(screen)

    pygame.display.flip()  # Update screen
    clock.tick(10)  # Control speed (10 FPS)

pygame.quit()
