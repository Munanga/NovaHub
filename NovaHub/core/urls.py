from django.urls import path
from core.views import index, delete

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>', delete, name='delete'),
]