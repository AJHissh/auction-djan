from django.urls import path, include
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("subcategories", views.subcategories, name="subcategories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("listing/<int:dat_id", views.listings, name='listings')
] 

