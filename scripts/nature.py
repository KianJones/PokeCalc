
ifile = open("natures.txt", "r")
ofile = open("nat.txt", "w")
x = ifile.tell()

numlines = 0

for line in ifile.readlines():
    numlines += 1
    
ifile.seek(x)
a = []

for line in ifile.readlines():
    a.append(line.split(',')[1])
    
ifile.seek(x)

b = []
for line in ifile.readlines():
    b.append(line.split(',')[2:4])
    
for i in range(0, len(b)-1):
    b[i][0] = int(b[i][0])
    b[i][1] = int(b[i][1])
    
c = dict(zip(a,b))
print c



ifile.close()
ofile.close()