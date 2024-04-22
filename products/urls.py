from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductsViewSet

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='product')

urlpatterns = [
    # path('', views.ProductsViewSet.as_view({'get': 'list', 'post': 'create'}), name='products-list'),
    path('products/', ProductsViewSet.as_view({'get': 'list', 'post': 'create'}), name='products-list'),
    path('products/<int:pk>/', ProductsViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
    path('products/update/<int:pk>/', ProductsViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='product-update'),
    path('products/delete/<int:pk>/', ProductsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='product-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]