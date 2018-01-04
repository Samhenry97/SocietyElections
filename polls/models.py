#-------------------------------------------------------------------
#This file contains the model DAO's for the app
#-------------------------------------------------------------------

from django.db import models

# Contains the information about the person being elected
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	major = models.CharField(max_length=50)
	rank = models.CharField(max_length=10)
	position = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name + ' ' + self.last_name + ", " + self.rank + ' ' + self.major + ' major, current position: ' + self.position

#contains the information about the poll for a particular position
class PositionQuestion(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

#contains the people up for election for each question, is an association table
class CandidateChoice(models.Model):
	question = models.ForeignKey(PositionQuestion, on_delete=models.CASCADE, related_name='choices')
	candidate_id = models.ForeignKey(Person, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return 'Candidate with id ' + candidate_id + ' has ' + self.votes + ' votes.'