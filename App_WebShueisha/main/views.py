from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Reviews,
		
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		blogs = Blog.objects.filter(is_active=True)
		reviews = Reviews.objects.filter(is_active=True)
		
		context["blogs"] = blogs
		context["reviews"] = reviews
		
		return context

class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. we will be in contact')
		return super().form_valid(form)



class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

	#
class ReviewsView(generic.ListView):
	model = Reviews
	template_name = "main/reviews.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class ReviewsDetailView(generic.DetailView):
	model = Reviews
	template_name = "main/reviews-detail.html"


	