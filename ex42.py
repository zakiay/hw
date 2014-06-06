class Model(object):
	def __init__(self, n):
		self.n = n

class Dog(object):
	def __init__(self, n):
		self.n = n

class Human(Model):
	def __init__(self, n):
		self.n = n

d = Dog(4)
h = Human(2)

print "d: %r" % d.n
print "h: %r" % h.n