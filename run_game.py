import pygame
from settings import Settings


def run_game():
    # pygame.init() 不需要了
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('我的游戏！')

    while True:
        screen.fill((200, 200, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


run_game()
