import pygame


def update_screen(screen,ai_settings, ship):
    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    ship.update()
    pygame.display.flip()


def check_event(ship):
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def  check_keydown_event(event, ship):
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True

def check_keyup_event(event, ship):
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_RIGHT:
        ship.move_right = False
