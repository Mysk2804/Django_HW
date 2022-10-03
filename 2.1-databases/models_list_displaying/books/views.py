from django.shortcuts import render

from books.models import Book



def books_view(request):
    template = 'books/books_list.html'
    all_books = Book.objects.all()
    context = {
        'books': all_books
    }
    return render(request, template, context)

def book_title(request, slug):
    template = 'books/books_title.html'
    all_books = Book.objects.all()
    bookу = ''
    for book in all_books:
        if str(book.pub_date) == slug:
            bookу = book
    context = {
        'book': bookу,
        'page': all_books
    }
    return render(request, template, context)

