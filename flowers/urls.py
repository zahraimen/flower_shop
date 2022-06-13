from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlowerListView.as_view(), name='flower_list'),
    path('<int:pk>/', views.book_detail_view, name='flower_detail'),
    path('new/', views.FlowerCreateView.as_view(), name='flower_create'),
    path('<int:pk>/edit/', views.FlowerUpdateView.as_view(), name='flower_update'),
    path('<int:pk>/delete/', views.FlowerDeleteView.as_view(), name='flower_delete')
]
