from msilib.schema import CheckBox
from socket import fromshare
from django import forms
from .models import BlogPost

#Import the model that you want to work with
#Give it a class(anything you want)
#It inherits forms.ModelForm(from the import of forms up top)
#We're using a database that has a model, so we want to create form fields for all of our model code

#Forms.modelform allows us to create form fields from our model 
class BlogForm(forms.ModelForm):
    #Create class '''Meta''' and designate what are model is, fields, and widgets
    class Meta:
       model = BlogPost
       fields = ('title', 'body', 'user', 'public')  
       #This is where we get to style our form. attrs is our attributes 
       #To use these we wrap are code(create.html) in 'form-group' and for each item we give it a class of form-control in order to bootstrapify 
       widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
        'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
        'user': forms.Select(attrs={'class': 'form-control'}),
        'public': forms.CheckboxInput(attrs={'class': 'form-control'}),
       }

#Forms.modelform allows us to create form fields from our model 
class UpdateForm(forms.ModelForm):
    #Create class '''Meta''' and designate what are model is, fields, and widgets
    class Meta:
       model = BlogPost
       fields = ('title', 'body', 'public')  
       #This is where we get to style our form. attrs is our attributes 
       #To use these we wrap are code(update.html) in 'form-group' and for each item we give it a class of form-control in order to bootstrapify 
       widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
        'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
        'public': forms.CheckboxInput(attrs={'class': 'form-control'}),
       }