#-----------------------------------------------------------------------
#This file contains the logic to manipulate the pages that the user sees 
#-----------------------------------------------------------------------

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import *
from .nomineeObject import *
from .forms import PollForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#This method contains the logic to manipulate the page containing all the candidates
def polls(request):
	#grab all of the positions up for election 
	latest_question_list = PositionQuestion.objects.order_by('id')
	#create an object that holds each of the candidates for each of the positions

	#dictionary containing all of the people, classified by question
	peopleDict = {} 

	for question in latest_question_list:

		#position we need to get the people for
		nomineePosition = question.id

		#list of all the people local to this question
		personList = []

		# TODO: there has to be a quicker way of doing this, maybe a get method
		# but this loops over all of the candidates
		for person in CandidateChoice.objects.order_by('id'):

			#if the person's id equals the position id, grab them
			if person.question_id == nomineePosition:

				#get the data corresponding to that person's id
				personData = Person.objects.get(pk=person.candidate_id)

				#create a person object
				personToAdd = Nominee(personData.first_name + ' ' + personData.last_name, personData.rank, personData.major, (personData.first_name + personData.last_name).lower())
				personList.append(personToAdd)

		# add the people in this particular question to the group of all the people
		peopleDict[question.id] = personList

	context = {'latest_question_list': latest_question_list, 'peopleDict': peopleDict}
	return render(request, 'polls/polls.html', context)


def submitted(request):
	if request.method == 'POST':
		form = PollForm(request.POST)
		if form.is_valid():
			return HttpResponse("""Thank you""")

	context = {}
	return render(request, 'polls/submission.html', context)


#This returns the details about a certain position, with the url to access this page in urls.py
def detail(request, question_id):
	question = get_object_or_404(PositionQuestion, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

#This displays the results of the question
def results(request, question_id):
	return HttpResponse("""You're looking at the results of question {}.""".format(question_id))

#This method handles voting for a particular candidate
def vote(request, question_id):
	question = get_object_or_404(PositionQuestion, pk=question_id)
	try:
		selected_choice = question.choices.get(pk=request.POST['CandidateChoice'])
	except (KeyError, CandidateChoice.DoesNotExist):
        # Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def ballot(request):
	candidate_poll_list = PositionQuestion.objects.order_by('-pub_date')
	print(candidate_poll_list)
	context = {'candidate_poll_list': candidate_poll_list}
	return render(request, 'polls/ballot.html', context)
