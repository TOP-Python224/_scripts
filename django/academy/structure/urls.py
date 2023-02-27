from django.urls import path

from structure.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='main'),
]

