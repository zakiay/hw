class lexicon(object):
	def scan(self, sentence):
		keywords = [["direction", "north"], ["direction", "south"],
		["direction", "east"], ["direction", "west"], ["verb", "go"], 
		["verb", "stop"], ["verb", "kill"], ["verb", "eat"], ["stop", "the"],
		["stop", "in"], ["stop", "of"], ["stop", "from"], ["stop", "at"],
		["stop", "it"], ["noun", "door"], ["noun", "bear"],
		["noun", "princess"], ["noun", "cabinet"]]

		words = sentence.split(' ')

		full_list = []
		found = False

		for i in range(0, len(words)):
			found = False
			for j in range(0, len(keywords)):
				if words[i].lower() == keywords[j][1]:
					full_list.append((keywords[j][0], keywords[j][1]))
					found = True

			if not found:
				try:
					n = int(words[i])
					full_list.append(('number', n))
				except ValueError:
					full_list.append(('error', words[i]))
 
		return full_list