people = 20
cats = 30
dogs = 15

print "p: ", people
print "c: ", cats
print "d: ", dogs 

if people < cats:
	print "p < c"
if people > cats:
	print "p > c."
if people < dogs:
	print "p < d"
if people > dogs:
	print "p > d"

dogs += 5

print
print "d: ", dogs

if people >= dogs:
	print "p >= d"
if people <= dogs:
	print "p <= d"

if people == dogs:
	print "p == d"

if True:
	print "\nTrue\n"