from django.urls import path
from .views import BookListView, AddBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', AddBookView.as_view(), name='add_book'),
]
