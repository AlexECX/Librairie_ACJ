from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
#from django.template import Context, loader
from django.urls import reverse

# Database models import
from books.models import Book
from main_site.forms import SignUpForm


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

@login_required
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
            return redirect('main_site:index')
    else:
        form = SignUpForm()
        return render(request, 'main_site/signup_form.html', {'form': form})

# Not in use
def error(request):
    return render(request, '404.html', {})
