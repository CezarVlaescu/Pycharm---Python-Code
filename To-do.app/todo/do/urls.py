from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_data/<str:pk>', views.Update, name='update_data'),
    path('delete/<str:pk>', views.delete, name='delete'),
]