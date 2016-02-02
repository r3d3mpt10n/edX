def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return set(secretWord) <= set(lettersGuessed)

def guessedWord(secretWord, lettersGuessed):
    for i in lettersGuessed:
        if i not in lettersGuessed:
            secretWord = secretWord.replace(i," _ ")
    return(secretWord)

def getAvailableLetters(lettersGuessed):
    avail = "abcdefghijklmnopqrstuvwxyz"
    for i in lettersGuessed:
        avail = avail.replace(i, "")
    return(avail)


def hangman(secretWord):

    remain_guess = 8
    lettersGuessed = []
    print("Let's play hangman!")
    print("I'm thinking of a word that is %s letters long." % (len(secretWord)))

    while remain_guess >= 0:

        print("-------------")
        if isWordGuessed(secretWord, lettersGuessed):
            remain_guess = -1
            print("Congratulations, you nailed it!")
        elif remain_guess == 0:
            remain_guess = -1
            print("Sorry, you ran out of guesses. The word was %s." % (secretWord))
        else:
            print("You have %s guesses left." % (remain_guess))
            print("Available letters: %s" % (getAvailableLetters(lettersGuessed)))
            guess = raw_input("Please guess a letter: ")
            guess = guess.lower()
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: %s" % (getGuessedWord(secretWord, lettersGuessed)))
            elif guess in secretWord:
                lettersGuessed.append(guess)
                print("Good guess: %s" % (getGuessedWord(secretWord, lettersGuessed)))
            else:
                lettersGuessed.append(guess)
                remain_guess -= 1
                print("Oops! That letter is not in my word: %s" % (getGuessedWord(secretWord, lettersGuessed)))



secretWord = chooseWord(wordlist).lower()
a = "a"
hangman(a, secretWord)

secretWord = "apple"
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(guessedWord(secretWord, lettersGuessed))
print(getAvailableLetters(lettersGuessed))