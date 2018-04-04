from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    """from urllib import request
import datetime

#TODO: use this to get the current vintage year
now = datetime.datetime.now()
yearToSearch = now.year

#TODO: make this the name of the person who is creating an account
pictureName = "johndoe.jpg"

f = open(pictureName, 'wb')
f.write(request.urlopen("http://www.bjuvintage.com/uploads/2017/public/portraits/20160919687986-1.jpg").read())
f.close()"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
