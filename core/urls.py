from django.urls import path
from .views import (
    AssetListView,
    AssetDetailView,
    AssetCreateView,
    AssetUpdateView,
    AssetDeleteView,
    UserAssetListView
)
from . import views

urlpatterns = [
    path('', AssetListView.as_view(), name='core-home'),
    path('user/<str:username>', UserAssetListView.as_view(), name='user-assets'),
    path('asset/<int:pk>/', AssetDetailView.as_view(), name='asset-detail'),
    path('asset/new/', AssetCreateView.as_view(), name='asset-create'),
    path('asset/<int:pk>/update/', AssetUpdateView.as_view(), name='asset-update'),
    path('asset/<int:pk>/delete/', AssetDeleteView.as_view(), name='asset-delete'),
    path('about/', views.about, name='core-about'),
]
