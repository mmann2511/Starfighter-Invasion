import pygame
from pygame.sprite import Sprite

class XWing(Sprite):
    """Player-controlled X-Wing"""

    def __init__(self, ai_game, scale=None):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/xwing.png')
        if scale:
            self.image = pygame.transform.scale(self.image, scale)
        else:
            self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        mouse_x, _ = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x

        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.left < 0:
            self.rect.left = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)
