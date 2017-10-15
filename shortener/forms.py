from django import forms

class SubmitForm(forms.Form):
	url = forms.CharField(
			label = '',
			widget = forms.TextInput(
					attrs = {
						'placeholder' : 'Enter the url'
					}
				)
		)