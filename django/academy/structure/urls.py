from django.urls import path

from structure import views


urlpatterns = [
    path('', views.index, name='main'),
]

