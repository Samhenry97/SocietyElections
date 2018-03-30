#This is a file that contains the class with the data needed to list candidates
#Not sure if it's necessary, but I thought I'd create it to help be more organized
#and instead of just passing around tuples. Will help with code clarity


class Nominee:
	name = ''
	rank = ''
	major = ''
	pictureLocation = ''

	#constructor
	def __init__(self, name, rank, major, pictureLocation):
		self.name = name
		self.rank = rank
		self.major = major
		self.pictureLocation = pictureLocation

	#accessor methods
	def getName(self):
		return self.name

	def getRank(self):
		return self.rank

	def getMajor(self):
		return self.major

	def getPictureLocation(self):
		return self.pictureLocation




