f = open('pokemon.txt')
of = open('pokenames.txt', 'w')
x = f.tell()

numLines = 0

for line in f.readlines():
    numLines += 1

f.seek(x)

a = []
for line in f.readlines():
    a.append(int(line.split(',')[0]))

f.seek(x)

b = []
for line in f.readlines():
    b.append(line.split(',')[1])

c = dict(zip(a, b))

for i in range(1, 719):
    of.write(("'%s' : %d,\n" % (c[i], i)))
    #print ("'%s' : %d,\n" %(c[i], i))

for i in range(10001, 10061):
    of.write(("'%s' : %d,\n" % (c[i], i)))
    #print ("'%s' : %d,\n" %(c[i], i))


f.close()
of.close()

#order of items in pokemon.txt
#id,identifier,generation_id,evolves_from_species_id,evolution_chain_id
#,color_id,shape_id,habitat_id,gender_rate,capture_rate,base_happiness,
#is_baby,hatch_counter,has_gender_differences,growth_rate_id,forms_switchable,
#order,conquest_order
