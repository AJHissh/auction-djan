from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Listings

def index(request):
    queries = Listings.objects.all()
    
    return render(request, "auctions/index.html", {
        "data" : queries
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def categories(request):
    temp_list = []
    queries = Listings.objects.all().distinct()
    for i in queries:
        if i.category not in temp_list:
            temp_list.append(i.category)
            print(i.category)
    #  queries = Listings.objects.filter(category="Household")
    upd_queries = temp_list 
    print(temp_list)
    return render(request, "auctions/categories.html", {
        "data" : upd_queries
    })

def watchlist(request):
    return render(request, "auctions/watchlist.html")

@login_required
def edit_profile(request):
    if request.method == "POST":
        f_name = request.POST["firstName"]
        l_name = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        current_user = request.user
        print(current_user)
        obj = User.objects.get(username=current_user)
        print(obj)
        if l_name:
            obj.last_name = l_name
        if f_name:
            obj.first_name = f_name
        if email:
            obj.email = email
        if password:
            obj.set_password(password)
        obj.save()
        print(request)
        user = authenticate(request, username=current_user, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse("edit_profile"))
    return render(request, "auctions/edit.html") 
            
@login_required
def createlisting(request):
    try:
        if request.method == "POST":
            product = request.POST["productname"]
            category = request.POST["productcategory"]
            price = request.POST["salesprice"]
            description = request.POST["description"]
            current_user = request.user                
            obj = Listings.objects.create(owner=current_user)
            obj.item_name = product
            obj.category = category
            obj.price = price
            obj.description = description
            obj.owner = str(current_user)
            obj.save()
    except:
            return render(request, "auctions/createlisting.html", {
                    "message": "Please enter correct values except"
                })    
    return render(request, "auctions/createlisting.html")

