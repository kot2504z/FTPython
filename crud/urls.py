from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_page, name='posts_page'),
	path('add_post', views.add_post, name='add_post'),
]