from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for showing details of one library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
