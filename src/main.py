import random
import sys
from ascii_art import *

words = ["blauwal", "meerschweinchen", "hai", "delfin", "kabeljau"]
letters_guessed = []
word_accepted = False
finished = False
random_word = None
letters_already_guessed = []
letterAlreadyGuessed = False
letterGuessed = False
letterFound = False


def welcome_script():  # The welcome script that starts the game.
    print("""Hey, Welcome to my Hangman Game!
Cool to hear that you found it, wanna start?
If you see any problems, feel free to open a new issue on GitHub or type "info" for more""")
    user_in = input("(y/n/info)")
    if user_in == "y" or user_in == "Y":
        start_game()
    elif user_in == "n" or user_in == "N":
        sys.exit()
    elif user_in == "info" or user_in == "Info":
        print("""This is my first ASCII-Art Game.
'iicsaevoli' epyt
It's a bit of a clone of the popular "Hangman"-Game
!sneppah tahw ees dna
You can find my GitHub-Repo by searching for 'KaptainAhoibrause/AsciiHangman'
Enjoy!""")
        welcome_script()
    elif user_in == "iloveascii":
        print(line_one)
        print(line_two_1)
        print(line_two_2)
        print(line_three)
        print(line_four)
        print("These are my first ASCII Arts for this game :^)")
        welcome_script()
    else:
        welcome_script()


def start_game():  # The initial start of the game.
    global word_accepted, random_word, finished, letterAlreadyGuessed, \
        letterGuessed, letters_already_guessed, letterFound
    while not word_accepted:  # Asking if the words length is ok
        random_word = words[random.randint(0, len(words)) - 1]
        print("""Are you okay with a word that is""", len(random_word), """letters long?""")
        user_in = input("(y/n)")
        if user_in == "y" or user_in == "Y":
            word_accepted = True

    while not finished:  # Main loop for the game
        print("""Alright, try to guess a letter. (Don't use capital letters)""")
        user_in = input(">")
        for x in range(0, len(letters_already_guessed)):  # Checking if the the latter was already guessed and...
            if user_in == letters_already_guessed[x]:
                print("""You already guessed that letter.""")
                letterAlreadyGuessed = True
        if not letterAlreadyGuessed:  # ...if not, it will continue.
            letters_already_guessed.append(user_in)
            for x in range(0, len(random_word)):  # checking if the letter is found in the word.
                if random_word[x] == user_in:
                    letterGuessed = True
                    letters_guessed.append(x)
            if not letterGuessed:  # say this if the letter wasn't found in the word.
                print("""Sorry this is the wrong letter.""")
            print("""Your word now looks like this:""")  # giving the letters you guessed.
            for x in range(0, len(random_word)):
                for y in range(0, len(letters_guessed)):
                    if random_word[x] == random_word[letters_guessed[y]]:
                        print("""You found letter no""", x + 1,
                              """which is""", random_word[x])
                        letterFound = True
                        break
                if not letterFound:
                    print("You didn't found letter number", x + 1)
                letterFound = False
            if len(letters_guessed) > len(random_word) - 1:  # giving congrats if you won the game.
                print("""You won the Games and guessed the word:""", random_word, """
Congrats!!""")
                finished = True
            letterGuessed = False
            letterFound = False
        else:  # cleaning stuff if the letter was already guessed.
            letterAlreadyGuessed = False


if __name__ == '__main__':
    welcome_script()
