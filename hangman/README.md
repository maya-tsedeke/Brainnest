
# Hangman Game

A brief description of what this project does and who it's for

'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

## Expected Output
```bash
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
''
```
### This is a Python implementation of the classic word guessing game, Hangman.
### How to Play

    * The game will randomly choose a word from the word list: ['python', 'java', 'kotlin', 'javascript'].
    * The player has to guess the letters that make up the word.
    * The player is allowed a maximum of 6 wrong guesses.
    * The game ends when the player guesses the word or runs out of tries.
### Usage
* To play the game, simply run the hangman() function in the Python interpreter or in a Python script.
## Proposed Output
```bash

    You have 6 tries left.
    Used letters: 
    Word: _ _ _ _ _ _

    Guess a letter: p
    You have 6 tries left.
    Used letters: p
    Word: p _ _ _ _ _

    Guess a letter: y
    You have 6 tries left.
    Used letters: y p
    Word: p y _ _ _ _

    Guess a letter: t
    You have 6 tries left.
    Used letters: t y p
    Word: p y t _ _ _

    Guess a letter: h
    You have 6 tries left.
    Used letters: h t y p
    Word: p y t h _ _

    Guess a letter: n
    You have 6 tries left.
    Used letters: h t y n p
    Word: p y t h _ n

    Guess a letter: o
    Congratulations! You guessed the word python !
```
   # If you have any improvement you are welcome!!
   # Broject from Brainnest company
   # Developed by : Tsedeke T