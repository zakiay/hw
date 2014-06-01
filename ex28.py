out = open("ex28_sample.txt", 'w')
s = ""

for i in range(1, 21):
	s =  "%d. \n" % i
	out.write(s)

out.close()