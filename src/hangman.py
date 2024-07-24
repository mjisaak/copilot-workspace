import random

words = ["python", "hangman", "challenge", "programming", "openai"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return stages[6 - attempts]

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print(display_hangman(attempts))
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")

    if attempts == 0:
        print(display_hangman(attempts))
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_game()
