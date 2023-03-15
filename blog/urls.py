from django.urls import path
from . import views

urlpatterns = [
	path('post', views.Posts.as_view()),
    path('post/<int:pk>', views.PostDetail.as_view()),
]
