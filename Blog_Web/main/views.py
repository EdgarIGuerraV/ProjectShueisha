from multiprocessing import context
from django.shortcuts import render

#
#importaciones necesarias 
from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
        Portfolio,
        Blog,
        Reviews,
	)

from django.views import generic
from . forms import BlogForm, ContactForm, ReviewsForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect

#registro de usuarios
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form =CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'La cuenta fue creada con el nombre: '+ user)

				return redirect('main:register')
		
		context = {'form':form}
		return render(request, 'main/register.html', context)

#Logeo de usuarios
def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Username OR Password is incorrect')
		context = {}
		return render(request, 'main/contact.html', context)

#Cerrar sesion de usuarios
def logoutUser(request):
	logout(request)
	return redirect('main:contact')
		


#indice de la aplicacion
class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		reviews = Reviews.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		context["reviews"] = reviews
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por la sugerencia.')
		return super().form_valid(form)

#clase para agregar informacion a los blogs desde la app
class BlogAddInfo(generic.FormView):
	template_name = "main/blog-add.html"
	form_class = BlogForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por la contribucion a los Bolgs.')
		return super().form_valid(form)
#clase para agregar informacion a las reviews desde la app
class ReviewsAddInfo(generic.FormView):
	template_name = "main/Reviews-add.html"
	form_class = ReviewsForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por la contribucion a las Reviews.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"
#clase para mostrar los blogs
class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog-home.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

#clase para mostrar los detalles de los blogs
class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-post.html"


#clase para mostrar las reviews
class ReviewsView(generic.ListView):
    model = Reviews
    template_name = "main/reviews-home.html"
    paginate_by = 10 

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

#clase para mostrar los detalles de las reviews
class ReviewsDetailView(generic.DetailView):
    model = Reviews
    template_name = "main/reviews-post.html"