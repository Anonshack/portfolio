from django.contrib import admin
from .models import Review, Project


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'rating', 'is_approved', 'created_at')
    list_editable = ('is_approved',)
    list_filter = ('is_approved', 'rating')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    fields = ('title', 'description', 'tech_stack', 'link', 'github',
              'image1', 'image2', 'image3', 'order', 'is_active')
