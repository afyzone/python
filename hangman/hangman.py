import os
import sys
import getpass
import requests
import random

from colorama import init, Fore

init()

responsetext = requests.get('https://raw.githubusercontent.com/afyzone/python/main/hangman/dependencies/worldlist.txt').text.split('\n')
theword = random.choice(responsetext)
underscore_word = ""
lives = 7

alreadyguessedletter = {}

def start():
    print(Fore.CYAN + '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

    ''')
    guessquestion()

def win():
    os.system('cls')
    lifecheck()
    getpass.getpass(Fore.GREEN + 'The word was ' + theword + '. You win! Press Enter to close')
    sys.exit()

def currentword():
    global underscore_word

    underscore_word = ""

    for char in theword:
        if char in alreadyguessedletter:
            underscore_word += char
        else:
            underscore_word += '_'

    print(Fore.MAGENTA + "Current Guessed Word: " + underscore_word)
    
    if underscore_word == theword:
        win()

def lifecheck():
    if lives == 7:
        print('''
_ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========
        ''')
    elif lives == 6:
        print('''
_ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========
        ''')
    elif lives == 5:
        print('''
_ _ _ _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
        ''')
    elif lives == 4:
        print('''
_ _ _ _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
        ''')
    elif lives == 3:
        print('''
_ _ _ _

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
        ''')
    elif lives == 2:
        print('''
_ _ _ _

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
        ''')
    elif lives == 1:
        os.system('cls')
        print('''
You lose.
_ _ _ _

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    ''')
        getpass.getpass('You have lost. The word was ' + theword + '. Press Enter to close.')
        sys.exit()

def guessesupdate(letter):
    if not (len(letter) == 1 and letter.isalpha()): 
        os.system('cls')
        lifecheck()
        print(Fore.YELLOW + "Please enter a single letter.")
        guessquestion()

    if letter in alreadyguessedletter:
        os.system('cls')
        lifecheck()
        print(Fore.BLUE + 'You have already guessed ' + letter + ' letter.')
        guessquestion()
    else:
        alreadyguessedletter[letter] = True

def guessquestion():
    currentword()
    global lives
    guess = input(Fore.LIGHTWHITE_EX + 'Guess a letter: ').lower()
    guessesupdate(guess)

    if guess in theword:
        os.system('cls')
        lifecheck()
        print(Fore.GREEN + "You guessed " + guess + ", that's a letter in the word.")
        guessquestion()

    else:
        if not lives == 1: os.system('cls')
        lives = lives - 1
        lifecheck()
        print(Fore.RED + "You guessed " + guess + ", that's not in the word. You lose a life.")
        guessquestion()

start()
