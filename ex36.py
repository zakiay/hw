from sys import exit

def first():
	print "Room #1"
	print "Go to room 2 or 4"

	next = raw_input('> ')

	if next == "2":
		print "Going to room #2..."
		second()
	elif next == "4":
		print "Going to room #4..."
		fourth()
	elif next == "5": # easter egg
		print "Easter egg..."
		egg()
	else:
		dead("You can't follow instructions...")

def second():
	print "Room #2"
	dead("I'm tired of writing this game...")

def third():
	print "Room #3"
	dead("I'm tired of writing this game...")

def fourth():
	print "Room #4"
	dead("I'm tired of writing this game...")

def egg():
	print "## Secret room ##"
	dead("I'm tired of writing this game... But you are cool...")

def dead(s):
	print "You died because: ", s
	exit(0)

def go():
	print "Welcome, go to room #1..."
	first()

go()
