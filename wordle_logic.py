import random, os

BASE_DIR = os.path.dirname(__file__)
WORDS_PATH = os.path.join(BASE_DIR, 'assets', 'words.txt')
GUESSES_PATH = os.path.join(BASE_DIR, 'assets', 'guesses.txt')

def WORDS(path=WORDS_PATH):
    with open(path) as f:
        return f.read().split()

def GUESSES(path=GUESSES_PATH):
    with open(path) as f:
        return f.read().split()
    
def WORDCHOICE(words):
    return random.choice(words)

def CALCULATE(user, word):
    result = [0] * 5
    duplicate = list(word)

    for i in range(5):
        if user[i] == word[i]:
            result[i] = 2
            duplicate[i] = None

    for i in range(5):
        if user[i] in duplicate and result[i] == 0:
            result[i] = 1
            duplicate[duplicate.index(user[i])] = None
    return result