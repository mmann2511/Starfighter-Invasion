import pygame
from pygame.sprite import Sprite
import random
from bullet import TieFighterBullet

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

        screen_rect = self.screen.get_rect()

        # Starting position random x position
        self.rect.centerx = random.randint(0, screen_rect.width)
        # Start top of screen
        self.rect.y = -100

        # Store positions as floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        ship = ai_game.ship

        # Direction vector from TIE → Ship
        dx = ship.rect.centerx - self.x
        dy = ship.rect.centery - self.y

        # Normalize the vector (convert to speed 1)
        distance = (dx**2 + dy**2) ** 0.5
        self.vx = dx / distance
        self.vy = dy / distance

        # Scale the speed
        self.speed = 10.0
        self.vx *= self.speed
        self.vy *= self.speed

        # Firing Timer
        self.fire_timer = random.randint(20, 90)      #1-2 seconds at 60 FPS
        self.ready_for_second_shot = False

    def fire(self):
        if self.fire_timer > 0:
            return

        offset = 5

        bullet_left = TieFighterBullet(
            self.ai_game,
            self.rect.centerx - offset,
            self.rect.bottom,
        )

        bullet_right = TieFighterBullet(
            self.ai_game,
            self.rect.centerx + offset,
            self.rect.bottom,
        )
        # adjust y position
        bullet_left.rect.y -= 20
        bullet_left.y = float(bullet_left.rect.y)

        bullet_right.rect.y = bullet_left.rect.y
        bullet_right.y = float(bullet_right.rect.y)

        # angle the bullet
        bullet_left.dx = +0.05
        bullet_right.dx = -0.05

        self.ai_game.enemy_bullets.add(bullet_left, bullet_right)  
        self.fire_timer = random.randint(30,90)  


    def update(self):
        """Fighter Movement"""
        # Update Rect
        self.x += self.vx
        self.y += self.vy

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.rect.top > self.screen.get_rect().bottom:
            self.kill()

        # Handle Firing
        self.fire_timer -= 1

        if self.fire_timer <= 0 and not self.ready_for_second_shot:
            self.fire()
            self.ready_for_second_shot = True
            self.fire_timer = 8
            return
        
        if self.fire_timer <= 0 and self.ready_for_second_shot:
            self.fire()
            self.ready_for_second_shot = False
            self.fire_timer = random.randint(120, 180)
            return
