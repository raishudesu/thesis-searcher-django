from django.contrib import admin
from .models import Thesis, Author, Keyword, Panelist, Adviser, Comment

# Register your models here.


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    filter_horizontal = ["authors", "panelists", "keywords"]
    list_display = [
        "title",
        "status",
        "published_date",
        "defense_date",
        "institution",
        "department",
    ]
    list_filter = ["published_date", "defense_date", "status"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'thesis', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']



admin.site.register([Author, Keyword, Panelist, Adviser])
