from unicodedata import category
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from..serializers.discountSerializer import DiscountSerializer
from ..serializers.categorySerializer import CategorySerializer
from ..models import *


class ProductSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer(many=True)
    category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"
