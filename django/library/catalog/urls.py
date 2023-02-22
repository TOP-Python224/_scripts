from django.urls import path

from catalog import views

# ''
# 'ast/'
urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('ast/', views.publisher, kwargs={'pub_id': 1}, name='ast'),
    path('eksmo/', views.publisher, kwargs={'pub_id': 2}, name='eksmo'),
]
