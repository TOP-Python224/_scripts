from django import forms

from structure.models import Department


class AddDepartment(forms.ModelForm):
    select_currency = forms.ChoiceField(choices=(
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ))

    class Meta:
        model = Department
        fields = ('name', 'building', 'financing')
        # exclude = ('faculty',)
        labels = {
            'name': 'Enter the name for a new department',
            'building': 'Enter the building number for a new department',
            'financing': 'Enter the current budget for a new department',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs |= {'class': 'input_text_style'}
        self.fields['building'].widget.attrs |= {'class': 'input_int_style'}
        self.fields['financing'].widget.attrs |= {'class': 'input_dec_style'}

