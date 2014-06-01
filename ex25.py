def break_words(stuff):
	"""This function will break up words"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Returns sorted sentence"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints first and last words"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts and prints first and last words"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)