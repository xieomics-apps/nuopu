from django.contrib import admin
from basicapp.models import (Platform, Post, 
                             Service, Category, 
                             Aboutus, SiteSetting, 
                             ContactInfo)
# Register your models here.

admin.site.register(Platform)

class PostAdmin(admin.ModelAdmin):
   model = Post
   list_display = ('title', 'slug', 'author', 'publish',
                   'status', 'updated')
admin.site.register(Post, PostAdmin)

class ServiceAdmin(admin.ModelAdmin):
   model = Service
   list_display = ('title', 'slug', 'publish',
                   'status', 'updated')
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category)

admin.site.register(Aboutus)

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(ContactInfo)
