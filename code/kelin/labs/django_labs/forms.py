from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class SignUp(forms.Form):
    
    class Meta:
        model = User
        fields = ("username", "password")

    def save(self, commit=True):
        user = super(SignUp, self).save(commit-False)
        if commit():
            user.save
        return user