from django import forms

class Author(forms.Form):
    Auth = forms.CharField(label="Name", max_length=25)
    
class Message(forms.Form):
    Mess = forms.CharField(label="", widget=forms.Textarea, max_length=90)