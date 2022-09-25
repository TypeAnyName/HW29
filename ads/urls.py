from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ads.views import CategoryListView, index, AdDetailView, CategoryDetailView, CategoryCreateView, \
    CategoryUpdateView, CategoryDeleteView, AdsListView, AdCreateView, AdUpdateView, AdDeleteView, AdUploadImageView, \
    UserListView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', index),
    path('cat/', CategoryListView.as_view()),
    path('ad/', AdsListView.as_view()),
    path('ad/<int:pk>', AdDetailView.as_view()),
    path('ad/<int:pk>/update', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete', AdDeleteView.as_view()),
    path('ad/create', AdCreateView.as_view()),
    path('ad/<int:pk>/upload_image', AdUploadImageView.as_view()),
    path('cat/<int:pk>', CategoryDetailView.as_view()),
    path('cat/<int:pk>/update', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete', CategoryDeleteView.as_view()),
    path('cat/create', CategoryCreateView.as_view()),
    path('user/', UserListView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('user/<int:pk>/update', UserUpdateView.as_view()),
    path('user/<int:pk>/delete', UserDeleteView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
