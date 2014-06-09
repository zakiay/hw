from nose.tools import *
from game import *

words = [('noun', 'player'), ('noun', 'princess'), ('verb', 'kill'),
('verb', 'shake'), ('direction', 'north'), ('direction', 'south')]

def test_sentence():
	s = Sentence(('noun', "player"), 
		('verb', "kill"), ('noun', "monster"))

	assert_equal(s.subject, "player")
	assert_equal(s.verb, "kill")
	assert_equal(s.object, "monster")

def test_peek():
	p = peek(words)
	assert_equal(p, 'noun')

def test_match():
	m = match(words, 'noun')
	assert_equal(m, ('noun', 'player'))

	m = match(words, 'wrong')
	assert_equal(m, None)

	m = match(words, 'verb')
	assert_equal(m, ('verb', 'kill'))

def test_skip():
	skip(words, 'noun')
	m = match(words, 'verb')

	assert_equal(m, ('verb', 'shake'))

