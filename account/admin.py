from django.contrib import admin
from .models import  CustomUser,Book,Category
# Register your models here.
from django.contrib import admin
 
@admin.register(CustomUser)
class CustomUseradmin(admin.ModelAdmin):
  list_display = ['id','username', 'email']

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
  list_display = ['uid','categori_name']

@admin.register(Book)
class Bookadmin(admin.ModelAdmin):
  list_display = ['uid','name', 'author','book_category']
  raw_id_fields = ['author','book_category']

