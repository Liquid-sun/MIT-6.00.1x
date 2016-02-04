#!/usr/bin/env python


# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    sw = list({ch for ch in secretWord})
    return all(map(lambda x: x in lettersGuessed, sw))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ""
    for ch in secretWord:
        if ch in lettersGuessed:
            s += ch
        else:
            s += "_ "
    return s


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join([ch for ch in string.ascii_lowercase if ch not in lettersGuessed])


def welcome(secretWord):
    '''Print out welcome message and word lenght.'''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secretWord)))


def congrats():
    print("Congratulations, you won!")


def divider():
    print("-------------")


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    welcome(secretWord)

    left_quess = 8
    available_letters = [ch for ch in string.ascii_lowercase]
    mistakesMade = 0
    lettersGuessed = []
    lettersNotGuessed = set()


    while(mistakesMade < 8):
        divider()
        print("You have {} guesses left".format(left_quess - mistakesMade))
        print("Availabale letters: {}".format(''.join(available_letters)))
        
        while True:
            letter = raw_input("Please guess a letter: ").lower()
            if letter in string.ascii_lowercase:
                break

        if letter in lettersGuessed or letter in lettersNotGuessed:
            guessed_word = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You have already guessed that letter: {}".format(guessed_word))
            lettersGuessed.append(letter)
            continue

        if letter not in secretWord:
            mistakesMade += 1
            available_letters = [ch for ch in available_letters if ch != letter]
            guessed_word = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! That letter is not in my word: {}".format(guessed_word))
            lettersNotGuessed.add(letter)

        if letter in secretWord:
            lettersGuessed.append(letter)
            available_letters = [ch for ch in available_letters if ch != letter]
            guessed_word = getGuessedWord(secretWord, lettersGuessed)
            print("Good guess: {}".format(guessed_word))

            if isWordGuessed(secretWord, lettersGuessed):
                divider()
                congrats()
                return
    divider()
    print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
    return


if __name__=="__main__":
    # When you've completed your hangman function, uncomment these two lines
    # and run this file to test! (hint: you might want to pick your own
    # secretWord while you're testing)

    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)

