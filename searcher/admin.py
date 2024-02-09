from django.contrib import admin
from .models import Thesis, Author, Keyword, Panelist, Adviser

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


admin.site.register([Author, Keyword, Panelist, Adviser])
