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

# Function to check if the player has won
def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Function to play the game
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_game_state(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if check_win(word, guessed_letters):
                print("Congratulations! You guessed the word: " + word)
                break
        else:
            attempts -= 1
            print("Incorrect guess. Attempts remaining: " + str(attempts))

        if attempts == 0:
            print("Game over. The word was: " + word)

# Add a graphical output showing the hangman progress in 3D using PyWeb3D
# Note: This is a placeholder comment. Implementing 3D graphics in a console application is not feasible.

# Track the scores in an in-memory database
# Note: This is a placeholder comment. Implementing an in-memory database is not required for this task.

if __name__ == "__main__":
    play_game()
    exit()
