from django.urls import path
# from .views import (BookCreate, BookDelete, BookDetail, BookUpdate, BookList, home_page, BookSearch, BookListApi,
#                     BookCreateApi, BookDestroyApi, BookUpdateApi)
#
# urlpatterns = [
#     path('', home_page, name='home-page'),
#     path('book-list/', BookList.as_view(), name='book-list'),
#     path('book-create/', BookCreate.as_view(), name='book-create'),
#     path('book-update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
#     path('book-detail/<int:pk>/', BookDetail.as_view(), name='book-detail'),
#     path('book-delete/<int:pk>/', BookDelete.as_view(), name='book-delete'),
#     path('book_search/', BookSearch.as_view(), name='book-search'),
#     path('list-api/', BookListApi.as_view(), name='list-api'),
#     path('create-api/', BookCreateApi.as_view(), name='create-api'),
#     path('destroy-api/<int:pk>/', BookDestroyApi.as_view(), name='destroy-api'),
#     path('update-api/<int:pk>/', BookUpdateApi.as_view(), name='update-api'),
#
# ]


from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
urlpatterns = router.urls