import random
import time

# This is a comment. It's a single line that starts with a # sign.

# The input method accepts a prompt string directly in between the parenthesis. It'll help later on.
# This try/catch statement is another great tool. See if you understand what we're doing here.
try:
    guess = input('I will flip a coin 1000 times. Guess how many times it will come up heads. (press enter to begin): ')
except:
    raise ValueError('Sorry, I didnt understand your response. Please input a number.')

flips=0
heads=0

while flips < 1000:
   if random.randint(0,1) == 1:
       heads = heads + 1
   flips = flips + 1
   
   if flips == 900:
      print('900 flips and there have been ' + str(heads) + ' heads ')
      time.sleep(2)

   if flips == 100:
      print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
      time.sleep(2)

   if flips == 500:
      print('Halfway done and heads has come up ' + str(heads) + ' times.')
      time.sleep(2)
   
print('\n')
print('Out of 1000 coin tosses. Heads came up ' + str(heads) + ' times!')

# I thought it would be cool to print out what the person guessed.
print('You guessed: {0}'.format(guess))
print('Were you close?')
