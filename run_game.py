import pygame


def run_game():
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('我的游戏！')

    while True:
        screen.fill((200, 200, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


run_game()
