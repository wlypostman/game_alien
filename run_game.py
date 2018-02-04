import pygame
from settings import Settings
import game_functions as gf


def run_game():
    # pygame.init() 不需要了
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('我的游戏！')

    while True:
        gf.update_scrren(ai_settings)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


run_game()
