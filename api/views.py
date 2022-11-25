from rest_framework import generics
from .models import Car, News
from .serializers import CarSerializers,NewsSerializers


# class ResumeAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = ResumeSerializer

class CarAPIViews(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class NewsApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers