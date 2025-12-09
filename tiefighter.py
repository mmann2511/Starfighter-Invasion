import pygame
from pygame.sprite import Sprite
import random

class TieFighter(Sprite):
    """Enemy Tie Fighter"""

    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/tiefighter.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.vx = random.uniform(-self.settings.alien_max_speed,
                                 self.settings.alien_max_speed)
        self.vy = random.uniform(-self.settings.alien_max_speed,
                                 self.settings.alien_max_speed)

        self.chaos = random.uniform(0.5, 1.5)
        self.change_timer = random.randint(30, 120)

    def _check_edges_random(self):
        screen_rect = self.screen.get_rect()

        if self.rect.left <= 0:
            self.rect.left = 0
            self.x = float(self.rect.x)
            self.vx *= -1

        elif self.rect.right >= screen_rect.right:
            self.rect.right = screen_rect.right
            self.x = float(self.rect.x)
            self.vx *= -1

        if self.rect.top <= 0:
            self.rect.top = 0
            self.y = float(self.rect.y)
            self.vy *= -1

        if self.rect.top > screen_rect.bottom:
            self.rect.y = -random.randint(50, 150)
            self.y = float(self.rect.y)

            self.vx = random.uniform(-self.settings.alien_max_speed,
                                     self.settings.alien_max_speed)
            self.vy = random.uniform(
                self.settings.alien_max_speed * 0.5,
                self.settings.alien_max_speed
            )

            self.chaos = random.uniform(0.5, 1.5)
            self.change_timer = random.randint(20, 80)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        self.vx += random.uniform(-0.3, 0.3) * self.chaos
        self.vy += random.uniform(-0.3, 0.3) * self.chaos

        if random.randint(1, 50) == 1:
            self.vx += random.uniform(-1.0, 1.0) * self.chaos
            self.vy += random.uniform(-1.0, 1.0) * self.chaos

        self.change_timer -= 1
        if self.change_timer <= 0:
            self.vx += random.uniform(-1, 1)
            self.vy += random.uniform(-1, 1)
            self.change_timer = random.randint(30, 120)

        limit = self.settings.alien_max_speed
        self.vx = max(min(self.vx, limit), -limit)
        self.vy = max(min(self.vy, limit), -limit)

        self._check_edges_random()
        
