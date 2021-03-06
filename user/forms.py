from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.models import User, models

class userRegistration(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        email = models.EmailField(unique=True)
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]