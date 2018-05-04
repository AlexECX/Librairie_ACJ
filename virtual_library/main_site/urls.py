from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views



from . import views

login_template = {'template_name': 'main_site/signin_form.html'}

app_name = 'main_site'
urlpatterns = [
    path('signin/', auth_views.login, login_template, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('', views.index, name='index'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('index/', RedirectView.as_view(url='')),
    # re_path(r'', views.error, name='error'),
]
