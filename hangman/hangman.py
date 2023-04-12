import random

def hangman():
    wordlist = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(wordlist)
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # letters already guessed by the player
    lives = 6  # number of tries left

    # ask the player for a letter until the word is guessed or the player runs out of tries
    while len(word_letters) > 0 and lives > 0:
        # print the current state of the game
        print(f"You have {lives} tries left.")
        print('Used letters:', ' '.join(used_letters))
        current_word = [letter if letter in used_letters else '_' for letter in word]
        print('Word:', ' '.join(current_word))

        # ask the player for a letter
        user_letter = input('Guess a letter: ').lower()

        # check if the letter is valid
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            # if the letter is in the word, remove it from word_letters set
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # game is over, print the result
    if lives == 0:
        print('Sorry, you ran out of tries. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!')
hangman()