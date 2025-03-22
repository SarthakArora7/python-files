import pygame

WIDTH, HEIGHT = 700, 600
def show_start_screen(screen):
    # screen.fill((0, 0, 0))  # Black background
    background_img = pygame.image.load("start_end_bg_img.jpg")  # Optional background
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    screen.blit(background_img, (0, 0))  # Draw background image
    font = pygame.font.Font(None, 50)  # Default font, size 50
    text = font.render("Press Any Key to Start", True, (0, 0, 0))  # Black text
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//3 - 30))  # Centered text
    screen.blit(text, text_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  # Any key starts the game
                waiting = False
