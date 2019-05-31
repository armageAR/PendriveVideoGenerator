from django.contrib import admin

from .models import Category, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video)
