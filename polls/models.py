from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	major = models.CharField(max_length=50)
	rank = models.CharField(max_length=10)
	position = models.CharField(max_length=20)

class PositionQuestion(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class CandidateChoice(models.Model):
	question = models.ForeignKey(PositionQuestion, on_delete=models.CASCADE)
	candidate_id = models.ForeignKey(Person, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)