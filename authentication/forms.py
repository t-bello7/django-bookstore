from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

CustomUser = get_user_model


class CustomUserCreationForm(UserCreationForm):
    pass
    # email = forms.CharField()
    # username = forms.CharField()

    # class Meta:
    #     model = CustomUser
    #     fields = ('email', 'username', )


class CustomUserChangeForm(UserChangeForm):
    pass

    # class Meta:
    #     model = CustomUser
    #     fields = ('email', 'username', )
