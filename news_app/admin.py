from django.contrib import admin

from .models import News, Category, Contact, PHOTOGRAPHY

class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = ['title','category','status','published_time']
    list_filter = ['category', 'status']
    prepopulated_fields = {'slug' : ['title',]}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','nomi']

class PHOTOGRAPHYAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact)
admin.site.register(PHOTOGRAPHY)