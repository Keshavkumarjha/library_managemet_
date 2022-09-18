from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from account.models import Book


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username','type','password1', 'password2')
        class Meta:
    

            widgets = {
                'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email Address'})
    
                 }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')




class Booksform(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
    