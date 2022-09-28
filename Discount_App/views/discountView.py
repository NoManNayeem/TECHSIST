from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models import Discount
from ..serializers.discountSerializer import DiscountSerializer
from ..customFilters.discountFilters import DiscountFilter
from rest_framework import filters

class DiscountList(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    # filter_class = DiscountFilter ## Use if needed
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name',]

    def get(self, request, format=None):
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DiscountDetail(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def get_object(self, id):
        try:
            return Discount.objects.get(id=id)
        except Discount.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        discount = self.get_object(id)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data)
    

    # def put(self, request, id, format=None):
    #     discount = self.get_object(id)
    #     serializer = DiscountSerializer(discount, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        discount = self.get_object(id)
        serializer = DiscountSerializer(discount, data=request.data, partial=True) # setting partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        discount = self.get_object(id)
        discount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class ValidDiscountDetail(APIView):
#     # permission_classes = (IsAuthenticated,)
#     permission_classes = (AllowAny,)
#     # filter_class = DiscountFilter ## Use if needed
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name',]

#     def get(self, request, format=None):
#         discounts = Discount.objects.filter(Is_Valid=True)
#         serializer = DiscountSerializer(discounts, many=True)
#         return Response(serializer.data)
        