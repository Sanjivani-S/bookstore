from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Order
from book.models import Book
import json

# Place an order (POST request)
@method_decorator(csrf_exempt, name='dispatch')
class PlaceOrderView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            book_id = data.get('book_id')
            quantity = data.get('quantity')
            
            # Check if both book_id and quantity are provided
            if not book_id or not quantity:
                return JsonResponse({"error": "Both book_id and quantity are required."}, status=400)
            
            # Attempt to fetch the book
            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                return JsonResponse({"error": "Book not found"}, status=404)

            # Create the order
            order = Order.objects.create(book=book, quantity=quantity)
            return JsonResponse({
                "id": order.id,
                "book": order.book.title,
                "quantity": order.quantity,
                "status": order.status,
            }, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data provided."}, status=400)

# Get all orders
class OrderListView(View):
    def get(self, request):
        # Ensure you're referencing the book relation properly
        orders = Order.objects.all().select_related('book').values('id', 'book__title', 'quantity', 'status')
        return JsonResponse(list(orders), safe=False)
"""
class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all().values("id", "book_title", "quantity", "status")
        return JsonResponse(list(orders), safe=False)
"""
        

# Get a specific order
class OrderDetailView(View):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            return JsonResponse({
                "id": order.id,
                "book": order.book.title,
                "quantity": order.quantity,
                "status": order.status,
            })
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
