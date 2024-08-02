import random

# List of words for the game
words = ["elephant", "giraffe", "hippopotamus", "kangaroo", "koala", "leopard", "lion", "monkey", "panda", "rhinoceros", "tiger", "zebra"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the game
def display_game_state(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("Current word: " + display_word)
    print("Guessed letters: " + " ".join(guessed_letters))

# Function to check if the player has won
def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Function to display the hangman progress
def display_hangman(attempts):
    stages = [
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
    print(stages[6 - attempts])

# Function to play the game
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("You have " + str(attempts) + " attempts to guess the word.")

    while attempts > 0:
        display_hangman(attempts)
        display_game_state(word, guessed_letters)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
            if check_win(word, guessed_letters):
                print("Congratulations! You guessed the word: " + word)
                break
        else:
            print("Wrong guess.")
            attempts -= 1
            guessed_letters.append(guess)
            print("You have " + str(attempts) + " attempts left.")

    if attempts == 0:
        display_hangman(attempts)
        print("Game over. The word was: " + word)

if __name__ == "__main__":
    play_game()
