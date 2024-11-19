from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Book
import json

# Display all available books
class BookListView(View):
    def get(self, request):
        books = Book.objects.all().values("id", "title", "author", "price")
        return JsonResponse(list(books), safe=False)

# Add a new book (POST request)
@method_decorator(csrf_exempt, name='dispatch')  # Apply csrf_exempt to the class
class AddBookView(View):
    def post(self, request):
        data = json.loads(request.body)
        title = data.get('title')
        author = data.get('author')
        price = data.get('price')
        book = Book.objects.create(title=title, author=author, price=price)
        return JsonResponse({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "price": str(book.price),
        })
