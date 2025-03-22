import pygame

WIDTH, HEIGHT = 700, 600
def show_game_over_screen(screen):
    # screen.fill((0, 0, 0))  # Black background
    background_img = pygame.image.load("start_end_bg_img.jpg")  # Optional background
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    screen.blit(background_img, (0, 0))  # Draw background image
    font = pygame.font.Font(None, 50)
    text = font.render("GAME OVER!", True, (0, 0, 0))  # Black color
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//3 - 30))
    screen.blit(text, text_rect)

    restart_text = font.render("Press R to Restart", True, (0, 0, 0))
    restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT - HEIGHT//3 + 30))
    screen.blit(restart_text, restart_rect)

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart game
                    waiting = False
