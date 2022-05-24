from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    score = forms.FloatField(
        label="평점",
        widget=forms.NumberInput(
            attrs={
                'class': 'my-score me-3 ms-2',
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
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class': 'my-review mx-2 w-50',
                'placeholder': '한줄평을 작성해주세요!',
            }
        ),
        required=True
    )
    class Meta:
        model = Review
        fields = ('score','content',)