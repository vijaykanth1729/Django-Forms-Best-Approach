from django.urls import path
from .views import books_list, contact, our_forum

app_name = 'books'
urlpatterns = [
    path('contact/', contact, name='contact'),
    path('', books_list, name='list'),
    path('forum/',our_forum, name='forum'),


]
