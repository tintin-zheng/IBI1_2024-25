# What does this piece of code do?
# Answer:Using the computer to creat two random integers (range from 1-6),
# to see whether they are the equal and 
# record the number of attempts.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#defign a varible called progress
progress=0

'''creat a while loop,
	if the progress is larger than or equal to 0,
	the value of progress will add 1
	count the number of attempts
'''
while progress>=0:
	progress+=1

	#creat a randint first_n
	first_n = randint(1,6)
	#creat a randint second_n
	second_n = randint(1,6)
	#judge whether first_n is equall to second_n
	if first_n == second_n:
		#if they are equal, print progress
		print(progress)
		#jump out of the loop (break)
		break

