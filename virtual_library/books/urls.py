from django.urls import path,re_path,include
from django.views.generic import RedirectView



from books import views

app_name = 'books'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/<keyword>/', views.search, name='search'),
    path('<int:book_id>/', views.get_info, name='get_info'),
    # re_path(r'', views.error, name='error'),
]