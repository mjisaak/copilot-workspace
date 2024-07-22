import random

words = [
    "python", "java", "kotlin", "javascript", "typescript", "swift", "objective", "ruby", "perl", "haskell",
    "scala", "go", "rust", "dart", "elixir", "clojure", "fsharp", "erlang", "lua", "groovy",
    "matlab", "fortran", "cobol", "pascal", "ada", "vhdl", "verilog", "assembly", "bash", "powershell"
]

def select_word():
    return random.choice(words)

def display_game_state(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_hangman(attempts_left):
    stages = [
        """
           -----
           |   |
               |
               |
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
          /|   |
               |
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
          / \\  |
               |
        --------
        """
    ]
    return stages[6 - attempts_left]

def start_new_game():
    word = select_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")
    print(display_game_state(word, guessed_letters))
    print(display_hangman(attempts_left))

    while attempts_left > 0:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        print(display_game_state(word, guessed_letters))
        print(display_hangman(attempts_left))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    start_new_game()
