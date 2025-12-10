import sys
from time import sleep
import random
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from xwing import XWing
from bullet import Bullet
from tiefighter import TieFighter


class StarfighterInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Starfighter Invasion")

        # Stats & scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Player ship
        self.ship = XWing(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.aliens.update()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_high_score()
                pygame.event.set_grab(False)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.game_active:
                    self._fire_bullet()
                else:
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()

            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            pygame.event.set_grab(True)

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        bullet1 = Bullet(self)
        bullet2 = Bullet(self)

        # adjust x position from base bullet
        bullet1.rect.centerx = self.ship.rect.centerx + 35
        bullet1.x = float(bullet1.rect.x)

        bullet2.rect.centerx = self.ship.rect.centerx - 35
        bullet2.x = float(bullet2.rect.x)

        # adjust y position
        bullet1.rect.y += 20
        bullet1.y = float(bullet1.rect.y)

        bullet2.rect.y = bullet1.rect.y
        bullet2.y = float(bullet2.rect.y)

        # angle the bullet
        bullet1.dx = -0.5
        bullet2.dx = +0.5

        self.bullets.add(bullet1, bullet2)

    def _update_bullets(self):
        """Update bullet positions and remove off-screen bullets."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet–TieFighter collisions."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for fighters in collisions.values():
                self.stats.score += self.settings.alien_points * len(fighters)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()

            self.stats.level += 1
            self.settings.alien_max_speed += 0.3

            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Respond to X-Wing being hit"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """Update TieFighter movement and check collisions"""
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _create_fleet(self):
        """Create a fleet of TieFighters"""
        fighter = TieFighter(self)
        width, height = fighter.rect.size

        current_x, current_y = width, height

        while current_y < (self.settings.screen_height - 3 * height):
            while current_x < (self.settings.screen_width - 2 * width):
                self._create_fighter(current_x, current_y)
                current_x += 2 * width

            current_x = width
            current_y += 2 * height

    def _create_fighter(self, x_position, y_position):
        """Create a TieFighter at a given row/column"""
        fighter = TieFighter(self)
        fighter.x = x_position
        fighter.rect.x = x_position
        fighter.rect.y = y_position
        self.aliens.add(fighter)

    def draw_stars(self, num_stars=50):
        """Draw random stars on the screen."""
        for _ in range(num_stars):
            x = random.randint(0, self.settings.screen_width)
            y = random.randint(0, self.settings.screen_height)
            radius = random.randint(1, 2)
            color = (255, 255, 255)
            pygame.draw.circle(self.screen, color, (x, y), radius)

    def _update_screen(self):
        """Draw everything"""
        self.screen.fill(self.settings.bg_color)
        self.draw_stars(num_stars=100)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    game = StarfighterInvasion()
    game.run_game()

