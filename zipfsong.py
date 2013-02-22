## Code written by Tyler Sartin 21 February 2013 ##
from operator import itemgetter

[n, m] = map(int, raw_input().split())

frequencies = []
track_names = []

## For all tracks, split titles and frequencies. Append to separate lists.
for i in range(n):
	item = raw_input().split()
	frequencies.append(item[0])
	track_names.append(item[1])


frequencies = map(long, frequencies)

## Create a list of Zipfs (zi = 1 / i)
## Create a list of the qualities which are fi / zi ==> fi * i

zipfs = range(1, n + 1)
qualities = []

for i in range(n):
	qualities.append(long(frequencies[i] * zipfs[i]))

## Create a tuple with the track names and their qualities. Then sort the tuple
## based on their qualities. Reverse the list for descending order.
trk_qual = zip(track_names, qualities)
output = sorted(trk_qual, key=itemgetter(1), reverse=True)

## Output only the number needed (m)
for i in range(m):
	print output[i][0]