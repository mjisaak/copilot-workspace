import random

def display_game_state(word, guessed_letters, attempts_left):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {display_word}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")
    print_hangman(attempts_left)

def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def check_loss(attempts_left):
    return attempts_left <= 0

def get_user_input():
    return input("Guess a letter: ").lower()

def print_hangman(attempts_left):
    stages = [
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
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
          |   |
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
              |
              |
              |
              |
        =========
        """
    ]
    print(stages[6 - attempts_left])

def hangman():
    words = ["python", "hangman", "challenge", "programming", "code"]
    word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    while True:
        display_game_state(word, guessed_letters, attempts_left)
        guess = get_user_input()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts_left -= 1

        if check_win(word, guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break

        if check_loss(attempts_left):
            print(f"Game over! The word was: {word}")
            break

if __name__ == "__main__":
    hangman()
