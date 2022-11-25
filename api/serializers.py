from rest_framework import serializers
from .models import Car, News


# class ResumeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = ('model', 'marka', 'year', 'price', 'color')


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '_all_'


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '_all_'