from  django import forms

class myForm(forms.Form):
    # username = forms.CharField(max_length=100)
    choice = forms.CharField(max_length=100)


class social_postForm(forms.Form):
    username = forms.CharField(max_length=100)
    post = forms.CharField(widget=forms.Textarea)