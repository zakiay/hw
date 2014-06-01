from sys import argv

script, filename = argv

print "Erasing %r..." % filename
print "Ctrl-C to cancel, <Enter> to continue..."

raw_input(">")

print "Opening %r for deletion..." % filename
target = open(filename, 'w')

print "Deleting..."
target.truncate()

print "Please write two new lines."
line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")

print "Writing..."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

print "Closing..."
target.close()