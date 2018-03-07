#-----------------------------------------------------------------------
#This file contains the logic to manipulate the pages that the user sees 
#-----------------------------------------------------------------------

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .forms import SignUpForm
from .tokens import account_activation_token
from django.template.loader import render_to_string
from .urls import *

def index(request):
	return render(request, 'signup/index.html')
	
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('signup/email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('redirect/')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})

def activate(request):
	return render(request, 'signup/activate.html')

def confirmed(request):
	return render(request, 'signup/confirmed.html')

