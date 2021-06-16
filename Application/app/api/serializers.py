from rest_framework import serializers
from app.models import Crop,Pesticide,Disease,Post,Shop


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