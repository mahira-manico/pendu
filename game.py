from word import choose_random_word
from constant import *
from score import calculate_score


class Game:
    def __init__(self, difficulty="medium"):
        self.word = choose_random_word()
        self.found_letters = set()
        self.missed_letters = set()
        self.difficulty = difficulty
        self.lives = self._get_lives(difficulty)
        self.score = 0
        self.finished = False
        self.won = False
    
    def _get_lives(self, difficulty):
        lives_map = {
            "easy": LIVES_EASY,
            "medium": LIVES_MEDIUM,
            "hard": LIVES_HARD
        }
        return lives_map.get(difficulty, LIVES_MEDIUM)
    
    def guess_letter(self, letter):  
        letter = letter.upper()
        if letter in self.found_letters or letter in self.missed_letters:
            return False
        
        if letter in self.word:
            self.found_letters.add(letter)
            self._update_score()
        else:
            self.missed_letters.add(letter)
            self.lives -= 1
        
        self._check_game_over()
        return True
    
    def _update_score(self):
        full_word = all(letter in self.found_letters for letter in self.word)
        self.score = calculate_score(len(self.found_letters), full_word, self.difficulty)
    
    def _check_game_over(self):
        if self.lives <= 0:
            self.finished = True
            self.won = False
            self.score = 0
        elif all(letter in self.found_letters for letter in self.word):
            self.finished = True
            self.won = True
            self._update_score()
    
    def get_displayed_word(self):
        return ' '.join(
            [letter if letter in self.found_letters else '_' for letter in self.word]
        )