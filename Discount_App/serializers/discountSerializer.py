from django.contrib.auth.models import User, Group
from rest_framework import serializers


from ..models import *


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"

        # def __init__(self, *args, **kwargs):
        #     kwargs['partial'] = True
        #     super(DiscountSerializer, self).__init__(*args, **kwargs)