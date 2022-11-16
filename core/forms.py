from django.contrib.auth import forms

from core.models import User

class CustomUserCreationForm(forms.UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "username", "age"]
        field_classes = {"username": forms.UsernameField}

