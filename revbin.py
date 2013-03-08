## Code written by Tyler Sartin on 18 February 2013.
## Start the tool and check for inputs less than or equal to zero.

def start(num):
	'''Takes in a positive integer and does a check
	INPUT: Positive decimal integer
	OUTPUT: None carries user to convert()'''
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive integer!"
	else:
		convert(num)
		


def convert(input):
	'''Takes the verified input and converts decimal to reverse binary
	INPUT: Positive decimal integer
	OUTPUT: Reversed binary equivalent'''
	binlist = []
	
	while input > 0:
		binlist.insert(0, input % 2)
		input /= 2
	
	new = []
	
	for i in range(len(binlist)):
		new.append(binlist[i] * 2 ** i)
	
	print sum(new)


start(int(raw_input()))