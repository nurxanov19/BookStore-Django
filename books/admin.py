from django.contrib import admin
from .models import Books

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'author_last_name', 'year', 'quantity']
    search_fields = ['title', 'author_name', 'author_last_name']
    list_filter = ['title', 'author_name', 'author_last_name', 'year', 'quantity', 'published_at']
    ordering = ['year', 'quantity']

admin.site.register(Books, BookAdmin)
