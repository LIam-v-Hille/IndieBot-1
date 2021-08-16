import re

class Filter:		# Create a filter object

	def __init__(self):
		self.filters = []
		pass

	def add_filter_phrase(self,*phrases):
		lphrases = list(phrases)
		for phrase in phrases:
			if phrase not in self.filters:
				self.filters.append(phrase)
			else:
				print(f"filter expression \"{phrase}\" already in list")
				lphrases.remove(phrase)
		return f"created a filter with phrase(s) {lphrases}"

	def remove_filter_phrase(self,*phrases):
		lphrases = list(phrases)
		for phrase in phrases:
			if phrase not in self.filters:
				print(f"filter expression \"{phrase}\" not in list")
				lphrases.remove(phrase)
			else:
				self.filters.remove(phrase)
		return f"removed {lphrases} from filters"

	def filter_file(self,file, text: bool = False):
		lines = open(file,"r").readlines()
		line_num = 1
		for line in lines:
			lower_line = line.lower()
			i = 0
			for _ in self.filters:
				lower_lines = re.split(" |\n", lower_line)
				if self.filters[i] in lower_lines:
					if text:
						print(f"phrase \"{self.filters[i]}\" at line {line_num}")
				i += 1
			line_num += 1

	def get_filter(self, text: bool = False):
		if text:
			return f"the current filters are {self.filters}"
		else:
			return self.filters



