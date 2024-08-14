from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home page"),
    path('detail/<str:model_name>/<int:pk>/', views.detail, name='detail'),
    path('comment/', views.comment, name='comment'),
    path('comment/update/<int:pk>/', views.update_comment, name='update_comment'),
    path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
]