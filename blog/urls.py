from django.urls import path
from blog import views

urlpatterns = [
    path('post/<int:post_id>/', views.post),
    path('', views.index)
]