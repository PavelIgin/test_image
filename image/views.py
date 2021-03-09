from rest_framework.views import APIView
from .serializer import ImageSaveSerializer
from rest_framework.response import Response


class ImageSaveView(APIView):

    def post(self, request):
        serializer = ImageSaveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': '200'})
