from django.conf.urls import url
from .views import PesticideViewSet, CropViewSet, DiseaseViewSet,PostViewSet,ShopViewSet,ShopProductViewSet, FilteredDiseaseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'disease/(?P<crop_id>[0-9]+)', FilteredDiseaseViewSet, basename='disease')
router.register(r'pesticide', PesticideViewSet, basename='pesticide')
router.register(r'post', PostViewSet, basename='post')
router.register(r'crop', CropViewSet, basename='crop')
router.register(r'disease', DiseaseViewSet, basename='disease')
router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'shop-product', ShopProductViewSet, basename='shop_product')
urlpatterns = router.urls
