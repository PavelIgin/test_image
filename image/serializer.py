from rest_framework.serializers import ModelSerializer
from .models import ImageSave


class ImageSaveSerializer(ModelSerializer):
    class Meta:
        model = ImageSave
        fields = '__all__'
