from sys import argv

script, uname, foo = argv
p = '> '

print "Hi, " + uname + "! I'm " + script
print "Like me? %rl" % foo
like = raw_input(p)

print "What's your laptop?"
comp = raw_input(p)

print """
So, %r, you said %r about liking me. 
You have a(n) %r computer.
""" % (uname, like, comp)