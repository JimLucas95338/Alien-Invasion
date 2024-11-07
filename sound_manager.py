import pygame
import os

class SoundManager:
    """A class to manage all game sounds."""
    
    def __init__(self):
        """Initialize the sound system."""
        pygame.mixer.init()
        
        # Get the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sounds_dir = os.path.join(current_dir, 'sounds')
        
        # Load sound effects
        self.shoot_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'shoot.wav'))
        self.explosion_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'explosion.wav'))
        self.alien_explosion_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'alien_explosion.wav'))
        self.level_up_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'level_up.wav'))
        
        # Set volumes
        self.shoot_sound.set_volume(0.3)
        self.explosion_sound.set_volume(0.4)
        self.alien_explosion_sound.set_volume(0.3)
        self.level_up_sound.set_volume(0.5)
    
    def play_shoot(self):
        """Play shooting sound."""
        self.shoot_sound.play()
    
    def play_explosion(self):
        """Play ship explosion sound."""
        self.explosion_sound.play()
    
    def play_alien_explosion(self):
        """Play alien explosion sound."""
        self.alien_explosion_sound.play()
    
    def play_level_up(self):
        """Play level up sound."""
        self.level_up_sound.play()