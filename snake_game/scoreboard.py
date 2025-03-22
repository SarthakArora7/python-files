import pygame

pygame.font.init() 

# Constants
WIDTH, HEIGHT = 600, 400  # Screen size
FONT = pygame.font.Font(None, 36)  # Default Pygame font
BLACK = (0, 0, 0)

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()

    def load_high_score(self):
        """Load high score from file"""
        try:
            with open("data.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Save high score if new high score is achieved"""
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def update_score(self):
        """Increase score and update high score if needed"""
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def reset_score(self):
        """Reset score when game restarts"""
        self.score = 0

    def draw(self, screen):
        """Render the score on the screen"""
        score_text = FONT.render(f"Score: {self.score}  High Score: {self.high_score}", True, BLACK)
        screen.blit(score_text, (WIDTH // 2 - 100, 20))
