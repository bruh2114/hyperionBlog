from django.urls import path
from .views import blog_list, post_detail
from . import views

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
]