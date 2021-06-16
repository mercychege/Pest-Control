from django.conf.urls import url
from .views import PesticideViewSet, CropViewSet, DiseaseViewSet,PostViewSet,ShopViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pest', PesticideViewSet, basename='pest')
router.register(r'post', PostViewSet, basename='post')
router.register(r'crop', CropViewSet, basename='crop')
router.register(r'disease', DiseaseViewSet, basename='disease')
router.register(r'shop', ShopViewSet, basename='shop')
urlpatterns = router.urls
