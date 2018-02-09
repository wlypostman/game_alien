import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    ship = Ship(screen, ai_settings)
    bullets = Group()
    while True:
        gf.check_event(ship,screen,ai_settings,bullets)
        bullets.update()
        gf.update_screen(screen, ai_settings, ship,bullets)


run_game()
