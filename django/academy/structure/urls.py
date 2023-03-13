from django.urls import path

from structure.models import Faculty, Department
from structure.views import IndexView, FacultyView, DepartmentView


urlpatterns = [
    path('', IndexView.as_view(), name='main'),
] + [
    path(
        f'{faculty.acronym}/',
        FacultyView.as_view(),
        kwargs={'pk': faculty.id},
        name=f'{faculty.acronym}'
    )
    for faculty in Faculty.objects.all()
] + [
    path(
        f'{dep.acronym}/',
        DepartmentView.as_view(),
        kwargs={'pk': dep.id},
        name=f'{dep.acronym}'
    )
    for dep in Department.objects.all()
] + []

