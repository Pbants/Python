import random
from numpy import matrix

print("Welcome to Hangman and goodluck!")

#read random line from a file containing words
word = random.choice(list(open("Dict.txt")))

for i in len(word):
	answer[i] = "_" #and in the same amount of blanks as the word 

#use a matrix to represent the hangman
man = matrix([['_','_','_'],['_','_','_'],['_','_','_']])
full_man = matrix([["\\",'O','/'],['_','|','_'],['/','_','\\']])


prev_guess = {} #list of previous guesses

while(guesses<7):
	guess = raw_input("Guess a Letter")

	if(guess is contained in word):
		print("That letter is part of the word!")

		#add the letter to the answer list in the same location as the original word
		local = word.index(guess)
		answer[local] = guess

		print ("%s") % answer

	elif(guess is not contained in word):
		print("That letter is not part of the word!")
		prev_guess.append(guess)
		for i in man:
			if man[i] = full_man[i]
				continue
			else if man[i] != full_man[i]:
				man[i] = full_man[i]
		print ("Used Letters %s") % prev_guess
		print ("***" * 10)
		print man
		print ("%s") % answer
	else:
		print("Please enter a letter from the alphabet!")

	guesses++

