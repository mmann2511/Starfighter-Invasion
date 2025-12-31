import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct positions
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.dx = 0.0

    def update(self):
        """Move the bullet up the screen"""
        # Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        
        # Update the rect position
        self.rect.y = self.y

        # x position (for angled shots)
        self.x += self.dx
        self.rect.x = int(self.x)

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


###################################################
# 
# TieFighter Bullet
#
# #################################################    

class TieFighterBullet(Bullet):
    """Enemy fighter bullet mechanics"""
    def __init__(self, ai_game, x, y):
        super().__init__(ai_game)
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Green laser
        self.color = (50, 255, 50)

        # Create bullet rect
        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)

        # Tie Fighter fires downward, so use midbottom instead of midtop
        self.rect.centerx = x
        self.rect.top = y

        # store float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.dx = 0.0

    def update(self):
        """Move bullet DOWN the screen."""
        self.y += self.settings.bullet_speed * 2   # enemy bullets slower
        self.rect.y = int(self.y)

        # x position (for angled shots)
        self.x += self.dx
        self.rect.x = int(self.x)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
