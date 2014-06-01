x = "There are %d types of people." % 10
b = "binary"
d = "don't"
y = "Those who know %s and those who %s" % (b, d)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

h = False
j = "Funny, right? %r"

print j % h

w = "Left..."
e = "...Right"

print w + e