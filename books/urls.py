from django.urls import path
from .views import BookCreate, BookDelete, BookDetail, BookUpdate, BookList, home_page, BookSearch

urlpatterns = [
    path('', home_page, name='home-page'),
    path('book-list/', BookList.as_view(), name='book-list'),
    path('book-create/', BookCreate.as_view(), name='book-create'),
    path('book-update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('book-detail/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('book-delete/<int:pk>/', BookDelete.as_view(), name='book-delete'),
    path('book_search/', BookSearch.as_view(), name='book-search'),
]