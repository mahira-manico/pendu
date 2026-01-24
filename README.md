<div align="center">

# 🎮 Hangman Game

<img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" width="200"/>

### A Modern Hangman Game Built with Python & Pygame

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-00ADD8?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/samba-gomis/pendu?style=for-the-badge)](https://github.com/samba-gomis/pendu/stargazers)

[Features](#-features) • [Installation](#-installation) • [How to Play](#-how-to-play) • [Screenshots](#-screenshots) • [Team](#-team)

---

</div>

## 📖 About

An interactive **Hangman Game** featuring a beautiful chalkboard-themed interface, multiple difficulty levels, sound effects, and a scoring system. Built as a team project at **La Plateforme_** coding school.

<div align="center">
  <img src="https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif" width="400"/>
</div>

---

## ✨ Features

### 🎯 Gameplay
- 🎲 **Random word selection** from extensive word database (100+ words)
- 🎚️ **Three difficulty levels**: Easy (10 lives), Medium (7 lives), Hard (5 lives)
- 🔤 **Real-time letter validation** and visual feedback
- 🏆 **Dynamic scoring system** with difficulty multipliers
- 💾 **Persistent leaderboard** - save your high scores

### 🎨 User Interface
- 🖼️ **Chalkboard aesthetic** with custom chalk font
- 🎭 **Smooth animations** for hangman drawing
- 📊 **Live score & lives display** with color-coded indicators
- 🏅 **Hall of Fame** with top 5 players and medal system

### 🔊 Audio Experience
- 🎵 **Background music** for menu and gameplay
- 🔔 **Sound effects** for correct/wrong guesses
- 🎺 **Victory & game over themes**
- 🔇 Optimized volume levels for comfortable gaming

### ⚙️ Technical Features
- 🏗️ **Modular architecture** - Clean separation of concerns
- 📁 **Organized project structure** with assets folders
- 💾 **File I/O management** for words and scores
- 🎮 **State machine pattern** for game flow
- 🐍 **Object-Oriented Programming** with Game class

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/samba-gomis/pendu.git
cd pendu
```

2. **Install dependencies**
```bash
pip install pygame
```

3. **Run the game**
```bash
python main.py
```

That's it! 🎉

---

## 🎮 How to Play

<div align="center">
  <img src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" width="300"/>
</div>

### Main Menu Controls

| Key | Action |
|-----|--------|
| `1` | Start Easy Mode (10 lives) |
| `2` | Start Medium Mode (7 lives) |
| `3` | Start Hard Mode (5 lives) |
| `S` | View Scores / Hall of Fame |
| `P` | Add Custom Words |

### During Gameplay

1. **Type letters** on your keyboard to guess
2. **Correct letter**: +10 points ✅
3. **Wrong letter**: Lose 1 life ❌
4. **Complete the word**: +100 bonus points! 🎉
5. Press `RETURN` or `ESC` to go back to menu

### Scoring System

```python
# Base Points
correct_letter = 10 points
complete_word = 100 points

# Difficulty Multipliers
easy_mode = 1x
medium_mode = 1.5x
hard_mode = 2x

# Example
# Hard mode, 8 letters found, word complete:
# (8 × 10 + 100) × 2 = 360 points 🔥
```

---

## 📁 Project Structure

```
pendu/
│
├── 🎮 Core Game Files
│   ├── main.py              # Entry point
│   ├── pygame_menu.py       # Main game loop & state management
│   ├── game.py              # Game logic & class
│   ├── display.py           # All rendering functions
│   ├── word.py              # Word management
│   ├── score.py             # Score calculations & persistence
│   ├── sound.py             # Audio management
│   └── constant.py          # Game constants & settings
│
├── 🎨 Assets
│   ├── images/
│   │   ├── background.jpg      # Chalkboard background
│   │   ├── hangman_logo.png    # Menu logo
│   │   └── game_logo.png       # Window icon
│   │
│   └── sounds/
│       ├── new_letter.wav      # Correct guess sound
│       ├── wrong_letter.wav    # Wrong guess sound
│       ├── score_level.wav     # Score milestone
│       ├── background_loop.wav # Menu music
│       ├── background_game.wav # Gameplay music
│       ├── victory.wav         # Win theme
│       └── game_over.wav       # Lose theme
│
├── 📊 Data
│   ├── words.txt           # Word database (100+ words)
│   └── scores.txt          # Saved high scores
│
├── ✍️ Font
│   └── chalk.ttf           # Custom chalk font
│
└── 📄 Documentation
    ├── README.md
    └── .gitignore
```

---

## 🎨 Screenshots

### Main Menu
<div align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="600"/>
  <p><i>Choose your difficulty and start playing!</i></p>
</div>

### Gameplay
<div align="center">
  <img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="600"/>
  <p><i>Guess letters before the hangman is complete</i></p>
</div>

### Victory Screen
<div align="center">
  <img src="https://media.giphy.com/media/g9582DNuQppxC/giphy.gif" width="400"/>
  <p><i>Celebrate your win and save your score!</i></p>
</div>

### Hall of Fame
<div align="center">
  <img src="https://media.giphy.com/media/26BRBKqUiq586bRVm/giphy.gif" width="400"/>
  <p><i>Top 5 leaderboard with medal system</i></p>
</div>

---

## 🛠️ Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

### Core Technologies
- **Python 3.7+** - Programming language
- **Pygame 2.0+** - Game development framework

### Programming Concepts
- ✅ Object-Oriented Programming (OOP)
- ✅ State Machine Pattern
- ✅ File I/O Operations
- ✅ Event-Driven Programming
- ✅ Modular Architecture (MVC-inspired)
- ✅ Audio Management
- ✅ Game Loop Design

---

## 🎓 Learning Outcomes

This project helped us develop skills in:

### Technical Skills
- 🐍 Advanced Python programming
- 🎮 Game development with Pygame
- 🏗️ Software architecture and design patterns
- 📂 File handling and data persistence
- 🎨 UI/UX design and user interaction
- 🔊 Audio integration and management

### Soft Skills
- 👥 Team collaboration and Git workflow
- 📋 Project planning and task distribution
- 🐛 Debugging and problem-solving
- 📖 Code documentation and readability
- ⏱️ Time management and deadlines

---

## 🎮 Game Features Breakdown

### Difficulty System

| Difficulty | Lives | Score Multiplier | Best For |
|-----------|-------|------------------|----------|
| 🟢 Easy | 10 | 1x | Beginners |
| 🟡 Medium | 7 | 1.5x | Intermediate |
| 🔴 Hard | 5 | 2x | Experts |

### Word Categories

Our word database includes:
- 🐘 **Animals** (20+ words)
- 🍕 **Food** (20+ words)
- 💻 **Technology** (15+ words)
- 🎸 **Music** (10+ words)
- 👔 **Professions** (15+ words)
- 🌍 **Nature** (20+ words)
- 🏈 **Sports & Activities** (15+ words)
- 👕 **Clothing** (10+ words)
- 🏛️ **Places** (10+ words)
- ✨ **Adjectives** (10+ words)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the project**
2. **Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contributions
- 💡 Add more word categories
- 🌍 Add language support (French, Spanish, etc.)
- 🎨 New themes (space, underwater, etc.)
- 🏆 Achievement system
- 👥 Multiplayer mode
- 💾 Cloud save feature
- 📱 Responsive design for different resolutions

---

## 👥 Team

<div align="center">

### 💻 Developers

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/samba-gomis">
        <img src="https://github.com/samba-gomis.png" width="100px;" alt="Samba Gomis"/><br />
        <sub><b>Samba Gomis</b></sub>
      </a><br />
      <sub>🎮 Game Logic & Architecture</sub>
    </td>
    <td align="center">
      <a href="https://github.com/mahira-manico">
        <img src="https://github.com/mahira-manico.png" width="100px;" alt="Mahira Manico"/><br />
        <sub><b>Mahira Manico</b></sub>
      </a><br />
      <sub>🎨 UI/UX & Display Systems</sub>
    </td>
    <td align="center">
      <a href="https://github.com/elyes-messaadia">
        <img src="https://github.com/elyes-messaadia.png" width="100px;" alt="Elyes Messaadia"/><br />
        <sub><b>Elyes Messaadia</b></sub>
      </a><br />
      <sub>🔊 Audio & File Management</sub>
    </td>
  </tr>
</table>

### 🏫 Built at La Plateforme_

<img src="https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif" width="300"/>

*Project created as part of Python programming curriculum at [La Plateforme_](https://laplateforme.io/), Marseille*

</div>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- 🎓 **La Plateforme_** for the project-based learning methodology
- 🎮 **Pygame Community** for excellent documentation and tutorials
- 🎨 **Design Inspiration** from classic arcade games
- 🔊 **Sound Effects** from various free sound libraries
- ✍️ **Chalk Font** for the authentic chalkboard aesthetic

---

## 🐛 Known Issues & Future Improvements

### Current Limitations
- ⚠️ No hint system yet
- ⚠️ Single language support (English)
- ⚠️ No difficulty auto-adjustment

### Planned Features
- [ ] 💡 Hint system (reveal random letter)
- [ ] 🌍 Multi-language support
- [ ] ⏱️ Timer challenge mode
- [ ] 🎯 Word categories selection
- [ ] 📊 Statistics dashboard
- [ ] 🎨 Multiple theme options
- [ ] 💾 Profile system with avatars
- [ ] 🏆 Achievement badges

---

## 📞 Support & Contact

Having issues or questions? Feel free to:

- 🐛 [Open an issue](https://github.com/samba-gomis/pendu/issues)
- 💬 Contact the team members directly
- ⭐ Star the repo if you like it!

---

<div align="center">

### 🎯 Made with ❤️ and lots of ☕ by the team

<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="200"/>

**[⬆ Back to Top](#-hangman-game)**

[![GitHub](https://img.shields.io/badge/GitHub-samba--gomis%2Fpendu-181717?style=for-the-badge&logo=github)](https://github.com/samba-gomis/pendu)

*Have fun and happy guessing! 🎮*

</div>