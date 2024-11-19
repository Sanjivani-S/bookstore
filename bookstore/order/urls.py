from django.urls import path
from .views import PlaceOrderView, OrderListView, OrderDetailView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/place/', PlaceOrderView.as_view(), name='place_order'),
]
