from django.urls import path
from rest_framework import routers
from apiapp import views

urlpatterns = []

urlpatterns += [
    path('category-list/', views.BookCategoryListView.as_view(), basename='category-list')
]
