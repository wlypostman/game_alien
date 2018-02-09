import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ai_settings,ship):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
    
    def bullet_draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
