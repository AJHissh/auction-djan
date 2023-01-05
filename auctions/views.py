from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Listings
from .forms import ImageForm
from django.contrib import messages

def index(request):
    queries = Listings.objects.all()
    #  queries = Listings.objects.filter(category='Food')
    
    return render(request, "index.html", {
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
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


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
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


def categories(request):
    temp_list = []
    queries = Listings.objects.all()
    for i in queries:
        if i.category not in temp_list:
            temp_list.append(i.category)
            print(i.category)
    upd_queries = temp_list 
    print(temp_list)
    return render(request, "categories.html", {
        "data" : upd_queries
    })
    
def subcategories(request):
    temp_list = []
    name = request.GET['name']
    print(name)
    queries = Listings.objects.filter(category=name)
    return render(request, "subcategories.html", {
        "data" : queries
    })
    

def watchlist(request):
    return render(request, "watchlist.html")

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
    return render(request, "edit.html") 
            
@login_required
def createlisting(request):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
 
            if form.is_valid():
                obj = form.save(commit=False)
                obj.owner = request.user
                obj.save()
                return render(request, "createlisting.html")
        else:
            form = ImageForm()
        return render(request, "createlisting.html", {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')
    

