from django.urls import path
from . import views

app_name = "main"

#creando los path correspondientes

urlpatterns = [
    path('',views.IndexView.as_view(),name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('blogaddinfo/', views.BlogAddInfo.as_view(), name="blogaddinfo"),
     path('reviewsaddinfo/', views.ReviewsAddInfo.as_view(), name="reviewsaddinfo"),
    path('reviews/', views.ReviewsView.as_view(), name="reviews"),
    path('reviews/<slug:slug>',views.ReviewsDetailView.as_view(), name="review"),
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name = 'blog'),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolio"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name = "portfolio"),
    

]