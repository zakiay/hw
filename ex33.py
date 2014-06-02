import time

n = []
length = 15

def dance():
	while True:
		time.sleep(0.06)
		i = 0
		while i < length:
			#print "#%d..." % i
			n.append(i)

			i += 1
			print "n: ", n

		j = length - 1

		while j > 0:
			#print "#%d..." % i
			n.pop(j)

			j -= 1
			print "n: ", n

raw_input('<Enter>...')
print "\n#######\n"

dance()

#for m in n:
#	print m