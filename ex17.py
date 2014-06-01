from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print "Copying %r (%d bytes) to %r (exists? %r)..." % (from_file, len(indata), to_file, exists(to_file))

out_file = open(to_file, 'w').write(indata)
