from sys import argv

script, filename = argv

txt = open(filename)

print "\nYour file: %r" % filename
print txt.read() + "\n"

txt.close()
