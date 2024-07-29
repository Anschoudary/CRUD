from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete')
]
