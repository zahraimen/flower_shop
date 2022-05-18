from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlowerListView.as_view(), name='flower_list')
]
