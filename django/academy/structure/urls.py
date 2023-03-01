from django.urls import path

from structure.models import Faculty
from structure.views import IndexView, FacultyView, my_form_view


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
    path('forms', my_form_view, name='forms')
]

