from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def books(request):
    lista_libros = Libro.objects.all()
    context = {
        'libros': lista_libros,
    }
    return render(request, 'books.html', context)


def add_book(request):
    titulo = request.POST['tittle']
    description = request.POST['description']
    Libro.objects.create(titulo=titulo, descripcion=description)
    return redirect(books)


def books_show(request, book_id):
    context = {
        'books' : Libro.objects.get(id = book_id),
        'authors' : Libro.objects.get(id = book_id).publicador.all(),
        'all_authors' : Publicador.objects.exclude(libros = book_id ),
    }
    return render(request, 'books_show.html', context)


def add_publisher(request, book_id):
    nuevo = Publicador.objects.get(id = request.POST['select_author'])
    Libro.objects.get(id = book_id).publicador.add(nuevo)
    return redirect(f'/books_show/{book_id}') # El / antes de la dirección, borra lo anterior
                                        # y no es una consecución de la redirección que indico, es decir,
                                        # No recargará /books_show/5/books_show/5', sino que solamente /books_show/{book_id}'


def authors(request):
    lista_autores = Publicador.objects.all()
    context = {
        'autores': lista_autores,
    }
    return render(request, 'authors.html', context)


def add_author(request):
    nombre = request.POST['nombre2']
    notas = request.POST['nota']
    Publicador.objects.create(nombre=nombre, notas=notas)
    return redirect(authors)


def authors_show(request, author_id): # Cambié de get a filter porque me decía que el objeto no es iterable
    books = Publicador.objects.get(id=author_id).libros.all()
    context = {
        'authors': Publicador.objects.filter(id = author_id),
        'boks': books,
        'all_books': Libro.objects.exclude(publicador = author_id ),
    }
    #print('***************************************************',buks)
    return render(request, 'authors_show.html', context)


def add_publisher_book(request, author_id):
    add = Libro.objects.get(id = request.POST['select_book'])
    Publicador.objects.get(id = author_id).libros.add(add)
    return redirect(f'/authors_show/{author_id}')


# def add_publisher(request, book_id):
#     nuevo = Publicador.objects.get(id = request.POST['select_author'])
#     Libro.objects.get(id = book_id).publicador.add(nuevo)
#     return redirect(f'/books_show/{book_id}')