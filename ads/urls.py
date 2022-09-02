from django.urls import path

from ads.views import CategoryView, index, AdsView, AdDetailView, CategoryDetailView

urlpatterns = [
    path('', index),
    path('cat/', CategoryView.as_view()),
    path('ad/', AdsView.as_view()),
    path('ad/<int:pk>', AdDetailView.as_view()),
    path('cat/<int:pk>', CategoryDetailView.as_view()),
]