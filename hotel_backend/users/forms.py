from django.contrib.auth.forms import UserChangeForm
from .models import User

# Change form for a user
class TextAreaChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['textArea',]