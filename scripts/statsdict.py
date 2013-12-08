ifile = open('pokemonstats.txt', 'rb')

#Creates a file pointer to the beginning of the file
x = ifile.tell()

# Generates the number of lines in the file
lines = 0
for i in ifile.readlines():
	lines+=1
    
lines -= 59*6
lines2 = lines + 60*6

#Moves the file pointer back to the beginning
ifile.seek(x)

# creates a list of the stat values
b = []
for line in ifile.readlines():
	b.append(line.split(',')[2])
	
#print b

# by proxy, makes a list of the pokemon ids
d = [x for x in range(1,(lines/6)+1)]
h = [i for i in range(10001,10061)]
#for i in range(10001,10061):
    

#print d

# generates a list of stat values for individual pokemon by taking every sixth 
# element in the b list, which contains the stat values
f = []
count = 0
for i in range(1,lines/6):
	f.append(b[count:count+6])
	count+=6

#print f
j = []
for i in range(lines/6, lines2/6):
    j.append(b[count:count+6])
    count+=6

# the final pokemon id -> stats list dict
g = dict(zip(d,f))
k = dict(zip(h,j))

for i in range(1,len(g)+1):
	print ("%d :" % i), g[i], ','

for i in range(10001,10061):
	print ("%d :" % i), k[i], ','


ifile.close()