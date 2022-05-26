from django import forms
from .models import (
    ActorArticle,
    DirectorArticle,
    PeopleArticle,
    ActorComment,
    DirectorComment,
    PeopleComment,
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


class ActorCommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'from-control mx-2 w-50',
                'placeholder': '댓글을 작성해주세요!',
            }
        ),
        required=True
    )
    class Meta:
        model = ActorComment
        fields = ('content',)


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


class DirectorCommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'from-control mx-2 w-50',
                'placeholder': '댓글을 작성해주세요!',
            }
        ),
        required=True
    )
    class Meta:
        model = DirectorComment
        fields = ('content',)


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


class PeopleCommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'from-control mx-2 w-50',
                'placeholder': '댓글을 작성해주세요!',
            }
        ),
        required=True
    )
    class Meta:
        model = PeopleComment
        fields = ('content',)