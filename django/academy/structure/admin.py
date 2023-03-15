from django import forms
from django.contrib import admin

from structure import models


# admin.site.register(models.Department)
# class DepartmentInline(admin.TabularInline):
#     model = models.Department


class DepartmentForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=models.Group.objects.all()
    )

    class Meta:
        model = models.Department
        fields = ('name', 'building', 'financing', 'faculty', 'groups')


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentForm

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        values = models.Group.objects.filter(department=obj)
        # form.base_fields['groups'].initial = values
        # только для чтения
        form.base_fields['groups'].queryset = values
        return form


admin.site.register(models.Faculty)
# @admin.register(models.Faculty)
# class FacultyAdmin(admin.ModelAdmin):
#     inlines = [
#         DepartmentInline
#     ]


admin.site.register(models.Subject)
admin.site.register(models.Teacher)
admin.site.register(models.Curator)
admin.site.register(models.Student)
admin.site.register(models.Lecture)


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'year', 'department', 'students', 'curators')
    list_display = ('year', 'name')
    list_display_links = ('name',)

