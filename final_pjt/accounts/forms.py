from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디를 입력해주세요.',
            }
        )
    )

    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 입력해주세요.',
            }
        )
    )
    
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 한 번더 입력해주세요.',
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디를 입력해주세요.',
            }
        )
    )

    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 입력해주세요.',
            }
        )
    )


    class Meta:
        model = get_user_model()
        fields = ("username", "password")