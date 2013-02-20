import collections

## Take initial input of n (number of lines) and m (number of songs for output).
nm = raw_input().split()

## After splitting the input, convert them to integers.
[n, m] = map(int, nm)

## Create new (ordered) dictionary and for all n add to dictionary the name of track: and number
## of plays (fi). The number of plays is changed to integer.
songs = collections.OrderedDict()

## For all tracks, split titles and frequencies. Then add them to the dictionary by putting
## track title first, then frequency.
for i in range(n):
	item = raw_input().split()
	songs[item[1]] = int(item[0])

#print songs
## Create three lists, fis is a list of the frequencies, zis is list of the Zipf values
## and qis is a list of qualities.
## zi = (n - i) / n
## qi = fi / zi

fis = []
for item in songs:
	fis.append(songs[item])


zis = []
qis = []
for i in range(n):
	zis.append(1 / (1.0 + i))
	qis.append(fis[i] / zis[i])


## Replace the frequencies in the songs list with the qualities, qi.
k = 0
for item in songs:
	songs[item] = qis[k]
	k = k + 1

## Sort and reverse the quality list into descending order.
qis = list(set(qis))
qis.sort()
qis.reverse()

##print fis
##print zis
##print qis
##print songs


## This function takes in the output number required, the quality list, and the songs
## list and proceeds to create the output list.
def check(qis, songs):
	for i in range(len(qis)):
		for item in songs:
			if qis[i] == songs[item]:
				output.append(item)
				


global output
output = []

check(qis, songs)

## Print the outputs.
for i in range(m):
	print output[i]
## output1 = list(set(output))	
## print output
