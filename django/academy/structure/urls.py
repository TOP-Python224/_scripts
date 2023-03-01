from django.urls import path

from structure.models import Faculty
from structure.views import IndexView, FacultyView, MyFormView


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
    path('forms', MyFormView.as_view(), name='forms')
]

