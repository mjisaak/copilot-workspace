import random

def select_random_word():
    words = [
        "elephant", "giraffe", "hippopotamus", "kangaroo", "alligator",
        "crocodile", "chimpanzee", "dolphin", "flamingo", "gorilla",
        "jaguar", "koala", "leopard", "meerkat", "ostrich",
        "panda", "penguin", "rhinoceros", "squirrel", "tiger"
    ]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    hangman_stages = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]

    while incorrect_guesses < max_incorrect_guesses:
        print(hangman_stages[incorrect_guesses])
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            guessed_letters.append(guess)
            incorrect_guesses += 1

    if incorrect_guesses == max_incorrect_guesses:
        print(hangman_stages[incorrect_guesses])
        print("Game over! The word was:", word)

if __name__ == "__main__":
    hangman()
