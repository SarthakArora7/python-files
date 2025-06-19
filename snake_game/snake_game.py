import pygame
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from start_screen import show_start_screen
from end_screen import show_game_over_screen
from difficulty import select_difficulty
from obstacles import Obstacle 
import random

pygame.init()

WIDTH, HEIGHT = 700, 600
GRID_SIZE = 20
BACKGROUND_COLOR = (0, 0, 0)  # Black

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

show_start_screen(screen)

background_img = pygame.image.load("background.png")  # Optional background
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

snake = Snake()
food = Food()
scoreboard = Scoreboard()
clock = pygame.time.Clock()
difficulty = select_difficulty(screen)

obstacles = Obstacle()  

scoreboard.get_player_name(screen)

def random_turn():
    current_direction = snake.direction  
    if current_direction in [(GRID_SIZE, 0), (-GRID_SIZE, 0)]:  
        new_direction = random.choice([(0, GRID_SIZE), (0, -GRID_SIZE)]) 
    else: 
        new_direction = random.choice([(GRID_SIZE, 0), (-GRID_SIZE, 0)]) 
    snake.change_direction(new_direction)

running = True
while running:
    screen.blit(background_img, (0, 0)) 

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

    snake.move()

    head_x, head_y = snake.body[0]  

    # Check for wall collision in HARD mode
    if difficulty == "hard":
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            # show_game_over_screen(screen)
            scoreboard.game_over_screen(screen)
            snake.reset_snake()
            scoreboard.reset_score()
            continue  # Restart game loop after reset

    # Wrap around in EASY mode
    elif difficulty == "easy":
        if head_x < 0:
            head_x = WIDTH - GRID_SIZE 
        elif head_x >= WIDTH:
            head_x = 0 
        if head_y < 0:
            head_y = HEIGHT - GRID_SIZE 
        elif head_y >= HEIGHT:
            head_y = 0 
        snake.body[0] = (head_x, head_y)

    # Collision with obstacles -> Reduce score
    if (head_x, head_y) in obstacles.obstacles:
        scoreboard.score = max(0, scoreboard.score - 1)  # Prevent negative scores
        random_turn()

    # Collision with food -> Refresh obstacles
    if snake.body[0] == (food.x, food.y):
        food.refresh()
        scoreboard.update_score()
        snake.extend()
        obstacles.refresh(scoreboard.score)  # **Regenerate obstacles**

    # Collision with tail
    if snake.body[0] in snake.body[1:]:
        scoreboard.game_over_screen(screen)
        snake.reset_snake()
        scoreboard.reset_score()

    food.draw(screen)
    snake.draw(screen)
    obstacles.draw(screen)
    scoreboard.draw(screen)

    pygame.display.flip()
    clock.tick(10)  

pygame.quit()
