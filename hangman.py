import random
from numpy import matrix
import re

print("Welcome to Hangman and goodluck!")

#Create a list of words from a file, then choose a random word from the list 
#and strip spaces, new lines etc
words = list(open("Dict.txt"))
word = random.choice(words).rstrip().lower()
#print word #for testing purposes

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
ans_str = ''
while(incorrect != 8 and correct < len(word) and not(ans_str==word)):
	guess = raw_input("Guess a Letter: ")

	if(len(guess)>1):
		print "Please enter a single letter!"

	elif(guess.lower() in prev_guess or guess.lower() in answer):
		print "You guessed that letter already!"

	#elif(guess.lower() in answer):
	#	print "You guess that letter already!"

	elif(guess.lower() in word):
		print("That letter is part of the word!")
		for i in re.finditer(guess.lower(), word):
			local = i.start()
			#add the letter to the answer list in the same location as the original word
			answer[local] = guess.lower()
		print HANGMAN[incorrect]
		print ("%s") % answer
		correct = correct + 1
		ans_str = ''.join(answer)

	elif(not(guess.lower() in word)):
		prev_guess.append(guess.lower())
		print("That letter is not part of the word!")
		print ("Used Letters %s") % prev_guess
		print ("***" * 10)
		print HANGMAN[incorrect]
		print ("%s") % answer
		incorrect = incorrect + 1

	else:
		print("Please enter a letter from the alphabet!")
print ("Game Over")

	
