from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Books
from .forms import BookForm
from django.views import View
# Create your views here.

def home_page(request):
    return render(request, 'home.html')


class BookCreate(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'webpages/book_create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('book-list')

        return render(request, 'webpages/book_create.html', {'form': form})


class BookList(View):

    def get(self, request):
        books = Books.objects.all()
        return render(request, 'webpages/book_list.html', {'books': books})


class BookDetail(View):

    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        return render(request, 'webpages/book_detail.html', {'book': book})


class BookUpdate(View):

    def get(self, request, pk):
        book = get_object_or_404(Books, id=pk)
        form = BookForm(instance=book)
        return render(request, 'webpages/book_update.html', {'form': form})

    def post(self, request, pk):
        book = get_object_or_404(Books, id=pk)
        form = BookForm(request.POST, instance=book, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('book-detail', kwargs={'pk': book.id}))

        return render(request, 'webpages/book_update.html', {'form': form})


class BookDelete(View):

    def get(self, request, pk):
        book = get_object_or_404(Books, id=pk)
        return render(request, 'webpages/book_delete.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Books, id=pk)
        book.delete()
        return redirect('book-list')


class BookSearch(View):

    def get(self, request):
        query = request.GET.get('q', None)
        book = Books.objects.filter(Q(title__icontains=query) | Q(year__icontains=query)) if query else Books.objects.none()
        return render(request, 'webpages/book_search.html', {'book': book})


# class BookSearch(View):
#
#     def get(self, request):
#         query = request.GET.get('q', None)
#         book = Books.objects.annotate(SearchVector('year', 'title', 'author_name')) if query else Books.objects.none()
#         return render(request, 'webpages/book_search.html', {'book': book})