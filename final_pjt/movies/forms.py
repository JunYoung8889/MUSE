from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'rows': 1,
                'cols': 40,
                'placehoder': '한줄평을 작성해주세요!',
            }
        ),
        required=True
    )
    class Meta:
        model = Comment
        fields = ('content',)