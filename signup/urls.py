from django.urls import path

from . import views

app_name = 'signup'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('redirect', views.activate, name='redirect'),
]