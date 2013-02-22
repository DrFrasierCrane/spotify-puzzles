# Start the tool and check for inputs less than or equal to zero.
def start(num):	
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive integer!"
	else:
		convert(num)
		


def convert(input):
	global binlist
	binlist = []
	
	while input > 0:
		binlist.append(input % 2)
		input = input / 2
	
	binlist.reverse()
	new = []
	
	for i in range(len(binlist)):
		new.append(binlist[i] * 2 ** i)
	
	print sum(new)


num = int(raw_input())


start(num)