from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json
from django.forms.models import model_to_dict


from .models import Sale, SessionCart
from books.models import Book

# Decorators for views

def refresh_page_decorate(view_func):
    """Oblige un rafraichissement de la page apres exécution de la view

    :Args: view_func (function): La fonction view a décorer

    :Returns: function: La fonction view décoré
    """
    def refresh_page(request, *args, **kwargs):
        next = request.POST.get("next", "/")
        view_func(request, *args, **kwargs)

        return redirect(next)
        #return redirect(request.META.get('HTTP_REFERER','main_site:index'))
    return refresh_page

# Create your views here.

@login_required
def shop(request):
    sale_query = request.POST.get("research")
    if sale_query is not None:
        sale = Sale()
        sale.product = sale_query
        sale.user = request.user
        sale.save()
        return redirect(reverse('main_site:index'))
    else:
        return render(request, "online_shop/sale_form.html", {})


@login_required
@refresh_page_decorate
def add_to_cart(request, book_id):
    user_cart_id = request.session.get("shopping_cart")
    if not user_cart_id:
        user_cart = SessionCart.objects.filter(user=request.user).first()
        if not user_cart:
            a = SessionCart()
            a.user = request.user
            a.save()
            user_cart = a
        request.session["shopping_cart"] = user_cart.id
        request.session.modified = True
    else:
        user_cart = SessionCart.objects.get(id=user_cart_id)

    query = Book.objects.filter(id=book_id).first()
    user_cart.books.add(query)



@login_required
@refresh_page_decorate
def remove_from_cart(request, book_id):
    user_cart_id = request.session.get("shopping_cart")
    if not user_cart_id:
        user_cart = SessionCart.objects.filter(user=request.user).first()
        if not user_cart:
            a = SessionCart()
            a.user = request.user
            a.save()
            user_cart = a
        request.session["shopping_cart"] = user_cart.id
        request.session.modified = True
    else:
        user_cart = SessionCart.objects.get(id=user_cart_id)

    to_remove = user_cart.books.filter(id=book_id).first()
    if to_remove:
        user_cart.books.remove(to_remove)



@login_required
def view_cart(request):
    user_cart_id = request.session.get("shopping_cart")
    if not user_cart_id:
        user_cart = SessionCart.objects.filter(user=request.user).first()
        if not user_cart:
            a = SessionCart()
            a.user = request.user
            a.save()
            user_cart = a
        request.session["shopping_cart"] = user_cart.id
        request.session.modified = True
    else:
        user_cart = SessionCart.objects.get(id=request.session["shopping_cart"])

    shopping_cart_books = user_cart.books.all()

    context = { "books": shopping_cart_books, }
    return render(request, "online_shop/shopping_cart.html", context)
