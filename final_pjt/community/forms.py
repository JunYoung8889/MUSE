from django import forms
from .models import (
    ActorArticle,
    DirectorArticle,
    PeopleArticle,
)


class ActorForm(forms.ModelForm):
    title = forms.CharField(
        label = '게시글 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '게시글 제목을 작성해주세요',
            }
        ),
        required=True
    )
    content = forms.CharField(
        label='게시글 내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '게시글 내용을 작성해주세요',
            }
        ),
        required=True
    )
    
    class Meta:
        model = ActorArticle
        fields = ('title','content',)


class DirectorForm(forms.ModelForm):
    title = forms.CharField(
        label = '게시글 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '게시글 제목을 작성해주세요',
            }
        ),
        required=True
    )
    content = forms.CharField(
        label='게시글 내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '게시글 내용을 작성해주세요',
            }
        ),
        required=True
    )
    
    class Meta:
        model = DirectorArticle
        fields = ('title','content',)


class PeopleForm(forms.ModelForm):
    title = forms.CharField(
        label = '게시글 제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '게시글 제목을 작성해주세요',
            }
        ),
        required=True
    )
    content = forms.CharField(
        label='게시글 내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '게시글 내용을 작성해주세요',
            }
        ),
        required=True
    )
    
    class Meta:
        model = PeopleArticle
        fields = ('title','content',)