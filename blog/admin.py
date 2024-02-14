from django.contrib import admin
from .models import Post,Comment

# Register your models here.


class ProductAdmin(admin.ModelAdmin) :
    list_filter = ['created_at']




admin.site.register(Post)
admin.site.register(Comment,ProductAdmin)
