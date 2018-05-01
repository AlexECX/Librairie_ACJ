from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


from main_site.forms import SignUpForm
from books.models import Book

def index(request):

    books_to_propose = []

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    books = Book.objects.all()
    books_to_propose = list(books)

    # Render the HTML template index.html with the data in the context variable.
    context= {'num_visits':num_visits,
              'books_to_propose': books_to_propose
             }
    return render(request, 'main_site/index.html', context)


# def signin(request):
#     context = {}
#     return render(request, 'main_site/signin_form.html', context)

# def signup(request):
#     context = {}
#     return render(request, 'main_site/signup_form.html', context)

def userprofile(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'main_site/user_profile.html', {"user":user})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('main_site:index'))
    else:
        form = SignUpForm()
    return render(request, 'main_site/signup_form.html', {'form': form})


def error(request):
    return render(request, '404.html', {})
