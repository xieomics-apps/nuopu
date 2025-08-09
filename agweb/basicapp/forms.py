from django import forms

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')

class ContactusForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])
