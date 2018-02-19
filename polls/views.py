#-----------------------------------------------------------------------
#This file contains the logic to manipulate the pages that the user sees 
#-----------------------------------------------------------------------

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#This method contains the logic to manipulate the page containing all the candidates
def index(request):
	latest_question_list = PositionQuestion.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

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

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'polls/signup.html', {'form': form})