import pygame
from bullet import Bullet


def update_screen(screen,ai_settings, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    ship.update()
    for bullet in bullets:
        bullet.bullet_draw()
    pygame.display.flip()


def check_event(ship, screen, ai_settings, bullets):
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship, screen, ai_settings, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ship, screen, ai_settings, bullets):
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_SPACE:
        newbullet = Bullet(screen,ai_settings, ship)
        bullets.add(newbullet)

def check_keyup_event(event, ship):
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_RIGHT:
        ship.move_right = False
