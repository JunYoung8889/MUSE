from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'my-score form-control',
                'placeholder': 'Score',
                'step': 0.5,
                'min': 0,
                'max': 5,
            }
        ),
        error_messages={
            'required': 'Please enter score(float)'
        },
    )

    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'my-review form-control',
                'rows': 1,
                'cols': 40,
                'placehoder': '한줄평을 작성해주세요!',
            }
        ),
        required=True
    )
    class Meta:
        model = Review
        fields = ('score','content',)