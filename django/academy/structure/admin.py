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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['groups'].initial =


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentForm

    def get_changeform_initial_data(self, request):
        initials = super().get_changeform_initial_data(request)
        initials['groups'] = [o for o in models.Group.objects.filter(department__name=initials['name'])]
        return initials


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

