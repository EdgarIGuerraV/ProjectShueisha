from importlib.metadata import requires
from django import forms
from .models import Blog, ContactProfile, Reviews

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Registro de los forms que tomaran la informacion ingresada en la aplicacion


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)
#Form encargado de crear nuevos usuarios 
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

#Form encargado de crear nuevos blogs desde la propia aplicación
class BlogForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
		'placeholder': '*Author name...',
	}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
		'placeholder': '*Full name...',
	}))
	description = forms.CharField(max_length=500, required=True,
		widget=forms.TextInput(attrs={
		'placeholder': '*Description...',
	}))
	body = forms.CharField(max_length=1000, required=True,
		widget=forms.Textarea(attrs={
		'placeholder': '*Body info...',
	}))
	image = forms.ImageField()

	class Meta:
		model = Blog
		fields =['author','name', 'description', 'body', 'image']

#Form encargado de crear nuevas reviews desde la misma aplicacion
class ReviewsForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
		'placeholder': '*Author name...',
	}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
		'placeholder': '*Full name...',
	}))
	description = forms.CharField(max_length=500, required=True,
		widget=forms.TextInput(attrs={
		'placeholder': '*Description...',
	}))
	body = forms.CharField(max_length=1000, required=True,
		widget=forms.Textarea(attrs={
		'placeholder': '*Body info...',
	}))
	image = forms.ImageField()

	class Meta:
		model = Reviews
		fields =['author','name', 'description', 'body', 'image']