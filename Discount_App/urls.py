from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

from .views.discountView import *
from .views.productView import *
from .views.categoryView import *

urlpatterns = [
    ### Discount URLS ###
    path('discounts/', DiscountList.as_view()),
    path('discounts/<int:id>/', DiscountDetail.as_view()),

    ### Category URLS ###
    path('categories/', CategoryList.as_view()),
    path('categories/<int:id>/', CategoryDetail.as_view()),


    ### Product URLS ###
    path('products/', ProductList.as_view()),
    path('products/<int:id>/', ProductDetail.as_view()),
    path('products/add-discount/', Add_Discount_All.as_view()),

    ### Auth Token ###
    path('login/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
]