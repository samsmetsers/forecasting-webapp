from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import GameUserCreationForm

class SignUpView(CreateView):
    form_class = GameUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
