from django.contrib import admin
from .models import Thesis, Author, Keyword, Panelist

# Register your models here.


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    filter_horizontal = ["authors", "panelists", "keywords"]


admin.site.register([Author, Keyword, Panelist])


# @admin.register(models.Thesis)
# class ThesisAdmin(admin.ModelAdmin):
#     list_display = ["title", "abstract"]
