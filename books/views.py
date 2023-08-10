from django.shortcuts import redirect, render
from .models import Book


# Create your views here.

def home(request):
    return render(request, 'books/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        Book.objects.create(title=title, author=author, genre=genre)
    books = Book.objects.all()
    return render(request, 'books/add_book.html', {'books': books})

def delete_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        book.delete()
        return redirect('book-list')
    except Book.DoesNotExist:
        return redirect('book-list')

