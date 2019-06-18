from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import Book
from django.shortcuts import render, get_object_or_404


def index(request):
    book_list = Book.objects.order_by('title')[:5]
    #output = ', '.join([q.title for q in book_list])
    #return HttpResponse(output)
    context = {
        'book_list': book_list,
    }
    return render(request, 'katalog/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'katalog/detail.html', {'book': book})
