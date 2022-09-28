from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models import *
from ..serializers.categorySerializer import CategorySerializer
from rest_framework import filters

class CategoryList(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=category_name',]

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CategoryDetail(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        category = self.get_object(id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def patch(self, request, id):
        category = self.get_object(id)
        serializer = CategorySerializer(category, data=request.data, partial=True) # setting partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

