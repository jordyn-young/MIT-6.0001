# Problem Set 2, hangman.py
# Name: Jordyn Young
# Collaborators: N/A
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

# OPEN PROPER DIRECTORY:
    # cd /Users/jordynyoung/Documents/Programming/Python/MIT 6.0001/ps2

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for e  in letters_guessed:
        if e not in secret_word:
            letters_guessed.remove(e)
    return sorted(set(secret_word)) == sorted(letters_guessed)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_secret_word = list(secret_word) # makes list out of letters in secret_word
    word = [] # creating empty list for the "return"
    
    for letter in letters_secret_word:
        if letter not in letters_guessed:
            word.append("_ ")
        else:
            word.append(letter)   
    return ''.join(word)

# =============================================================================
## FANCY VERSION OF GET_GUESSED_WORD THAT TREVOR WROTE ##
# def get_guessed_word2(secret_word, letters_guessed):
#     return ''.join(
#         letter if letter in letters_guessed else '_ '
#         for letter in secret_word)
# =============================================================================

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase)
    
    for letter in all_letters:
        if letter in letters_guessed:
            all_letters.remove(letter)
    return ''.join(all_letters)

    
wordlist = load_words()
secret_word = choose_word(wordlist) # choose secret word

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = [] # creates empty list

    
    num_guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("_ " * len(secret_word))
    
    while num_guesses > 0:
        print("You have",num_guesses,"guesses left.")
        print("Available letters:",''.join(get_available_letters(letters_guessed)))
        next_guess = input("What letter do you guess next?: ").lower()
        
        if len(next_guess) > 1:
            input("Please guess only ONE letter: ")
        elif next_guess not in string.ascii_lowercase:
            if warnings !=0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, " warnings left.")
            else:
                num_guesses -= 1
                print("Oops! That is not a valid letter. You have 0 warnings left, so you lost 1 guess.")
        elif next_guess in letters_guessed:
            if warnings !=0:
                warnings -= 1
                print("Oops! You already guessed that letter. You have", warnings, " warnings left.")
            else:
                num_guesses -= 1
                print("Oops! You already guessed that letter. You have 0 warnings left, so you lost 1 guess.")
        elif next_guess not in secret_word:
            letters_guessed.append(next_guess)
            if next_guess in vowels:
                num_guesses -= 2
            else:
                num_guesses -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(next_guess)
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("Congratulations, you won! The secret word was ", secret_word)
                unique_letters_secret_word = len(set(secret_word))
                print("Your total score for this game is: ", num_guesses*unique_letters_secret_word)
                break
            else:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        
        print("-" * 11)
    
    if num_guesses == 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("Sorry, you ran out of guesses. The word was",secret_word,".")
    
    return
    
                

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


# =============================================================================
# VARIABLES NEEDED FOR:
# match_with_gaps(my_word, other_word) and show_possible_matches(my_word)
# already embedded in hangman_with_hints(secret_word)
    # my_word = get_guessed_word(secret_word, letters_guessed)
    # other_word = secret_word
# =============================================================================

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''    
    my_word = my_word.replace(" ", "")
    
    if len(my_word) != len(other_word):
        return False
    else:
        i = len(my_word) - 1
        while i >= 0:
            if my_word[i] == other_word[i]:
                match = True
            elif my_word[i] == '_' and other_word[i] not in my_word:
                match = True
            else:
                match = False
                break
            i -= 1
        return match


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    word_list = line.split()
    
    possible_words = []
    
    for word in word_list:
        if match_with_gaps(my_word, word):
            possible_words.append(word)

    if possible_words == []:
        print('No matches found')
    else:
        print(' '.join(possible_words))
    
    return possible_words

def possible_matches_letters_not_guessed(possible_words, letters_guessed, my_word, secret_word):
    '''
    possible_words: output of show_possible_matches(my_word)
    letters_guessed: letters guessed in the hangman game thus far
    guessed_word_so_far: output of get_guessed_word(secret_word, letters_guessed)
    returns: list of possible words that do not contain letters already 
    guessed in place of " - "

    ''' 
    possible_words_hint = []
    
    for word in possible_words:
        i = len(word) - 1
        while i >= 0:
            if possible_words[i] not in letters_guessed and my_word[i] == '_ ':
                match = True
                i -=1
            else:
                match = False
                break
    if match == True:
        possible_words_hint.append(word)
    
    return possible_words_hint

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = [] # creates empty list
    
    num_guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("_ " * len(secret_word))
    
    while num_guesses > 0:
        print("You have",num_guesses,"guesses left.")
        letters_left = get_available_letters(letters_guessed)
        print("Available letters:",''.join(letters_left))
        next_guess = input("What letter do you guess next?: ").lower()
        
        if len(next_guess) > 1:
            print("Please guess only ONE letter: ")
        elif next_guess not in string.ascii_lowercase:
            if next_guess == '*':
                my_word = get_guessed_word(secret_word, letters_guessed)
                other_word = secret_word
                possible_words = show_possible_matches(my_word)
                for word in possible_words:
                    i = len(word) - 1
                    while i >= 0:
                        if word[i] not in letters_guessed and my_word[i] == '_ ':
                            pass
                        else:
                            possible_words.remove(word)                
                print('Possible word matches are:')
                print(' '.join(possible_words))
            elif warnings !=0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, " warnings left.")
            else:
                num_guesses -= 1
                print("Oops! That is not a valid letter. You have 0 warnings left, so you lost 1 guess.")
        elif next_guess in letters_guessed:
            if warnings !=0:
                warnings -= 1
                print("Oops! You already guessed that letter. You have", warnings, " warnings left.")
            else:
                num_guesses -= 1
                print("Oops! You already guessed that letter. You have 0 warnings left, so you lost 1 guess.")
        elif next_guess not in secret_word:
            letters_guessed.append(next_guess)
            if next_guess in vowels:
                num_guesses -= 2
            else:
                num_guesses -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(next_guess)
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("Congratulations, you won! The secret word was ", secret_word)
                unique_letters_secret_word = len(set(secret_word))
                print("Your total score for this game is: ", num_guesses*unique_letters_secret_word)
                break
            else:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        
        print("-" * 11)
    
    if num_guesses == 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("Sorry, you ran out of guesses. The word was",secret_word,".")
    
    return



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)

