class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing(self):
		for line in self.lyrics:
			print line

	def rap(self):
		print self.lyrics

happy_bday = Song(["Happy, BDay",
					"I heart you",
					"So I'll stop right there"])

yeezy = Song("One good girl is worth a thousand chickens")

happy_bday.sing()
yeezy.rap()