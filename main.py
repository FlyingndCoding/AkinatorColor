

#Imports all libraries needed in program
import time
import sys

#Restarts game
def restart():
	answer = [] #empty list of answers
	intro()
	game()
	scoring()
	results()
	outro()

#All the introductory text at the start of the game, describes how the game will work
def intro():
	start = "Welcome to the color Akinator! Think of a color! Try to think of a SIMPLE, one worded color(NOT baby blue, sea green, etc.)."
	waiting = "-Waiting; do not type color below, just think of one-"
	tip = 'Answer the questions with 1 for Yes or 2 for No.'
	begin = "Ready? Here's the first question."
	for i in start: #makes text appear letter by letter
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.05)
	print ('')
	for i in waiting: #makes text appear letter by letter
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(5.0)
	print ('')
	for i in tip: #makes text appear letter by letter
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.05)
	print ('')
	for i in begin: #makes text appear letter by letter
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(1.0)
	print('')

#The actual game; asks the user questions about their color
def game():
	not_used = ['Is your color a primary color of light?', 'Is your color a primary color of pigment?', 'Can you find your color in the sky?', 'Is your color metallic?', 'Is your color on the American Flag?', 'Does your color absorb OR reflect ALL light as a pigment?', 'Is your color one of Ayala’s school colors?', 'Is your color one of Ayala’s current class colors?', 'Does your color begin with a ‘b’?', 'Does your color end in a vowel?', 'Does your color end in a consonant?', 'Is this color in the rainbow?', 'Are trees your color in the fall?', 'Is your color monochrome?(including silver)', 'Is your color a cool color?', 'Does your color start with a g?', "Is your color associated with Valentine's day?(Red, Purple, Pink, White, Magenta, etc.)"]
	for question in not_used: #cycles through all the questions
		for i in question: #makes text appear letter by letter
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.05)
		print ('')
		reply = int(input('Answer: '))
		if reply == 1: #accepts 1 as an answer
			answer.append(reply)
		elif reply == 2: #accepts 2 as an answer
			answer.append(reply)
		else: #does not accept any other integer
			print ('Please answer with 1 or 2!')
			reply = input('Answer: ')
		print('')

#Compares the user's results with the computer's knowledge
def results():
	if answer == red:
		print ("We guess your color is red.") 
	elif answer == orange:
		print ("We guess your color is orange.")
	elif answer == yellow:
		print ("We guess your color is yellow.")
	elif answer == green:
		print ("We guess your color is green.")
	elif answer == blue:
		print ("We guess your color is blue.")
	elif answer == purple:
		print ("We guess your color is purple.")
	elif answer == pink:
		print ("We guess your color is pink.")
	elif answer == brown:
		print ("We guess your color is brown.")
	elif answer == black:
		print ("We guess your color is black.")
	elif answer == white:
		print ("We guess your color is white.")
	elif answer == grey:
		print ("We guess your color is grey.")
	elif answer == silver:
		print ("We guess your color is silver.")
	elif answer == gold:
		print ("We guess your color is gold.")
	elif answer == magenta:
		print ("We guess your color is magenta.")
	else: #If the answer list does not match ANY of the colors
		print ("Your color is too hard or doesnt even exist. We couldn't guess it. Play again!")

#A warm goodbye to the user who played the game❤; gives user the oppurtunity to restart the game
def outro():
	thanks = "Thank you for playing our game! We hope you enjoyed it! ❤"
	repeat = "Want to play again?"
	bye = "Goodbye!! Come again soon!"
	for i in thanks: #makes text appear letter by letter
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.05)
	print ('')
	for i in repeat: #makes text appear letter by letter, asks user if they would like to play again
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.05)
	print('')
	decision = input('Answer: ')
	if decision == 1:
		restart() #restarts game
	else:
		print('')
		for i in bye: #makes text appear letter by letter
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.05)
		sys.exit() #ends program
	
		
#MAIN	
#initialize variables
red = [1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1] 
orange = [2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2]
yellow = [2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2]
green = [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2]
blue = [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2]
purple = [2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1]
pink = [2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1]
brown = [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2]
black = [2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2]
white = [2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1]
grey = [2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2]
silver = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
gold = [2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2]
magenta = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]  
answer = []

#begin program
intro()
game()
results()
outro()