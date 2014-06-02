print "Welcome. Pick 1 or 2\n"
door = raw_input('> ')

if door == "1":
	print "Pick again. 3 or 4.\n"
	pick = raw_input('> ')

	if pick == '3':
		print 'you picked 3'
	elif pick == '4':
		print 'you picked 4'
	else:
		print 'why\'d you do that for?'
elif door == "2":
	print 'just pick 1 next time...'
else:
	print 'real funny...nerd'

	n = 4
	if n in range(1, 10):
		print 'in range'
	else:
		print 'not in range'