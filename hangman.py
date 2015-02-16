import random
from numpy import matrix
import re

print("Welcome to Hangman and goodluck!")

#Create a list of words from a file, then choose a random word from the list 
#and strip spaces, new lines etc
words = list(open("Dict.txt"))
word = random.choice(words).rstrip()
print word #for testing purposes

answer = []
for i in word:
	answer.append('_')

#use a list to represent the hangman
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

prev_guess = [] #list of previous guesses
incorrect = 0
correct = 0

while(incorrect != 8 and correct < len(word)):
	guess = raw_input("Guess a Letter: ")

	if(guess in word):
		print("That letter is part of the word!")
		for i in re.finditer(guess, word):
			local = i.start()
			#add the letter to the answer list in the same location as the original word
			#local = word.index(guess)
			answer[local] = guess
		print HANGMAN[incorrect]
		print ("%s") % answer
		correct = correct + 1

	elif(not(guess in word)):
		prev_guess.append(guess)
		print("That letter is not part of the word!")
		print ("Used Letters %s") % prev_guess
		print ("***" * 10)
		print HANGMAN[incorrect]
		print ("%s") % answer
		incorrect = incorrect + 1

	else:
		print("Please enter a letter from the alphabet!")

	
