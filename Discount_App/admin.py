from django.contrib import admin
from .models import Discount
# Register your models here.




@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("name","discount_type","discount_category",)
    list_filter = ("name","discount_type","discount_category",)

