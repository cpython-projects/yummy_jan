from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy


def logout_user(request):
    logout(request)
    return redirect('home:main_page')


# Create your views here.
class LoginUserView(LoginView):
    # form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next') or self.request.POST.get('next') or '/'


class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('login')

