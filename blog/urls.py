from . import views
from django.urls import path


urlpatterns = [


    path("", views.ListBlog.as_view(), name="posts"),




]