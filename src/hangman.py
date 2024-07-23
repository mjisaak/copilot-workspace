import random

def select_random_word():
    words = ["elephant", "giraffe", "kangaroo", "dolphin", "penguin"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def handle_user_input():
    return input("Guess a letter: ").lower()

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[attempts]

def main():
    word = select_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_current_state(word, guessed_letters))
    print(display_hangman(attempts))

    while attempts > 0:
        guess = handle_user_input()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess. Attempts left:", attempts)

        current_state = display_current_state(word, guessed_letters)
        print(current_state)
        print(display_hangman(attempts))

        if "_" not in current_state:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Game over. The word was:", word)

if __name__ == "__main__":
    main()
