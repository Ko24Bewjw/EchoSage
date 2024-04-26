from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

# accounts/views.py

from django.contrib.auth.views import LoginView
from django.urls import reverse

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('file_upload_view')  # 指定要重定向到的视图的名称


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('upload_media'))  # 重定向到主页或其他适当页面
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
