from django.urls import path

from . import views

urlpatterns = [
    path('login', views.UsuarioListView.as_view()),
]