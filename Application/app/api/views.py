from rest_framework import viewsets
from .serializers import CropSerializer,PesticideSerializer,DiseaseSerializer,PostSerializer,ShopSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from app.models import Crop,Pesticide,Disease,Post,Shop

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset=Crop.objects.all()
    serializer_class=CropSerializer

class PesticideViewSet(viewsets.ModelViewSet):
    queryset=Pesticide.objects.all()
    serializer_class=PesticideSerializer 

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset=Disease.objects.all()
    serializer_class=DiseaseSerializer   

class ShopViewSet(viewsets.ModelViewSet):
    queryset=Shop.objects.all()
    serializer_class=ShopSerializer

class DiseaseList(ListAPIView):
    serializer_class = CropSerializer

    def get_queryset(self):
        crop = self.request.crop
        return Disease.objects.filter(crop_id=crop)   
        
# class CropListView(ListAPIView):
# 	queryset=Crop.objects.all()
# 	serializer_class=CropSerializer
# class CropCreateView(CreateAPIView):
#     queryset=Crop.objects.all()
#     serializer_class = CropSerializer   	
# class CropDetailView(RetrieveAPIView):
# 	queryset=Crop.objects.all()
# 	serializer_class = CropSerializer
# class PesticideListView(ListAPIView):
#     queryset=Pesticide.objects.all()
#     serializer_class=PesticideSerializer
# class PesticideCreateView(CreateAPIView):
#     queryset=Pesticide.objects.all()
#     serializer_class = PesticideSerializer   	
# class PesticideDetailView(RetrieveAPIView):
# 	queryset=Pesticide.objects.all()
# 	serializer_class = PesticideSerializer

# class DiseaseListView(ListAPIView):
#     queryset=Disease.objects.all()
#     serializer_class=DiseaseSerializer
# class DiseaseCreateView(CreateAPIView):
#     queryset=Disease.objects.all()
#     serializer_class = DiseaseSerializer   	
# class DiseaseDetailView(RetrieveAPIView):
# 	queryset=Disease.objects.all()
# 	serializer_class = DiseaseSerializer