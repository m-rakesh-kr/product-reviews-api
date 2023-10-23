from django.contrib import admin
from .models import Product, Category, Company, ProductSize, ProductSite, Comment
from django.contrib.auth.models import Group

# admin.site.unregister(Group)
admin.site.site_header = "Product Review Admin"


# Method_1 (admin.register() decorator)
# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    list_filter = ('category',)


# Method_2 (admin.site.register method)
admin.site.register(Product, ProductAdmin)


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


# admin.site.register(Company)
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'url')


# admin.site.register(ProductSize)
@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


# admin.site.register(ProductSite)
@admin.register(ProductSite)
class ProductSiteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'product', 'company', 'price', 'url')


# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'product', 'user', 'created', 'updated')

