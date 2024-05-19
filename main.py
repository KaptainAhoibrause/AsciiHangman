import random
import sys
import ascii_art

words = ["blauwal", "meerschweinchen", "hai", "delfin", "kabeljau"]
letters_guessed = []
word_accepted = False
finished = False
random_word = None
letters_already_guessed = []
letterAlreadyGuessed = None
letterGuessed = False


def welcome_script():  # The welcome script that starts the game.
    print("""Hey, Welcome to my Hangman Game!
    Cool to hear that you found it, wanna start?
    If you see any problems, feel free to open a new issue on GitHub or type "info" for more""")
    user_in = input("(y/n)")
    if user_in == "y" or user_in == "Y":
        start_game()
    elif user_in == "n" or user_in == "N":
        sys.exit()
    elif user_in == "info" or user_in == "Info":
        print("")
    else:
        welcome_script()


def start_game():  # The initial start of the game.
    global word_accepted, random_word, finished, letterAlreadyGuessed, letterGuessed, letters_already_guessed
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
            if len(letters_guessed) > 0:  # giving the letters you guessed.
                print("""Your word now looks like this:""")
                for x in range(0, len(letters_guessed)):
                    print("""You guessed letter no""", letters_guessed[x] + 1,
                          """which is""", random_word[letters_guessed[x]])
            if len(letters_guessed) > len(random_word) - 1:  # giving congrats if you won the game.
                print("""You won the Games and guessed the word:""", random_word, """
Congrats!!""")
                letterGuessed = False
                finished = True
        else:  # cleaning stuff if the letter was already guessed.
            letterAlreadyGuessed = False


if __name__ == '__main__':
    welcome_script()
