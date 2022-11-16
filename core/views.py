from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from core.models import User
from core.forms import CustomUserCreationForm


def home(request):
    count = User.objects.count()
    return render(request, "core/home.html", {"count": count})


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

class SignUp(CreateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")


@login_required
def secret_page(request):
    return render(request, "core/secret_page.html")


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = "core/secret_page.html"
