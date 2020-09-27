from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label="Title",max_length=200 , required = True)
    content = forms.CharField(widget=forms.Textarea , label = "Content" , required = True)



