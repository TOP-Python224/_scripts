from decimal import Decimal as dec
from django import forms

from structure.models import Department, Group


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
        self.fields['name'].widget.attrs |= {'class': 'form-control'}
        self.fields['building'].widget.attrs |= {'class': 'form-control'}
        self.fields['financing'].widget.attrs |= {'class': 'form-control'}
        self.fields['select_currency'].widget.attrs |= {'class': 'btn btn-outline-secondary dropdown-toggle'}

    def save_with_fk(self, faculty):
        department = super().save(commit=False)
        department.faculty = faculty
        if self.cleaned_data['select_currency'] == 'EUR':
            department.financing *= dec('0.85')
        department.save()
        return department


class AddGroup(forms.ModelForm):
    year = forms.IntegerField(
        min_value=1,
        max_value=6,
        label='Enter the current year of education for a new group'
    )

    class Meta:
        model = Group
        fields = ('year', 'name')
        labels = {
            'name': 'Enter the name for a new group',
        }

    def save_with_fk(self, department):
        group = super().save(commit=False)
        group.department = department
        group.save()
        return group

