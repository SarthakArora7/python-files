import pygame
import sys
from start_screen import show_start_screen
from end_screen import show_game_over_screen

pygame.font.init() 

WIDTH, HEIGHT = 600, 600  
FONT = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()

    def load_high_score(self):
        try:
            with open("data.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        score_text = FONT.render(f"Score: {self.score}  High Score: {self.high_score}", True, BLACK)
        screen.blit(score_text, (WIDTH // 2 - 100, 20))

    def get_player_name(self, screen):
        name = ""
        active = True

        while active:
            background_img = pygame.image.load("name.jpg") 
            background_img = pygame.transform.scale(background_img, (700, 600))
            screen.blit(background_img, (0, 0))
            text = FONT.render("Enter your name:", True, BLACK)
            screen.blit(text, (700 // 2 - 100, HEIGHT//6 - 30))

            name_text = FONT.render(name, True, BLACK)
            screen.blit(name_text, (700 // 2 - 100, HEIGHT // 5))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and name:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 10:
                            name += event.unicode

        self.player_name = name

    def save_score(self):
        with open("scores.txt", "a") as file:
            file.write(f"{self.player_name},{self.score}\n")
        
    def get_top_scores(self):
        try:
            with open("scores.txt", "r") as file:
                scores = []
                for line in file:
                    parts = line.strip().split(",")  
                    if len(parts) == 2:
                        name, score = parts
                        if score.strip().isdigit(): 
                            scores.append((name.strip(), int(score.strip())))

            return sorted(scores, key=lambda x: x[1], reverse=True)[:5] 

        except FileNotFoundError:
            return [] 
        except Exception as e:
            print(f"Error loading scores: {e}")
            return []

    def show_leaderboard(self, screen):
        self.save_score()
        top_scores = self.get_top_scores()
        background_img = pygame.image.load("leader_board.jpg") 
        background_img = pygame.transform.scale(background_img, (700, 600))
        screen.blit(background_img, (0, 0))
        font = pygame.font.Font(None, 50)
        title = font.render("Leaderboard", True, BLACK)
        screen.blit(title, (700 // 2 - 100, HEIGHT // 4 - 30))
        y_offset = HEIGHT // 3
        for i, (name, high_score) in enumerate(top_scores, start=1):
            text = FONT.render(f"{i}. {name}: {high_score}", True, BLACK)
            screen.blit(text, (700 // 2 - 100, y_offset))
            y_offset += 40
        pygame.display.flip()
        pygame.time.delay(5000) 

    def game_over_screen(self, screen):
        self.show_leaderboard(screen)
        show_game_over_screen(screen) 
