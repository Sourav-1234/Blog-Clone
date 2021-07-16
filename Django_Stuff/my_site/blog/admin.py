from django.contrib import admin
from . models import Post, Tag,Author,Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter= ("author","tags","date",)
    list_display =("title","date","author",)
    prepopulated_fileds={"slug":("title",)}



admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)



