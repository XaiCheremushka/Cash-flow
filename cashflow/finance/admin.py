from django.contrib import admin

from .models import *


@admin.register(Category)
class CashFlowCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'slug']
    readonly_fields = ['slug']

    list_display = ['name', 'type', 'slug']
    list_display_links = ['name']
    ordering = ['type', 'name']


@admin.register(Subcategory)
class CashFlowSubcategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'slug']
    readonly_fields = ['slug']

    list_display = ['name', 'category', 'slug']
    list_display_links = ['name']
    ordering = ['category', 'name']
    list_filter = ['category']


@admin.register(Type)
class CashFlowTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    readonly_fields = ['slug']

    list_display = ['name', 'slug']
    list_display_links = ['name']
    ordering = ['name']


@admin.register(Status)
class CashFlowStatusAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    readonly_fields = ['slug']

    list_display = ['name', 'slug']
    list_display_links = ['name']
    ordering = ['name']


@admin.register(Currency)
class CashFlowCurrencyAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'symbol']

    list_display = ['name', 'code', 'symbol']
    list_display_links = ['name']
    ordering = ['name']


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    fields = ['date_created', 'status', 'type', 'subcategory', 'amount', 'currency', 'comment']

    list_display = ['date_created', 'status', 'type', 'subcategory', 'amount', 'currency']
    list_display_links = ['date_created']
    ordering = ['-date_created']
    list_filter = ['date_created', 'status', 'type', 'subcategory']
