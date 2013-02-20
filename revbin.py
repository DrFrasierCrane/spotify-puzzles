# Start the tool and check for inputs less than or equal to zero.
def start(num):	
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive integer!"
	else:
		convert(num)
		

# I ain't afraid of no while loops. Create a list and throw in 1s or 0s depending on
# the remainder from dividing by 2. Reverse the list, then create a new list
# containing the calculated decimal numbers. Then sum those decimals up!
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


# Tell people about themselves. (Commented out due to not being read by human.)
#print "\nHello and welcome to the reverse binary calculator!"
#print "This tool will:\n\n\t1) Take an input decimal\n\t2) Convert decimal to binary"
#print "\t3) Reverse the binary number\n\t4) Convert the reversed binary back to decimal\n"

num = int(raw_input())

# Let's start the show boiiiiii!
start(num)