from rest_framework import serializers
from app.models import Crop,Pest,Disease,Post


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crop
        fields='__all__'


class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pest
        fields='__all__'


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disease
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'