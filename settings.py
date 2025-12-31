class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 1200
        self.bg_color = (10, 10, 40) # Deep Space Blue

        # Ship's speed
        self.ship_speed = 3
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 100
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0) # Red  
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.alien_max_speed = 3.0
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.5
        # How quickly the alien point value increases
        self.score_scale = 1.5

        self.alien_chaos_scale = 1.05       # how fast chaos increase per level

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 10
        self.alien_speed = 1.0

        # Fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_max_speed *= self.speedup_scale
        self.alien_chaos_scale *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
