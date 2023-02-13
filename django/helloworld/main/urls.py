from django.urls import path

from main.views import index_view

# core.urls.urlpatterns -> 'index'
urlpatterns = [
    path('index/', index_view, name='main_page'),
]

