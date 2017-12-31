from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	major = models.CharField(max_length=50)
	rank = models.CharField(max_length=10)
	position = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name + ' ' + self.last_name + ", " + self.rank + ' ' + self.major + ' major, current position: ' + self.position

class PositionQuestion(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class CandidateChoice(models.Model):
	question = models.ForeignKey(PositionQuestion, on_delete=models.CASCADE)
	candidate_id = models.ForeignKey(Person, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return 'Candidate with id ' + candidate_id + ' has ' + self.votes + ' votes.'