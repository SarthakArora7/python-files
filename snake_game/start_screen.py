import pygame

WIDTH, HEIGHT = 700, 600
def show_start_screen(screen):
    background_img = pygame.image.load("start_end_bg_img.jpg") 
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    screen.blit(background_img, (0, 0))
    font = pygame.font.Font(None, 50) 
    text = font.render("Press Any Key to Start", True, (0, 0, 0))  
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//3 - 30))  
    screen.blit(text, text_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  
                waiting = False
