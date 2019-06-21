import sys

class Adatok:

	def append(self,filename):
		try:
			f = open(filename)
			for line in f:
				line = line.split()
				temp_pair = [int(line[0]), int(line[1])]
				self.data.append(temp_pair) 
			f.close()
		except IOError:
			print "Input file %s does not exist!" % filename
				
			
	def __init__(self,filename):
		self.data = []
		self.append(filename)

	def __str__(self):
		if not self.data:
			return "Empty"
		else:
			return "Intervals:\n" + "\n".join(map(lambda x : str(x).replace(" ", ""), self.data))