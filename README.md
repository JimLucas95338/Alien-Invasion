# 👾 Alien Invasion Game

A classic space shooter game built with Pygame where players control a spaceship to defend Earth from alien invaders. Battle waves of descending aliens while managing your limited ammunition and lives!

## 🎮 Game Demo

[![Gameplay Demo](https://github.com/JimLucas95338/Alien-Invasion/raw/main/Recording%202024-11-07%20154414.mp4)](https://github.com/JimLucas95338/Alien-Invasion/raw/main/Recording%202024-11-07%20154414.mp4)

*Click to watch the gameplay demo*

## 🎯 Game Features

- **Progressive Difficulty**: Speed increases with each level
- **Score System**: Points increase with each alien destroyed
- **High Score Tracking**: Your best score is saved between games
- **Limited Ammunition**: Strategic shooting with max 3 bullets at once
- **Sound Effects**:
  - "Pew-pew" laser sounds
  - Explosion effects
  - Alien destruction rumble
  - Level-up notification
- **Lives System**: Start with 3 ships
- **Dynamic Alien Movement**: Aliens move in formation and descend
- **Instant Restart**: Quick game reset with 'R' key

## 🔧 Requirements

- Python 3.x
- Pygame library
- NumPy (for sound generation)

## 📥 Installation

1. Ensure you have Python installed on your system:
```bash
python --version  # Should show Python 3.x
```

2. Install the required packages:
```bash
pip install pygame numpy
```

3. Clone the repository:
```bash
git clone https://github.com/JimLucas95338/Alien-Invasion.git
cd Alien-Invasion
```

## 🎮 How to Play

1. Start the game:
```bash
python alien_invasion.py
```

2. Controls:
- **R**: Start/Restart game
- **LEFT/RIGHT Arrows**: Move ship
- **SPACEBAR**: Fire bullets
- **Q**: Quit game

## 🎯 Gameplay Tips

1. **Watch Your Ammo**: You can only have 3 bullets on screen at once
2. **Timing is Key**: Aliens speed up with each level
3. **Protect Your Ships**: You start with 3 lives
4. **High Score Chase**: Try to beat your highest score
5. **Strategic Shooting**: Don't waste bullets, aim carefully!

## 📁 Project Structure

```
alien-invasion/
│
├── alien_invasion.py    # Main game file
├── settings.py         # Game settings and configurations
├── ship.py            # Ship class and movement
├── alien.py           # Alien class and behavior
├── bullet.py          # Bullet mechanics
├── game_stats.py      # Score and statistics tracking
├── scoreboard.py      # Score display
├── sound_manager.py   # Sound effects handling
│
├── images/            # Game sprites
│   ├── alien.bmp     # Alien sprite
│   └── ship.bmp      # Ship sprite
│
├── sounds/            # Sound effects
│   ├── shoot.wav     # Laser sound
│   ├── explosion.wav  # Ship explosion
│   ├── alien_explosion.wav  # Alien destruction
│   └── level_up.wav  # Level completion
│
└── README.md         # Documentation
```

## 🎮 Game Settings

Current default settings (can be modified in `settings.py`):
```python
Screen Size: 1200x800 pixels
Ship Speed: 2.5
Bullet Speed: 5.0
Alien Speed: 1.0
Fleet Drop Speed: 10
Max Bullets: 3
```

## 📈 Version History

### v2.0.0 (Latest)
- Added complete scoring system
- Implemented sound effects
- Added high score saving
- Added level progression
- Enhanced alien movement
- Improved game performance
- Added game statistics tracking

### v1.1.0
- Added lives system
- Implemented collision detection
- Added game over conditions
- Added restart functionality

### v1.0.0
- Initial release
- Basic movement
- Simple shooting mechanics

## 🐛 Known Issues & Future Updates

### Planned Features:
- [ ] Background music
- [ ] Different alien types
- [ ] Power-ups
- [ ] Shield system
- [ ] Boss battles
- [ ] Difficulty settings

### Known Issues:
- None currently reported

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -am 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🎮 Development Notes

### Adding New Features:
1. Create a new branch
2. Add your feature
3. Test thoroughly
4. Submit a pull request

### Testing:
- Run the game with different Python versions
- Test all key bindings
- Verify sound effects work
- Check collision detection
- Verify score tracking

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- Built with [Pygame](https://pygame.org/)
- Sound effects generated using Python
- Inspired by classic arcade games
- Thanks to all contributors and testers

## 📫 Contact

Jim Lucas - [GitHub Profile](https://github.com/JimLucas95338)

Project Link: [https://github.com/JimLucas95338/Alien-Invasion](https://github.com/JimLucas95338/Alien-Invasion)
