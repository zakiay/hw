the_count = [1, 2, 3, 4, 5]
fruits = ['apple','orange','banana','carrot']
change = [1, 'penny', 'dime', 3, 'quarter']

for number in the_count:
	print "Count #%d" % number

for fruit in fruits:
	print "Fruit: %s" % fruit

for i in change:
	print "I got %r" % i

elements = []

for i in range(0, 6):
	print "Adding %d to the list..." % i
	elements.append(i)

for i in elements:
	print "Element #%d" % i

odd = []
for i in range(1, 100, 2):
	odd.append(i)
	print "Added %d..." % i