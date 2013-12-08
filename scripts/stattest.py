#id,stat_id,base_stat,effort
ifile = open('pokemonstats2.txt', 'rb')

#Creates a file pointer to the beginning of the file
x = ifile.tell()

# Generates the number of lines in the file
lines = 0
for i in ifile.readlines():
	lines+=1

#Moves the file pointer back to the beginning
ifile.seek(x)

#The stat_id, not really needed
# a = []
# for line in ifile.readlines():
	# a.append(line.split(',')[1])
	
# print a

# move the pointer back to the beginning
ifile.seek(x)

# creates a list of the stat values
b = []
for line in ifile.readlines():
	b.append(line.split(',')[2])
	
print b


# c = zip(a,b)

# by proxy, makes a list of the pokemon ids
d = [x for x in range(1,(lines/6)+1)]
print d

#count = 0
# e = []
# for i in range(1,lines/6):
	# e.append(c[count:count+6])
	# count+=6	
# print e

# generates a list of stat values for individual pokemon by taking every sixth 
# element in the b list, which contains the stat values
f = []
count = 0
for i in range(1,lines/6):
	f.append(b[count:count+6])
	count+=6

print f

# the final pokemon id -> stats list dict
g = dict(zip(d,f))
print g

ifile.close()