# Hangman Game - AI Developer Instructions

## Project Overview
**Pendu** is a Hangman game built with Python and Pygame featuring a chalkboard UI, multiple difficulty levels, persistent scoring, and audio effects. The codebase uses a modular architecture where game logic is separated from UI rendering and pygame event handling.

## Architecture

### Core Components

| Component | File | Purpose |
|-----------|------|---------|
| **Game Engine** | `game.py` | `Game` class manages game state: word, guessed letters, lives, scoring, and win/loss conditions |
| **UI Layer** | `display.py` | Pygame rendering functions for menu, game board, scores screen |
| **Menu Loop** | `pygame_menu.py` | Main event loop handling state transitions (MENU → GAME → VICTORY/GAME_OVER → SCORES) |
| **Constants** | `constant.py` | Colors, screen dimensions, difficulty settings (e.g., `LIVES_EASY=10`, `LIVES_HARD=5`) |
| **Data Access** | `word.py`, `score.py` | File I/O for word database (`assets/data/words.txt`) and leaderboard (`assets/data/scores.txt`) |
| **Audio** | `sound.py` | Sound effect triggers on correct guess, wrong guess, victory |
| **Entry Point** | `main.py` | Imports all modules and calls `menu()` |

### Data Flow
```
menu() [pygame_menu.py]
  ↓ (user picks difficulty)
Game("easy"|"medium"|"hard") [game.py]
  ↓ (user guesses letter)
guess_letter(letter) → game state updated
  ↓ (check win/loss)
_check_game_over() → finished=True → display VICTORY or GAME_OVER
```

## Key Patterns & Conventions

### Game State Management
- `Game` class encapsulates all game state: `found_letters`, `missed_letters`, `lives`, `score`, `finished`, `won`
- Difficulty directly determines lives: Easy=10, Medium=7, Hard=5 (defined in `constant.py`)
- Score multiplier applied per difficulty: Easy=1x, Medium=1.5x, Hard=2x
- **Never modify lives/score outside `Game` methods** - always use `guess_letter()` and `_update_score()`

### Letter Guess Logic
```python
# In game.py:
def guess_letter(self, letter):
    if letter in found_letters or missed_letters:
        return False  # Already guessed
    if letter in self.word:
        self.found_letters.add(letter)  # Correct
    else:
        self.missed_letters.add(letter)  # Wrong
        self.lives -= 1
    self._check_game_over()
    return True
```
Letters are stored as **uppercase strings in sets** for O(1) lookup.

### Score Calculation
Located in `score.py`. Formula: `(found_letters * POINTS_PER_LETTER + full_word_bonus) * difficulty_multiplier`
- Full word bonus (100 points) only awarded on victory
- Score resets to 0 on loss

### File Persistence
- **Words**: One word per line in `assets/data/words.txt`, uppercase, UTF-8 encoded
- **Scores**: CSV format `name,score` in `assets/data/scores.txt`, sorted by score descending
- Functions: `read_words()`, `choose_random_word()`, `add_word()`, `read_scores()`, `save_score()`

## Common Development Tasks

### Adding a New Difficulty Level
1. Add constant in `constant.py`: `LIVES_CUSTOM = 6`, `CUSTOM_BONUS = 1.8`
2. Update `_get_lives()` dict in `game.py`
3. Add menu option in `pygame_menu.py`: `elif event.key==pygame.K_4: current_game=Game("custom")`
4. Update menu display in `display.py`

### Modifying Scoring
Edit `score.py` formula and multipliers in `constant.py`. Verify against existing saved scores to ensure leaderboard validity.

### Adding Sound Effects
Place `.wav` or `.ogg` file in `assets/sounds/`, load in `sound.py` using `pygame.mixer.Sound()`, trigger with `play_sound(sound_name)` in `pygame_menu.py`.

### Expanding Word Database
Add words to `assets/data/words.txt` (one per line, uppercase) or use in-game "Add Word" feature (state="ADD_WORD" in `pygame_menu.py`).

## Important Notes

- **Pygame Initialization**: `pygame.init()` and screen setup happen in `pygame_menu.py` on import, not in `main.py`
- **Font Dependency**: `chalk.ttf` must exist in project root for custom font rendering
- **Image Loading**: Gracefully handles missing assets (e.g., `HAS_LOGO=False` if logo missing)
- **State Machine**: Game state controlled by `current_state` variable in `pygame_menu.py` main loop
- **No Global Game Object**: Each menu navigation creates a new `Game()` instance; use `current_game` reference in loop

## Testing Patterns
- Game logic is isolated in `Game` class → unit test `guess_letter()`, `_check_game_over()`, `calculate_score()`
- UI is separate from logic → mock `Game` state for display testing
- File I/O can be tested with temporary test files in `assets/data/`
