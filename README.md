# 👾 Alien Invasion Game

A classic space shooter game built with Pygame where players control a spaceship to defend Earth from alien invaders. Battle waves of descending aliens while managing your limited ammunition and lives!

## 🎮 Game Overview

Alien Invasion is an action-packed 2D space shooter where you pilot Earth's last defense against waves of alien invaders. Control your spaceship at the bottom of the screen, dodge alien attacks, and shoot down the invading fleet before they reach Earth's surface. Each hit from an alien costs you a life - can you survive and protect our planet?

## 🔧 Requirements

- Python 3.x
- Pygame library

## 📥 Installation

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://python.org).

2. Install Pygame using pip:
```bash
pip install pygame
```

3. Clone or download this repository:
```bash
git clone [your-repository-url]
cd alien-invasion
```

## 🚀 How to Run

Run the game by executing the main script:
```bash
python alien_invasion.py
```

## 🎯 Game Controls

- **Left Arrow**: Move ship left
- **Right Arrow**: Move ship right
- **Spacebar**: Shoot bullets
- **Q**: Quit game
- **R**: Restart game (when game over)

## 🎮 Gameplay Features

- **Lives System**: Start with 3 lives
- **Limited Ammunition**: Maximum of 3 bullets at once
- **Dynamic Alien Movement**: Aliens move sideways and down
- **Progressive Difficulty**: New wave of aliens after clearing the screen
- **Game Over Conditions**:
  - Losing all lives
  - Aliens reaching the bottom of the screen
- **Instant Restart**: Press 'R' to start a new game after game over
- **Brief Invulnerability**: Short pause after being hit to regroup

## 📁 Project Structure

```
alien-invasion/
│
├── alien_invasion.py    # Main game file
├── settings.py         # Game settings and configurations
├── ship.py            # Ship class and related functions
├── alien.py           # Alien class and behaviors
├── bullet.py          # Bullet class and projectile management
├── images/            # Game assets
│   ├── alien.bmp     # Alien sprite
│   └── ship.bmp      # Ship sprite
└── README.md          # Game documentation
```

## 🛠️ Current Features

- Smooth ship movement
- Shooting mechanics
- Collision detection
- Lives system
- Alien fleet movement
- Game over conditions
- Restart capability
- Custom game window with configurable settings
- Clean exit functionality

## 📝 Planned Features

- Scoring system
- Sound effects
- Background music
- Level progression
- High score tracking
- Power-ups
- Different alien types
- Boss battles
- Animated explosions
- Main menu
- Difficulty settings

## 🎯 Game Settings

Current default settings (can be modified in `settings.py`):
- Screen: 1200x800 pixels
- Ship Speed: 1.5
- Bullet Speed: 1.5
- Bullet Size: 3x15 pixels
- Max Bullets: 3
- Alien Speed: 1.0
- Fleet Drop Speed: 10

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to add. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 🐛 Bug Reports

Found a bug? Please open an issue and include:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)
- System information

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- Built with [Pygame](https://pygame.org/)
- Inspired by classic space shooter arcade games
- Special thanks to the Python and Pygame communities

## 🔄 Version History

### v1.1.0
- Added lives system
- Implemented collision detection
- Added game over conditions
- Added restart functionality
- Enhanced alien fleet movement
- Added bullet limitations

### v1.0.0
- Initial release
- Basic movement
- Simple shooting mechanics
