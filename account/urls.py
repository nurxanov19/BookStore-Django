from django.urls import path
from .views import user_register


app_name = 'account'
urlpatterns = [
    path('', user_register, name='register'),
]