from django.contrib.auth import forms

# from core.models import User
# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

class CustomUserCreationForm(forms.UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ["email", "username", "age"]
        field_classes = {"username": forms.UsernameField}

