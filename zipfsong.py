## Code written by Tyler Sartin 20 February 2013 ##
from operator import itemgetter

[n, m] = map(int, raw_input().split())

frequencies = []
track_names = []

## For all tracks, split titles and frequencies.
for i in range(n):
	item = raw_input().split()
	frequencies.append(item[0])
	track_names.append(item[1])


frequencies = map(int, frequencies)

## Create three lists, fis is a list of the frequencies, zis is list of the Zipf values
## and qis is a list of qualities.
## zi = 1 / 1 + i
## qi = fi / zi

zipfs = []
qualities = []
for i in range(n):
	zipfs.append(1 / (1.0 + i))


for i in range(n):
	qualities.append(frequencies[i] / zipfs[i])


trk_qual = {}

for i in range(n):
	trk_qual[track_names[i]] = qualities[i]


output = sorted(trk_qual.iteritems(), key=itemgetter(1))
output.reverse()

for i in range(m):
	print output[i][0]
