# Create your models here.

from django.db import models
from book.models import Book  # Foreign key relationship to Book model

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order #{self.id} - {self.book.title}"

