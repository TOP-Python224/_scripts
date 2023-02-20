from django.urls import path

from catalog import views

# ''
# 'ast/'
urlpatterns = [
    path('', views.index),
    # path('ast/', views.publisher),
]
