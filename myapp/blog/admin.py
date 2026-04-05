from django.contrib import admin
from .models import Post,Category,AboutUs


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_at')
    list_display_links = ('created_at',)
    list_per_page = 10
    list_filter = ('category',)
    search_fields = ('title',)
    

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
