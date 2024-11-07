class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # High score should never be reset
        self.high_score = 0
        
        # Load high score from file if it exists
        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save the high score to a file."""
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))