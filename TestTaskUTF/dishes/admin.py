from django.contrib import admin

from .models import *


@admin.register(FoodCategory)
class FoodCategory(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id')
    list_filter = ('name_ru', 'order_id')


@admin.register(Food)
class Food(admin.ModelAdmin):
    list_display = (
        'id', 'category', 'is_vegan', 'is_special', 'code', 'internal_code', 'name_ru', 'description_ru',
        'description_en', 'description_ch', 'cost', 'is_publish')
    list_filter = ('category', 'is_publish')
