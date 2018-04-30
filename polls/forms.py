from django import forms

class PollForm(forms.Form):
	#since the number of fields is not know until runtime,
	#we need a way of contructing field variables dynamically
	def __init__(self, fields, *args, **kwargs):
		super(PollForm, self).__init__(*args, **kwargs)
		for i in range(len(fields)):
			self.fields['my_field_%i' % i] = forms.CharField()