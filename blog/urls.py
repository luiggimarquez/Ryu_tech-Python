from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.createPage, name="createPage"),
    path('', views.pagesListView, name="pages"),
    path('details/<id>', views.pageDetailView, name="details"),
    
]