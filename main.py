import random

print("Welcome to Guessing Game! \n")


def random_word():
    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    return random.choice(words)
def word_status(word,guessed_letters):
    display = ""
    for char in word:
        if char in guessed_letters:
            display += char
        else:
            display += "_"
    return display       

def word_guessing_game():
    secret_word = random_word()
    turns = 12
    guesses = []
    print("Secret Word: ",word_status(secret_word,guesses))
    while turns > 0:
        guess = input("Guess letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print('You must enter a single letter')
            continue
        if guess in guesses:
            print("You already guessed that letter")
            continue
        guesses.append(guess)
        if guess not in secret_word:
            print(f"Letter {guess} is not in the word")
            print(f"You have {turns} number of turns left")
            turns -= 1
        else:
            occurences = secret_word.count(guess)
            print(f"The letter {guess} is {occurences} times in the word")
        current_status = word_status(secret_word,guesses)
        print("Secret Word:",current_status)
        if current_status == secret_word:
            print(f"\nCongratulations!\nYou guessed the word \nThe word is: {current_status}")
            break

word_guessing_game()