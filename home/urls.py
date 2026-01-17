from django.urls import path
from .views import home, BlogDetails

urlpatterns = [
    path('',home,name='home'),
    path('blog/<int:pk>',BlogDetails,name='blog detail'),
]