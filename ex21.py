def add(a, b):
	print a, " + ", b
	return a + b
def sub(a, b):
	print a, " - ", b
	return a - b
def mul(a, b):
	print a, " * ", b
	return a * b
def div(a, b):
	print a, " / ", b
	return a / b

a = add(54, 41)
b = sub(32, 3)
c = mul(44, 22)
d = div(202.0, 54.0)

print
print a
print b
print c
print d

n = add(a, sub(b, mul(c, (div(d, 5.0)))))
print
print n
print

def puzzle(a, b, c, d, i):
	return a + (i/5.0) * c - b

print puzzle(a, b, c, d, 5)