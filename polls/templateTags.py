#if we need another template tag, information here: https://stackoverflow.com/questions/40686201/django-1-10-1-my-templatetag-is-not-a-registered-tag-library-must-be-one-of
from django import template

register = template.Library()

# If you get an invalid filter message, these need to be 
# registered as filters, not tags
@register.filter('at_index')
def at_index(data, index):
    return data[index]

@register.filter('getPictureLocation')
def getPictureLocation(name):
 	return 'polls/img/' + name + '.jpg'