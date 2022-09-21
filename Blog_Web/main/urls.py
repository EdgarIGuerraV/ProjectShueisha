from django.urls import path
from . import views

app_name = "main"

#creando los path correspondientes para interactuar con la aplicacion
#por medio de views

urlpatterns = [
    #registro y logeo de usuarios
    path('register/',views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('contact/', views.ContactView.as_view(), name="contact"),

    #indice de la aplicacion
    path('',views.IndexView.as_view(),name="home"),

    #Reviews
    path('reviewsaddinfo/', views.ReviewsAddInfo.as_view(), name="reviewsaddinfo"),
    path('reviews/', views.ReviewsView.as_view(), name="reviews"),
    path('reviews/<slug:slug>',views.ReviewsDetailView.as_view(), name="review"),
    #Blogs
    path('blogaddinfo/', views.BlogAddInfo.as_view(), name="blogaddinfo"),
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name = 'blog'),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolio"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name = "portfolio"),
    

]