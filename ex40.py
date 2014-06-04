class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy, BDay",
					"I heart you",
					"So I'll stop right there"])

yeezy = Song(["All I need is sweet and sour sauce",
				"One good girl is worth a thousand chickens"])

happy_bday.sing()
yeezy.sing()