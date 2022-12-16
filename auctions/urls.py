from django.urls import path

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
    path("edit_profile", views.edit_profile, name="edit_profile")
]
