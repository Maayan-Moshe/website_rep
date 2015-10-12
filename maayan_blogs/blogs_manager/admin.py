from django.contrib import admin

# Register your models here.

from .models import WildBlog, WebPageContentLocation

class WebPageContentLocationInline(admin.TabularInline):
    model = WebPageContentLocation
    extra = 3


class WildBlogAdmin(admin.ModelAdmin):
    
    inlines = [WebPageContentLocationInline]

admin.site.register(WildBlog, WildBlogAdmin)
admin.site.register(WebPageContentLocation)
