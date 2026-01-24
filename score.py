from constant import *

def read_scores(file="assets/data/scores.txt"):
    scores = []
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                if ',' in line:
                    name, score = line.strip().split(',')
                    scores.append((name, int(score)))
    except FileNotFoundError:
        pass
    return sorted(scores, key=lambda x: x[1], reverse=True)

def save_score(name, score, file="assets/data/scores.txt"):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f"{name},{score}\n")

def calculate_score(found_letters, full_word, difficulty):
    bonus = {
        "easy": EASY_BONUS,
        "medium": MEDIUM_BONUS,
        "hard": HARD_BONUS,
    }
    score = found_letters * POINTS_PER_LETTER
    if full_word:
        score += POINTS_FULL_WORD
    return int(score * bonus.get(difficulty, 1))