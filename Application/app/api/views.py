from rest_framework import viewsets
from .serializers import CropSerializer,PestSerializer,DiseaseSerializer,PostSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from app.models import Crop,Pest,Disease,Post

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset=Crop.objects.all()
    serializer_class=CropSerializer

class PestViewSet(viewsets.ModelViewSet):
    queryset=Pest.objects.all()
    serializer_class=PestSerializer 

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset=Disease.objects.all()
    serializer_class=DiseaseSerializer   
# class CropListView(ListAPIView):
# 	queryset=Crop.objects.all()
# 	serializer_class=CropSerializer
# class CropCreateView(CreateAPIView):
#     queryset=Crop.objects.all()
#     serializer_class = CropSerializer   	
# class CropDetailView(RetrieveAPIView):
# 	queryset=Crop.objects.all()
# 	serializer_class = CropSerializer
# class PestListView(ListAPIView):
#     queryset=Pest.objects.all()
#     serializer_class=PestSerializer
# class PestCreateView(CreateAPIView):
#     queryset=Pest.objects.all()
#     serializer_class = PestSerializer   	
# class PestDetailView(RetrieveAPIView):
# 	queryset=Pest.objects.all()
# 	serializer_class = PestSerializer

# class DiseaseListView(ListAPIView):
#     queryset=Disease.objects.all()
#     serializer_class=DiseaseSerializer
# class DiseaseCreateView(CreateAPIView):
#     queryset=Disease.objects.all()
#     serializer_class = DiseaseSerializer   	
# class DiseaseDetailView(RetrieveAPIView):
# 	queryset=Disease.objects.all()
# 	serializer_class = DiseaseSerializer