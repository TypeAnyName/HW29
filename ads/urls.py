from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from ads.views.service import index
from ads.views import ad as ads_view, category as cat_view, user as user_view, location as location_view

urlpatterns = [
    path('', index),

    path('api-auth/', include('rest_framework.urls')),

    path('ad/', ads_view.AdsViewSet.as_view()),
    path('ad/<int:pk>', ads_view.AdDetailView.as_view()),
    path('ad/<int:pk>/update', ads_view.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete', ads_view.AdDeleteView.as_view()),
    path('ad/create', ads_view.AdCreateView.as_view()),
    path('ad/<int:pk>/upload_image', ads_view.AdUploadImageView.as_view()),

    path('cat/', cat_view.CategoryListView.as_view()),
    path('cat/<int:pk>', cat_view.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update', cat_view.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete', cat_view.CategoryDeleteView.as_view()),
    path('cat/create', cat_view.CategoryCreateView.as_view()),

    path('user/', user_view.UserViewSet.as_view()),
    path('user/<int:pk>', user_view.UserDetailView.as_view()),
    path('user/create/', user_view.UserCreateView.as_view()),
    path('user/<int:pk>/update', user_view.UserUpdateView.as_view()),
    path('user/<int:pk>/delete', user_view.UserDeleteView.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
