# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("categories/", views.categories_blog, name="categories_blog"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]