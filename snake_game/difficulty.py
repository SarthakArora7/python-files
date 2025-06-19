import pygame

WIDTH, HEIGHT = 700, 600

def select_difficulty(screen):
    background_img = pygame.image.load("difficulty_img.png")
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    screen.blit(background_img, (0, 0))
    
    font = pygame.font.Font(None, 50)
    text = font.render("Select Difficulty", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//3 - 30))
    screen.blit(text, text_rect)
    
    easy_text = font.render("Press E for Easy", True, (0, 0, 0))
    easy_rect = easy_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(easy_text, easy_rect)
    
    hard_text = font.render("Press H for Hard", True, (0, 0, 0))
    hard_rect = hard_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
    screen.blit(hard_text, hard_rect)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return "easy"
                if event.key == pygame.K_h:
                    return "hard"
