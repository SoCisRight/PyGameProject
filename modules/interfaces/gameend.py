
import sys
import pygame


'''游戏结束界面'''
def GameEndInterface(screen, cfg):
    replay_image = pygame.image.load(cfg.IMAGE_PATHS['replay'])
    replay_image = pygame.transform.scale(replay_image, (400, 150))
    replay_image_rect = replay_image.get_rect()
    replay_image_rect.centerx = cfg.SCREENSIZE[0] / 2
    replay_image_rect.top = cfg.SCREENSIZE[1] * 0.52

    gameover_image = pygame.image.load(cfg.IMAGE_PATHS['gameover'])
    gameover_image = pygame.transform.scale(gameover_image, (400, 150))
    gameover_image_rect = gameover_image.get_rect()
    gameover_image_rect.centerx = cfg.SCREENSIZE[0] / 2
    gameover_image_rect.centery = cfg.SCREENSIZE[1] * 0.35
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if replay_image_rect.collidepoint(mouse_pos):
                    return True
                elif gameover_image_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        screen.blit(replay_image, replay_image_rect)
        screen.blit(gameover_image, gameover_image_rect)
        pygame.display.update()
        clock.tick(cfg.FPS)