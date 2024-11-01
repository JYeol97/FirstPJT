from django.urls import path
from . import views
app_name = 'movies'

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:pk>/', views.actor_detail)
]