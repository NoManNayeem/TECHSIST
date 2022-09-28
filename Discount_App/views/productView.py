from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models import Product
from ..serializers.productSerializer import ProductSerializer
from rest_framework import filters

class ProductList(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name',]

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProductDetail(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    

    # def put(self, request, id, format=None):
    #     product = self.get_object(id)
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data, partial=True) # setting partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class Add_Discount_All(APIView):
    def get_object(self, obj_id):
        try:
            return Product.objects.get(id=obj_id)
        except Product.DoesNotExist:
            raise Http404

    def validate_ids(self, id_list):
        for id in id_list:
            try:
                Product.objects.get(id=id)
            except Product.DoesNotExist:
                raise Http404
        return True
    

    def put(self, request, discount_id,*args, **kwargs):
        id_list = request.data['ids']
        self.validate_ids(id_list=id_list)
        instances = []
        for id in id_list:
            obj = self.get_object(obj_id=id)
            obj.discount = discount_id
            obj.save()
            instances.append(obj)
        serializer = ProductSerializer(instances, many=True)
        return Response(serializer.data)




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
        