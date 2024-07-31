from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodListView(APIView):

    def get(self, request, format=None):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
