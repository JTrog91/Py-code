import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+ 
  O   |
 /|   |
      |
     ===''', '''
  +---+ 
  O   |
 /|\  |
      |
     ===''', '''
  +---+ 
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+ 
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+ 
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+ 
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Colors':'red orange yellow green blue purple indigo violet white black brown'.split(),
'Shapes':'squair triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split()
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split()
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish goat leech mouse otter python squid tiger'.split()}

def getRandomWord(wordDict):
    #Function returns a random string from the passed dictionary list of strings and its key.
    #First randomly select a key from the dictionary. 
    wordKey = random.choice(list(wordDict.keys()))
   
    #Second randomly select a word from the keys list in the dictionary.
    wordIndex = random.randint(0, len(wordDict[wordKey]))
    
    return [wordDict [wordkey] [wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  #Replaces blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  #Show the secret word with spaces.
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    #Returns the letter entered by the player and makes sure the player entered a single letter and not something else.
    while True:
        guess = input('Guess a letter.')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Guess again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER.')
        else:
            return guess


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = ''
while difficulty not in 'EMH':
    print('Enter difficulty: E-Easy, M-Medium, H-Hard.')
    difficulty= input().upper()
    if difficulty == 'M'
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    if difficulty == 'H'
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]
    
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False
while True:
    print('The secret word is in the set:' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if player won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is"' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

    # Check if player has guessed too many times and lost.
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
              str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
        gameIsDone = True

    # Ask if the player wants to play again.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
