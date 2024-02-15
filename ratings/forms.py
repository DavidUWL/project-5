from django import forms
from .models import UserRating


class RatingsForm(forms.ModelForm):
    class Meta:
        model = UserRating
        exclude = ('user_profile',)
        fields = (
            'user_profile',
            'product',
            'rating_description',
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'rating_description': 'Write a short review',
            'product': 'your selected product.',
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'form-control')
            self.fields[field].label = False
