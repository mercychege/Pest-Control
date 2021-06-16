from rest_framework import serializers
from app.models import Crop,Pesticide,Disease,Post,Shop, ShopProduct


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crop
        fields='__all__'


class PesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pesticide
        fields='__all__'


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disease
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields='__all__'

class ShopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShopProduct
        fields='__all__'