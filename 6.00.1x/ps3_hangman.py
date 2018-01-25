# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME ="words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    z = list(secretWord)
    for letter in lettersGuessed:
        for x in range(z.count(letter)):
            z.remove(letter)
    if z == []:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    z = list(secretWord)
    for letter in z:
        if letter not in lettersGuessed:
            z[z.index(letter)] = '_'
    return ''.join(z)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    z = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in z:
            z.remove(letter)
    return ''.join(z)
    

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ',len(secretWord),' letters long.')
    
    lettersGuessed = []
    initialWord = getGuessedWord(secretWord, lettersGuessed)
    mistakesMade = 0
    availableLetters = string.ascii_lowercase
    while mistakesMade != 8:
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good Work. You got the word right:",secretWord)
            break
        else:
            print('------------')
            print('You have ',8-mistakesMade,'guesses left.')
            print('Available letters:', availableLetters)
            guess = input('Please guess a letter:')
            guessed = guess.lower()
            if guessed in lettersGuessed:
                print("Oops! You've already guessed that letter:", initialWord)
                continue
            else:
                lettersGuessed.append(guessed)
            word = getGuessedWord(secretWord, lettersGuessed)
            availableLetters = getAvailableLetters(lettersGuessed)
            if word == initialWord:
                print('Oops! That letter is not in my word:', word)
                mistakesMade += 1
            else:
                initialWord = word
                print('Good guess:', word)
    print('------------')
    if mistakesMade == 8:
        print('Sorry, you ran out of guesses. The word was ', secretWord,'.')
    else:
        print('Congratulations, you won!')



ch = 'y'
while ch == 'y':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    ch = input('Want to continue? y or n: ')
    print('_______________________________________________')