from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
        Portfolio,
        Blog,
        Reviews,
	)

from django.views import generic


from . forms import BlogForm, ContactForm, ReviewsForm


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

class BlogAddInfo(generic.FormView):
	template_name = "main/blog-add.html"
	form_class = BlogForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por la contribucion a los Bolgs.')
		return super().form_valid(form)

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

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog-home.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-post.html"



class ReviewsView(generic.ListView):
    model = Reviews
    template_name = "main/reviews-home.html"
    paginate_by = 10 

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ReviewsDetailView(generic.DetailView):
    model = Reviews
    template_name = "main/reviews-post.html"