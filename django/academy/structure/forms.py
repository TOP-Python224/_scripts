from django import forms
from django.core.exceptions import ValidationError
from string import ascii_letters


def is_alpha_space(value: str) -> None:
    if set(value) - (set(ascii_letters) | {' '}):
        raise ValidationError('field value must contain only latin letters and spaces')


class MyForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='Enter your name:',
        validators=[is_alpha_space]
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=100,
    )

