# Copilot-Workspace Demo

## Hangman Game

The Hangman game is a classic word-guessing game. The player tries to guess the word by suggesting letters within a certain number of attempts.

### How to Run the Game

To run the Hangman game, follow these steps:

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the `src` folder in the repository.
4. Run the following command:

```sh
python hangman.py
```

### Example Output

```
Welcome to Hangman!
You have 6 attempts to guess the word.
Current word: _______
Guessed letters: 
Enter a letter: e
Good guess!
Current word: e_e_____
Guessed letters: e
Enter a letter: a
Wrong guess.
You have 5 attempts left.
Current word: e_e_____
Guessed letters: e a
Enter a letter: t
Good guess!
Current word: e_e__t__
Guessed letters: e a t
Enter a letter: r
Wrong guess.
You have 4 attempts left.
Current word: e_e__t__
Guessed letters: e a t r
Enter a letter: n
Good guess!
Current word: e_e__t_n
Guessed letters: e a t r n
Enter a letter: p
Good guess!
Current word: e_e__t_n
Guessed letters: e a t r n p
Enter a letter: h
Good guess!
Current word: e_e_h_t_n
Guessed letters: e a t r n p h
Enter a letter: o
Good guess!
Current word: e_e_h_ton
Guessed letters: e a t r n p h o
Congratulations! You guessed the word: elephant
```

### ASCII Art

```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```
