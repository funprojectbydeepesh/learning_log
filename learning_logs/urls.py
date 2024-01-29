from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('topic/', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.detailview, name='detail'),
]