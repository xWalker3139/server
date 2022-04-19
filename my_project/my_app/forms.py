from django import forms
from .models import Post, Customer, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'autocomplete':'off'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'autocomplete':'off'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'autocomplete':'off'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'autocomplete':'off'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('user','name', 'email', 'profile_pic')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'title', 'email', 'description', 'image')
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'type':'hidden'}),
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title...', 'id':'title'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'id':'email'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description...', 'id':'description', 'maxlength':'80'}),
            'image':forms.FileInput(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('first_name', 'last_name', 'comment')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}),
            'comment':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your comment...'}),
        }
