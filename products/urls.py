from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductsViewSet, HomeView

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='product')

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsViewSet.as_view({'get': 'list', 'post': 'create'}), name='products-list'),
    path('products/<int:pk>/', ProductsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]