from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('books', views.books),
    path('add_book', views.add_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('books_show/<book_id>/', views.books_show),
    path('books_show/<book_id>/add_publisher', views.add_publisher),
    path('authors_show/<author_id>/', views.authors_show),
    path('authors_show/<author_id>/add_book', views.add_publisher_book),
]