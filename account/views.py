from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm
from .models import User
# Create your views here.

def user_register(request):

    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home-page')

    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})


