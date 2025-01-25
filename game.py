import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('DRUID')

clock = pygame.time.Clock()
test_font = pygame.font.Font('font/PixelType.ttf', 50)

game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_surface = test_font.render('My game', False, 'Black')
score_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))



play_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    play_gravity = -22
            if event.type == pygame.KEYDOWN:        
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and player_rect.bottom >= 300:
                    play_gravity = -22
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 600

                

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))

        pygame.draw.rect(screen, 'Red', score_rect)
        pygame.draw.rect(screen, 'Red', score_rect, 10)

        screen.blit(text_surface, score_rect)

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800

        screen.blit(snail_surface,snail_rect)

        # player
        
        play_gravity += 1
        player_rect.y += play_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.fill("White")
    
    pygame.display.update()
    clock.tick(60)
