import json

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.load_high_score()
        
        #Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Load the high score"""
        try:
            with open('high_score.json') as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        """Save the current high score"""
        with open('high_score.json', 'w') as f:
            json.dump(self.high_score,f)                    
