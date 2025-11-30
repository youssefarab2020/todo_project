from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.deleteTask, name='delete'),
    path('update/<int:id>/', views.updateTask, name='update'),
]
