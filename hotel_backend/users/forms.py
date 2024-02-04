from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# Creation form for a user
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("id",)

# Change form for a user
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("id",)