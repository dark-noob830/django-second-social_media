from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'updated']
    search_fields = ('slug',)
    list_filter = ['updated']
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)


admin.site.register(Post, PostAdmin)
