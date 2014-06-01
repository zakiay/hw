from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

n = raw_input("Say something")

print "First you say %s then you say %s?!" % (script, n)