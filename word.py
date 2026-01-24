import random

def read_words(file="assets/data/words.txt"):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            words = [line.strip().upper() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        return []

def choose_random_word(file="assets/data/words.txt"):
    words = read_words(file)
    if words:
        return random.choice(words)
    return None

def add_word(word, file="assets/data/words.txt"):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(word.strip().upper() + '\n')